"""
Aplicação Flask para produção no Hostinger
"""
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
import json
import sys
import os
from datetime import datetime
import pandas as pd
from pathlib import Path

# Adicionar o diretório atual ao path
sys.path.append('.')

# Importar configurações de produção
try:
    from config_prod import ConfigProducao
    config_class = ConfigProducao
except ImportError:
    # Fallback para configuração padrão
    from config import config
    config_class = None

# Importar os agentes
from agente_suporte import AgenteSuporte
from agente_conteudo import AgenteConteudo
from agente_vendas import AgenteAnaliseVendas
from agente_automatizado import AgenteAutomatizado
from database import db_manager
from integracoes import gerenciador_integracoes
from config import config

app = Flask(__name__)

# Configurar aplicação
if config_class:
    app.config.from_object(config_class)
else:
    app.secret_key = os.environ.get('SECRET_KEY', 'agente_ia_secret_key_2024')

# Inicializar agentes
agente_suporte = AgenteSuporte()
agente_conteudo = AgenteConteudo()
agente_vendas = AgenteAnaliseVendas()
agente_automatizado = AgenteAutomatizado()

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/suporte')
def suporte():
    """Página do agente de suporte"""
    return render_template('suporte.html')

@app.route('/conteudo')
def conteudo():
    """Página do agente de conteúdo"""
    return render_template('conteudo.html')

@app.route('/vendas')
def vendas():
    """Página do agente de vendas"""
    return render_template('vendas.html')

@app.route('/dashboard')
def dashboard():
    """Dashboard com estatísticas"""
    try:
        stats = db_manager.obter_estatisticas()
        return render_template('dashboard.html', stats=stats)
    except Exception as e:
        return render_template('dashboard.html', stats={}, error=str(e))

@app.route('/configuracao')
def configuracao():
    """Página de configuração"""
    return render_template('configuracao.html')

# API Routes
@app.route('/api/suporte', methods=['POST'])
def api_suporte():
    """API para processar solicitações de suporte"""
    try:
        data = request.get_json()
        pergunta = data.get('pergunta', '')
        
        if not pergunta:
            return jsonify({'erro': 'Pergunta é obrigatória'}), 400
        
        resultado = agente_suporte.processar_solicitacao(pergunta)
        
        if resultado.get('sucesso'):
            return jsonify({
                'sucesso': True,
                'resposta': resultado['dados']['resposta'],
                'urgencia': resultado['dados']['urgencia'],
                'timestamp': resultado['dados']['timestamp']
            })
        else:
            return jsonify({'erro': resultado.get('erro', 'Erro desconhecido')}), 500
            
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/conteudo', methods=['POST'])
def api_conteudo():
    """API para gerar conteúdo"""
    try:
        data = request.get_json()
        tipo = data.get('tipo', 'post')
        
        if tipo == 'post':
            tema = data.get('tema', '')
            plataforma = data.get('plataforma', 'Instagram')
            tom = data.get('tom', 'profissional')
            publico_alvo = data.get('publico_alvo', 'geral')
            
            if not tema:
                return jsonify({'erro': 'Tema é obrigatório'}), 400
            
            conteudo = agente_conteudo.gerar_post_social(tema, plataforma, tom, publico_alvo)
            
            return jsonify({
                'sucesso': True,
                'conteudo': conteudo,
                'tipo': 'post',
                'plataforma': plataforma,
                'timestamp': datetime.now().isoformat()
            })
        
        elif tipo == 'newsletter':
            topicos = data.get('topicos', [])
            publico_alvo = data.get('publico_alvo', '')
            empresa = data.get('empresa', 'Nossa empresa')
            
            if not topicos or not publico_alvo:
                return jsonify({'erro': 'Tópicos e público-alvo são obrigatórios'}), 400
            
            conteudo = agente_conteudo.criar_newsletter(topicos, publico_alvo, empresa)
            
            return jsonify({
                'sucesso': True,
                'conteudo': conteudo,
                'tipo': 'newsletter',
                'timestamp': datetime.now().isoformat()
            })
        
        else:
            return jsonify({'erro': 'Tipo de conteúdo inválido'}), 400
            
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/vendas', methods=['POST'])
def api_vendas():
    """API para análise de vendas"""
    try:
        # Verificar se há arquivo enviado
        if 'arquivo' not in request.files:
            return jsonify({'erro': 'Nenhum arquivo enviado'}), 400
        
        arquivo = request.files['arquivo']
        if arquivo.filename == '':
            return jsonify({'erro': 'Nenhum arquivo selecionado'}), 400
        
        # Salvar arquivo temporariamente
        upload_dir = Path('uploads')
        upload_dir.mkdir(exist_ok=True)
        
        arquivo_path = upload_dir / arquivo.filename
        arquivo.save(arquivo_path)
        
        # Processar com agente de vendas
        resultado = agente_vendas.executar_analise(str(arquivo_path))
        
        # Remover arquivo temporário
        arquivo_path.unlink()
        
        if resultado.get('sucesso'):
            return jsonify({
                'sucesso': True,
                'insights': resultado['dados']['insights'],
                'resumo': resultado['dados']['resumo'],
                'timestamp': resultado['dados']['timestamp']
            })
        else:
            return jsonify({'erro': resultado.get('erro', 'Erro na análise')}), 500
            
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/estatisticas')
def api_estatisticas():
    """API para obter estatísticas"""
    try:
        stats = db_manager.obter_estatisticas()
        return jsonify({'sucesso': True, 'dados': stats})
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/integracoes/teste', methods=['POST'])
def api_testar_integracoes():
    """API para testar integrações"""
    try:
        mensagem = request.json.get('mensagem', 'Teste do sistema web')
        resultados = gerenciador_integracoes.enviar_notificacao_global(mensagem, "teste")
        
        return jsonify({
            'sucesso': True,
            'resultados': resultados,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/configuracao', methods=['GET', 'POST'])
def api_configuracao():
    """API para configurações"""
    if request.method == 'GET':
        try:
            return jsonify({
                'sucesso': True,
                'config': {
                    'apis': config.API_CONFIG,
                    'integracoes': config.INTEGRACOES,
                    'database': config.DATABASE_CONFIG,
                    'logging': config.LOGGING_CONFIG
                }
            })
        except Exception as e:
            return jsonify({'erro': str(e)}), 500
    
    elif request.method == 'POST':
        try:
            data = request.get_json()
            secao = data.get('secao')
            chave = data.get('chave')
            valor = data.get('valor')
            
            if not all([secao, chave, valor]):
                return jsonify({'erro': 'Seção, chave e valor são obrigatórios'}), 400
            
            config.atualizar_configuracao(secao, chave, valor)
            
            return jsonify({'sucesso': True, 'mensagem': 'Configuração atualizada'})
        except Exception as e:
            return jsonify({'erro': str(e)}), 500

# Rota de saúde para verificar se a aplicação está funcionando
@app.route('/health')
def health():
    """Endpoint de saúde da aplicação"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

if __name__ == '__main__':
    # Criar diretórios necessários
    Path('uploads').mkdir(exist_ok=True)
    Path('templates').mkdir(exist_ok=True)
    Path('static').mkdir(exist_ok=True)
    Path('static/css').mkdir(exist_ok=True)
    Path('static/js').mkdir(exist_ok=True)
    
    print("🌐 Iniciando aplicação para produção...")
    print("📱 Acesse: http://localhost:5000")
    app.run(debug=False, host='0.0.0.0', port=5000)
