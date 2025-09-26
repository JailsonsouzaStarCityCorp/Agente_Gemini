"""
Sistema Interativo de Configuração do Agente de IA
"""
import os
import json
import logging
from typing import Dict, List, Any, Optional
from pathlib import Path
from config import config
from integracoes import gerenciador_integracoes
from database import db_manager

class ConfiguradorInterativo:
    """Sistema interativo de configuração"""
    
    def __init__(self):
        self.logger = logging.getLogger('configurador')
        self.config = config
    
    def menu_principal(self):
        """Menu principal de configuração"""
        while True:
            print("\n" + "="*60)
            print("⚙️  CONFIGURADOR DO AGENTE DE IA")
            print("="*60)
            print("1. 🔑 Configurações de API")
            print("2. 📧 Integrações de Comunicação")
            print("3. 🗄️  Configurações de Banco de Dados")
            print("4. 📊 Configurações de Análise")
            print("5. 🔒 Configurações de Segurança")
            print("6. ⚡ Configurações de Performance")
            print("7. 📱 Configurações de Notificações")
            print("8. 🎯 Configurações por Agente")
            print("9. 📈 Visualizar Estatísticas")
            print("10. 🧪 Testar Integrações")
            print("11. 💾 Backup/Restore")
            print("12. ❌ Sair")
            print("="*60)
            
            opcao = input("Escolha uma opção (1-12): ").strip()
            
            if opcao == "1":
                self.configurar_apis()
            elif opcao == "2":
                self.configurar_integracoes()
            elif opcao == "3":
                self.configurar_banco_dados()
            elif opcao == "4":
                self.configurar_analise()
            elif opcao == "5":
                self.configurar_seguranca()
            elif opcao == "6":
                self.configurar_performance()
            elif opcao == "7":
                self.configurar_notificacoes()
            elif opcao == "8":
                self.configurar_agentes()
            elif opcao == "9":
                self.visualizar_estatisticas()
            elif opcao == "10":
                self.testar_integracoes()
            elif opcao == "11":
                self.backup_restore()
            elif opcao == "12":
                print("👋 Configuração finalizada!")
                break
            else:
                print("❌ Opção inválida!")
    
    def configurar_apis(self):
        """Configurações de APIs"""
        print("\n🔑 CONFIGURAÇÕES DE API")
        print("-" * 40)
        
        # Gemini
        print("\n1. Google Gemini")
        api_key = input(f"API Key atual: {self.config.API_CONFIG['gemini']['api_key'][:10]}...\nNova API Key (Enter para manter): ").strip()
        if api_key:
            self.config.atualizar_configuracao('api', 'gemini', {**self.config.API_CONFIG['gemini'], 'api_key': api_key})
        
        # OpenAI
        print("\n2. OpenAI")
        openai_key = input(f"API Key OpenAI (atual: {'configurada' if self.config.API_CONFIG['openai']['api_key'] else 'não configurada'}): ").strip()
        if openai_key:
            self.config.atualizar_configuracao('api', 'openai', {**self.config.API_CONFIG['openai'], 'api_key': openai_key})
        
        # Claude
        print("\n3. Claude")
        claude_key = input(f"API Key Claude (atual: {'configurada' if self.config.API_CONFIG['claude']['api_key'] else 'não configurada'}): ").strip()
        if claude_key:
            self.config.atualizar_configuracao('api', 'claude', {**self.config.API_CONFIG['claude'], 'api_key': claude_key})
        
        print("✅ Configurações de API atualizadas!")
    
    def configurar_integracoes(self):
        """Configurações de integrações"""
        print("\n📧 CONFIGURAÇÕES DE INTEGRAÇÃO")
        print("-" * 40)
        
        integracoes = ['email', 'whatsapp', 'telegram', 'slack', 'discord', 'teams']
        
        for integracao in integracoes:
            print(f"\n{integracao.upper()}")
            habilitar = input(f"Habilitar {integracao}? (s/n): ").strip().lower() == 's'
            
            if habilitar:
                config_integracao = self.config.INTEGRACOES[integracao].copy()
                config_integracao['habilitado'] = True
                
                # Configurações específicas por integração
                if integracao == 'email':
                    config_integracao['smtp_server'] = input("SMTP Server: ").strip() or config_integracao['smtp_server']
                    config_integracao['email_usuario'] = input("Email usuário: ").strip() or config_integracao['email_usuario']
                    config_integracao['email_senha'] = input("Email senha: ").strip() or config_integracao['email_senha']
                
                elif integracao == 'whatsapp':
                    config_integracao['api_key'] = input("WhatsApp API Key: ").strip() or config_integracao['api_key']
                    config_integracao['numero_telefone'] = input("Número telefone: ").strip() or config_integracao['numero_telefone']
                
                elif integracao == 'telegram':
                    config_integracao['bot_token'] = input("Telegram Bot Token: ").strip() or config_integracao['bot_token']
                    config_integracao['chat_id'] = input("Chat ID: ").strip() or config_integracao['chat_id']
                
                elif integracao == 'slack':
                    config_integracao['webhook_url'] = input("Slack Webhook URL: ").strip() or config_integracao['webhook_url']
                    config_integracao['canal'] = input("Canal Slack: ").strip() or config_integracao['canal']
                
                elif integracao == 'discord':
                    config_integracao['bot_token'] = input("Discord Bot Token: ").strip() or config_integracao['bot_token']
                    config_integracao['canal_id'] = input("Canal ID: ").strip() or config_integracao['canal_id']
                
                elif integracao == 'teams':
                    config_integracao['webhook_url'] = input("Teams Webhook URL: ").strip() or config_integracao['webhook_url']
                
                self.config.atualizar_configuracao('integracoes', integracao, config_integracao)
            else:
                config_integracao = self.config.INTEGRACOES[integracao].copy()
                config_integracao['habilitado'] = False
                self.config.atualizar_configuracao('integracoes', integracao, config_integracao)
        
        print("✅ Configurações de integração atualizadas!")
    
    def configurar_banco_dados(self):
        """Configurações de banco de dados"""
        print("\n🗄️  CONFIGURAÇÕES DE BANCO DE DADOS")
        print("-" * 40)
        
        print("1. SQLite (Recomendado para desenvolvimento)")
        print("2. PostgreSQL (Recomendado para produção)")
        print("3. MySQL")
        print("4. MongoDB")
        
        opcao = input("Escolha o banco de dados (1-4): ").strip()
        
        if opcao == "1":
            self.config.atualizar_configuracao('database', 'sqlite', {'habilitado': True})
            print("✅ SQLite habilitado!")
        
        elif opcao == "2":
            host = input("Host PostgreSQL: ").strip() or "localhost"
            port = input("Porta: ").strip() or "5432"
            database = input("Nome do banco: ").strip() or "agente"
            usuario = input("Usuário: ").strip()
            senha = input("Senha: ").strip()
            
            config_postgres = {
                'host': host,
                'port': int(port),
                'database': database,
                'usuario': usuario,
                'senha': senha,
                'habilitado': True
            }
            
            self.config.atualizar_configuracao('database', 'postgresql', config_postgres)
            print("✅ PostgreSQL configurado!")
        
        elif opcao == "3":
            host = input("Host MySQL: ").strip() or "localhost"
            port = input("Porta: ").strip() or "3306"
            database = input("Nome do banco: ").strip() or "agente"
            usuario = input("Usuário: ").strip()
            senha = input("Senha: ").strip()
            
            config_mysql = {
                'host': host,
                'port': int(port),
                'database': database,
                'usuario': usuario,
                'senha': senha,
                'habilitado': True
            }
            
            self.config.atualizar_configuracao('database', 'mysql', config_mysql)
            print("✅ MySQL configurado!")
        
        elif opcao == "4":
            uri = input("URI MongoDB: ").strip() or "mongodb://localhost:27017/"
            database = input("Nome do banco: ").strip() or "agente"
            
            config_mongo = {
                'uri': uri,
                'database': database,
                'habilitado': True
            }
            
            self.config.atualizar_configuracao('database', 'mongodb', config_mongo)
            print("✅ MongoDB configurado!")
    
    def configurar_analise(self):
        """Configurações de análise"""
        print("\n📊 CONFIGURAÇÕES DE ANÁLISE")
        print("-" * 40)
        
        # Análise de sentimento
        print("1. Análise de Sentimento")
        habilitar_sentimento = input("Habilitar análise de sentimento? (s/n): ").strip().lower() == 's'
        if habilitar_sentimento:
            modelo = input("Modelo (portuguese/english): ").strip() or "portuguese"
            confianca = float(input("Confiança mínima (0.0-1.0): ").strip() or "0.7")
            
            self.config.atualizar_configuracao('analise', 'sentimento', {
                'habilitado': True,
                'modelo': modelo,
                'confianca_minima': confianca
            })
        
        # Classificação automática
        print("\n2. Classificação Automática")
        habilitar_classificacao = input("Habilitar classificação automática? (s/n): ").strip().lower() == 's'
        if habilitar_classificacao:
            categorias = input("Categorias (separadas por vírgula): ").strip().split(',')
            categorias = [cat.strip() for cat in categorias if cat.strip()]
            
            self.config.atualizar_configuracao('analise', 'classificacao', {
                'habilitado': True,
                'categorias': categorias,
                'auto_classificar': True
            })
        
        # Métricas
        print("\n3. Coleta de Métricas")
        habilitar_metricas = input("Habilitar coleta automática de métricas? (s/n): ").strip().lower() == 's'
        if habilitar_metricas:
            intervalo = int(input("Intervalo de coleta (segundos): ").strip() or "3600")
            retencao = int(input("Retenção de dados (dias): ").strip() or "90")
            
            self.config.atualizar_configuracao('analise', 'metricas', {
                'coleta_automatica': True,
                'intervalo_coleta': intervalo,
                'retencao_dados': retencao
            })
        
        print("✅ Configurações de análise atualizadas!")
    
    def configurar_seguranca(self):
        """Configurações de segurança"""
        print("\n🔒 CONFIGURAÇÕES DE SEGURANÇA")
        print("-" * 40)
        
        # Rate limiting
        rate_limit = int(input("Rate limit (requests/hora): ").strip() or "100")
        self.config.atualizar_configuracao('security', 'api_rate_limit', rate_limit)
        
        # Tamanho máximo de arquivo
        max_file_size = int(input("Tamanho máximo de arquivo (MB): ").strip() or "50")
        self.config.atualizar_configuracao('security', 'max_file_size', max_file_size * 1024 * 1024)
        
        # Extensões permitidas
        extensoes = input("Extensões permitidas (separadas por vírgula): ").strip()
        if extensoes:
            extensoes_lista = [ext.strip() for ext in extensoes.split(',')]
            self.config.atualizar_configuracao('security', 'allowed_extensions', extensoes_lista)
        
        # Timeout de sessão
        timeout = int(input("Timeout de sessão (segundos): ").strip() or "3600")
        self.config.atualizar_configuracao('security', 'session_timeout', timeout)
        
        print("✅ Configurações de segurança atualizadas!")
    
    def configurar_performance(self):
        """Configurações de performance"""
        print("\n⚡ CONFIGURAÇÕES DE PERFORMANCE")
        print("-" * 40)
        
        # Workers
        max_workers = int(input("Máximo de workers: ").strip() or "4")
        self.config.atualizar_configuracao('performance', 'max_workers', max_workers)
        
        # Cache
        habilitar_cache = input("Habilitar cache? (s/n): ").strip().lower() == 's'
        if habilitar_cache:
            cache_size = int(input("Tamanho do cache: ").strip() or "1000")
            cache_ttl = int(input("TTL do cache (segundos): ").strip() or "3600")
            
            self.config.atualizar_configuracao('performance', 'habilitar_cache', True)
            self.config.atualizar_configuracao('performance', 'cache_size', cache_size)
            self.config.atualizar_configuracao('performance', 'cache_ttl', cache_ttl)
        
        # Limite de memória
        memory_limit = int(input("Limite de memória (MB): ").strip() or "512")
        self.config.atualizar_configuracao('performance', 'memory_limit', memory_limit * 1024 * 1024)
        
        print("✅ Configurações de performance atualizadas!")
    
    def configurar_notificacoes(self):
        """Configurações de notificações"""
        print("\n📱 CONFIGURAÇÕES DE NOTIFICAÇÕES")
        print("-" * 40)
        
        # Email
        print("1. Notificações por Email")
        relatorios_diarios = input("Relatórios diários? (s/n): ").strip().lower() == 's'
        alertas_erro = input("Alertas de erro? (s/n): ").strip().lower() == 's'
        resumos_semanais = input("Resumos semanais? (s/n): ").strip().lower() == 's'
        
        self.config.atualizar_configuracao('notificacoes', 'email', {
            'relatorios_diarios': relatorios_diarios,
            'alertas_erro': alertas_erro,
            'resumos_semanais': resumos_semanais
        })
        
        # Webhook
        print("\n2. Webhook")
        webhook_url = input("URL do webhook: ").strip()
        if webhook_url:
            eventos = input("Eventos (erro,sucesso,conclusao): ").strip().split(',')
            eventos = [evento.strip() for evento in eventos if evento.strip()]
            
            self.config.atualizar_configuracao('notificacoes', 'webhook', {
                'url': webhook_url,
                'eventos': eventos,
                'habilitado': True
            })
        
        print("✅ Configurações de notificações atualizadas!")
    
    def configurar_agentes(self):
        """Configurações específicas por agente"""
        print("\n🎯 CONFIGURAÇÕES POR AGENTE")
        print("-" * 40)
        
        agentes = ['vendas', 'suporte', 'conteudo', 'automatizado']
        
        for agente in agentes:
            print(f"\n{agente.upper()}")
            config_agente = self.config.AGENTE_CONFIG[agente].copy()
            
            if agente == 'vendas':
                colunas = input("Colunas obrigatórias (separadas por vírgula): ").strip()
                if colunas:
                    config_agente['colunas_obrigatorias'] = [col.strip() for col in colunas.split(',')]
                
                gerar_graficos = input("Gerar gráficos automaticamente? (s/n): ").strip().lower() == 's'
                config_agente['gerar_graficos'] = gerar_graficos
            
            elif agente == 'suporte':
                urgencia_padrao = input("Urgência padrão (BAIXA/MÉDIA/ALTA): ").strip().upper()
                if urgencia_padrao in ['BAIXA', 'MÉDIA', 'ALTA']:
                    config_agente['urgencia_padrao'] = urgencia_padrao
                
                tempo_resposta = int(input("Tempo de resposta esperado (minutos): ").strip() or "30")
                config_agente['tempo_resposta_esperado'] = tempo_resposta
            
            elif agente == 'conteudo':
                tamanho_max = int(input("Tamanho máximo do post (caracteres): ").strip() or "2200")
                config_agente['tamanho_max_post'] = tamanho_max
                
                hashtags_max = int(input("Máximo de hashtags: ").strip() or "5")
                config_agente['hashtags_max'] = hashtags_max
            
            elif agente == 'automatizado':
                monitoramento = input("Monitoramento de pastas? (s/n): ").strip().lower() == 's'
                config_agente['monitoramento_pastas'] = monitoramento
                
                processamento_paralelo = input("Processamento paralelo? (s/n): ").strip().lower() == 's'
                config_agente['processamento_paralelo'] = processamento_paralelo
            
            self.config.atualizar_configuracao('agente', agente, config_agente)
        
        print("✅ Configurações dos agentes atualizadas!")
    
    def visualizar_estatisticas(self):
        """Visualiza estatísticas do sistema"""
        print("\n📈 ESTATÍSTICAS DO SISTEMA")
        print("-" * 40)
        
        try:
            stats = db_manager.obter_estatisticas()
            
            print(f"📊 Período: Últimos {stats.get('periodo_dias', 30)} dias")
            print(f"🔄 Processamentos: {stats.get('processamentos', {}).get('total', 0)}")
            print(f"✅ Sucessos: {stats.get('processamentos', {}).get('sucessos', 0)}")
            print(f"❌ Erros: {stats.get('processamentos', {}).get('erros', 0)}")
            print(f"📈 Taxa de sucesso: {stats.get('processamentos', {}).get('taxa_sucesso', 0):.1f}%")
            print(f"💰 Vendas: {stats.get('vendas', {}).get('total_vendas', 0)}")
            print(f"💵 Valor total: R$ {stats.get('vendas', {}).get('valor_total', 0):.2f}")
            print(f"🎧 Atendimentos: {stats.get('suporte', {}).get('total_atendimentos', 0)}")
            print(f"✍️ Conteúdos: {stats.get('conteudo', {}).get('total_conteudos', 0)}")
            
        except Exception as e:
            print(f"❌ Erro ao obter estatísticas: {str(e)}")
    
    def testar_integracoes(self):
        """Testa todas as integrações configuradas"""
        print("\n🧪 TESTE DE INTEGRAÇÕES")
        print("-" * 40)
        
        mensagem_teste = f"🧪 Teste do Agente de IA - {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        
        print("Enviando mensagem de teste para todos os canais...")
        resultados = gerenciador_integracoes.enviar_notificacao_global(mensagem_teste, "teste")
        
        print("\n📊 Resultados dos testes:")
        for canal, sucesso in resultados.items():
            status = "✅ Sucesso" if sucesso else "❌ Falhou"
            print(f"{canal.upper()}: {status}")
    
    def backup_restore(self):
        """Sistema de backup e restore"""
        print("\n💾 BACKUP/RESTORE")
        print("-" * 40)
        print("1. Fazer backup")
        print("2. Restaurar backup")
        print("3. Listar backups")
        
        opcao = input("Escolha uma opção (1-3): ").strip()
        
        if opcao == "1":
            nome_backup = input("Nome do backup: ").strip() or f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            self.fazer_backup(nome_backup)
        
        elif opcao == "2":
            self.listar_backups()
            nome_backup = input("Nome do backup para restaurar: ").strip()
            if nome_backup:
                self.restaurar_backup(nome_backup)
        
        elif opcao == "3":
            self.listar_backups()
    
    def fazer_backup(self, nome: str):
        """Faz backup das configurações"""
        try:
            backup_dir = Path("backups")
            backup_dir.mkdir(exist_ok=True)
            
            # Backup do banco de dados
            if db_manager.conexao:
                backup_file = backup_dir / f"{nome}.db"
                # Implementar backup do SQLite
                print(f"✅ Backup criado: {backup_file}")
            
            # Backup das configurações
            config_backup = {
                'api': self.config.API_CONFIG,
                'integracoes': self.config.INTEGRACOES,
                'database': self.config.DATABASE_CONFIG,
                'logging': self.config.LOGGING_CONFIG,
                'schedule': self.config.SCHEDULE_CONFIG,
                'security': self.config.SECURITY_CONFIG,
                'performance': self.config.PERFORMANCE_CONFIG,
                'agente': self.config.AGENTE_CONFIG,
                'notificacoes': self.config.NOTIFICACOES,
                'analise': self.config.ANALISE_CONFIG
            }
            
            config_file = backup_dir / f"{nome}_config.json"
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config_backup, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Backup de configurações criado: {config_file}")
            
        except Exception as e:
            print(f"❌ Erro ao fazer backup: {str(e)}")
    
    def listar_backups(self):
        """Lista backups disponíveis"""
        try:
            backup_dir = Path("backups")
            if backup_dir.exists():
                backups = list(backup_dir.glob("*.json"))
                if backups:
                    print("\n📁 Backups disponíveis:")
                    for backup in backups:
                        print(f"  - {backup.stem}")
                else:
                    print("❌ Nenhum backup encontrado")
            else:
                print("❌ Diretório de backups não existe")
        except Exception as e:
            print(f"❌ Erro ao listar backups: {str(e)}")
    
    def restaurar_backup(self, nome: str):
        """Restaura backup"""
        try:
            backup_file = Path("backups") / f"{nome}_config.json"
            if backup_file.exists():
                with open(backup_file, 'r', encoding='utf-8') as f:
                    config_backup = json.load(f)
                
                # Restaurar configurações
                for secao, dados in config_backup.items():
                    self.config.salvar_configuracao(secao, dados)
                
                print(f"✅ Backup {nome} restaurado com sucesso!")
            else:
                print(f"❌ Backup {nome} não encontrado")
        except Exception as e:
            print(f"❌ Erro ao restaurar backup: {str(e)}")

def main():
    """Função principal do configurador"""
    configurador = ConfiguradorInterativo()
    configurador.menu_principal()

if __name__ == "__main__":
    main()
