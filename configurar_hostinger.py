"""
Script para configurar automaticamente o deploy no Hostinger
"""
import os
import shutil
from pathlib import Path

def criar_arquivo_configuracao():
    """Criar arquivo de configuração para Hostinger"""
    
    config_content = """
# CONFIGURAÇÃO PARA HOSTINGER
# Copie estas configurações no painel do Hostinger

# Variáveis de Ambiente:
SECRET_KEY=sua_chave_secreta_muito_segura_123456789
GEMINI_API_KEY=AIzaSyBxEyDUMNA746H9kblcBCxtw8u8vDstvr8
OPENAI_API_KEY=sua_chave_openai_se_tiver
DATABASE_URL=sqlite:///agente_prod.db
FLASK_ENV=production
DEBUG=False

# Configurações do Python:
Versão: Python 3.8 ou superior
Arquivo de entrada: wsgi.py
Pasta: public_html

# Permissões necessárias:
uploads/ - 755 ou 777
static/ - 755
templates/ - 755

# Estrutura de arquivos esperada:
public_html/
├── wsgi.py
├── app.py
├── .htaccess
├── config_prod.py
├── requirements.txt
├── agente_*.py
├── config.py
├── database.py
├── integracoes.py
├── utils.py
├── templates/
├── static/
└── uploads/
"""
    
    with open('CONFIGURACAO_HOSTINGER.txt', 'w', encoding='utf-8') as f:
        f.write(config_content)
    
    print("✅ Arquivo de configuração criado: CONFIGURACAO_HOSTINGER.txt")

def criar_checklist_deploy():
    """Criar checklist de deploy"""
    
    checklist_content = """
# ✅ CHECKLIST DE DEPLOY NO HOSTINGER

## 📋 ANTES DO DEPLOY:
- [ ] Conta no Hostinger ativa
- [ ] Domínio configurado
- [ ] Arquivo agente_deploy.zip baixado

## 🚀 PROCESSO DE DEPLOY:

### 1. CONFIGURAR PYTHON:
- [ ] Acessar painel do Hostinger
- [ ] Ir para "Python" ou "Aplicações Python"
- [ ] Selecionar domínio
- [ ] Configurar versão Python 3.8+
- [ ] Definir arquivo de entrada: wsgi.py
- [ ] Salvar configurações

### 2. UPLOAD DOS ARQUIVOS:
- [ ] Ir para "Gerenciador de Arquivos"
- [ ] Navegar até public_html
- [ ] Fazer upload do agente_deploy.zip
- [ ] Extrair arquivo ZIP
- [ ] Verificar se todos os arquivos foram extraídos

### 3. CONFIGURAR VARIÁVEIS:
- [ ] Ir para "Variáveis de Ambiente"
- [ ] Adicionar SECRET_KEY
- [ ] Adicionar GEMINI_API_KEY
- [ ] Adicionar OPENAI_API_KEY
- [ ] Adicionar DATABASE_URL
- [ ] Salvar todas as variáveis

### 4. INSTALAR DEPENDÊNCIAS:
- [ ] Ir para "Terminal" ou "SSH"
- [ ] Executar: cd public_html
- [ ] Executar: pip install -r requirements.txt
- [ ] Aguardar instalação completa

### 5. CONFIGURAR PERMISSÕES:
- [ ] Selecionar pasta uploads/
- [ ] Definir permissão 755 ou 777
- [ ] Aplicar permissões

### 6. TESTAR APLICAÇÃO:
- [ ] Acessar https://seudominio.com
- [ ] Verificar se página carrega
- [ ] Testar chat de suporte
- [ ] Testar criação de conteúdo
- [ ] Testar upload de arquivos
- [ ] Verificar dashboard

## 🎯 RESULTADO ESPERADO:
- [ ] Página inicial carrega
- [ ] Todas as funcionalidades operacionais
- [ ] Interface responsiva
- [ ] Performance adequada

## 🆘 SE ALGO DER ERRADO:
- [ ] Verificar logs de erro
- [ ] Confirmar configurações Python
- [ ] Verificar variáveis de ambiente
- [ ] Testar permissões
- [ ] Contatar suporte Hostinger
"""
    
    with open('CHECKLIST_DEPLOY.txt', 'w', encoding='utf-8') as f:
        f.write(checklist_content)
    
    print("✅ Checklist de deploy criado: CHECKLIST_DEPLOY.txt")

def criar_comandos_ssh():
    """Criar arquivo com comandos SSH úteis"""
    
    comandos_content = """
# 🔧 COMANDOS SSH ÚTEIS PARA HOSTINGER

## 📁 NAVEGAÇÃO:
cd public_html                    # Ir para pasta da aplicação
ls -la                           # Listar arquivos
pwd                              # Mostrar diretório atual

## 🐍 PYTHON:
python3 --version                # Verificar versão Python
pip3 --version                   # Verificar versão pip
pip3 install -r requirements.txt # Instalar dependências

## 📊 VERIFICAR APLICAÇÃO:
python3 -c "import flask; print('Flask OK')"  # Testar Flask
python3 -c "from app import app; print('App OK')"  # Testar app

## 🔍 LOGS:
tail -f error.log                # Ver logs de erro
tail -f access.log               # Ver logs de acesso

## 🔐 PERMISSÕES:
chmod 755 uploads/               # Definir permissão uploads
chmod 644 *.py                   # Definir permissão arquivos Python
chmod 644 .htaccess              # Definir permissão .htaccess

## 🗂️ ESTRUTURA:
find . -name "*.py"              # Encontrar arquivos Python
find . -name "*.html"            # Encontrar templates
ls -la templates/                # Listar templates
ls -la static/                   # Listar arquivos estáticos

## 🧪 TESTE:
curl http://localhost:5000       # Testar aplicação localmente
curl -I https://seudominio.com   # Testar resposta HTTP

## 🔧 MANUTENÇÃO:
ps aux | grep python             # Ver processos Python
kill -9 PID                      # Matar processo (substitua PID)
"""
    
    with open('COMANDOS_SSH.txt', 'w', encoding='utf-8') as f:
        f.write(comandos_content)
    
    print("✅ Comandos SSH criados: COMANDOS_SSH.txt")

def verificar_arquivos_deploy():
    """Verificar se todos os arquivos necessários estão presentes"""
    
    print("🔍 Verificando arquivos de deploy...")
    
    arquivos_necessarios = [
        'agente_deploy.zip',
        'wsgi.py',
        '.htaccess',
        'config_prod.py',
        'requirements.txt'
    ]
    
    arquivos_faltando = []
    for arquivo in arquivos_necessarios:
        if not Path(arquivo).exists():
            arquivos_faltando.append(arquivo)
    
    if arquivos_faltando:
        print("❌ Arquivos faltando:")
        for arquivo in arquivos_faltando:
            print(f"   - {arquivo}")
        return False
    else:
        print("✅ Todos os arquivos de deploy estão presentes")
        return True

def criar_guia_rapido():
    """Criar guia rápido de deploy"""
    
    guia_content = """
# ⚡ GUIA RÁPIDO - DEPLOY NO HOSTINGER

## 🚀 EM 5 MINUTOS:

### 1. PYTHON:
- Painel → Python → Configurar
- Versão: 3.8+ | Entrada: wsgi.py

### 2. UPLOAD:
- Gerenciador → public_html
- Upload: agente_deploy.zip
- Extrair arquivo

### 3. VARIÁVEIS:
- Variáveis de Ambiente
- Adicionar: SECRET_KEY, GEMINI_API_KEY, DATABASE_URL

### 4. DEPENDÊNCIAS:
- Terminal → cd public_html
- pip install -r requirements.txt

### 5. TESTE:
- https://seudominio.com
- ✅ Funcionando!

## 🆘 PROBLEMAS COMUNS:

### Erro 500:
- Verificar Python configurado
- Confirmar wsgi.py como entrada
- Instalar dependências

### Erro 404:
- Extrair arquivos do ZIP
- Verificar .htaccess
- Confirmar estrutura

### Erro Import:
- pip install -r requirements.txt
- Python 3.8+
- Verificar imports

## 📞 SUPORTE:
- Chat Hostinger
- Ticket suporte
- Documentação
"""
    
    with open('GUIA_RAPIDO.txt', 'w', encoding='utf-8') as f:
        f.write(guia_content)
    
    print("✅ Guia rápido criado: GUIA_RAPIDO.txt")

def main():
    """Função principal"""
    print("🔧 CONFIGURANDO DEPLOY PARA HOSTINGER")
    print("="*50)
    
    # Verificar arquivos de deploy
    if not verificar_arquivos_deploy():
        print("\n❌ Execute primeiro: python deploy_hostinger.py")
        return
    
    # Criar arquivos de configuração
    criar_arquivo_configuracao()
    criar_checklist_deploy()
    criar_comandos_ssh()
    criar_guia_rapido()
    
    print("\n" + "="*50)
    print("✅ CONFIGURAÇÃO COMPLETA!")
    print("="*50)
    print("\n📁 Arquivos criados:")
    print("   - CONFIGURACAO_HOSTINGER.txt")
    print("   - CHECKLIST_DEPLOY.txt")
    print("   - COMANDOS_SSH.txt")
    print("   - GUIA_RAPIDO.txt")
    print("\n🚀 PRÓXIMOS PASSOS:")
    print("1. 📤 Faça upload do agente_deploy.zip para o Hostinger")
    print("2. ⚙️ Configure Python (versão 3.8+, entrada: wsgi.py)")
    print("3. 🔐 Adicione as variáveis de ambiente")
    print("4. 📦 Instale as dependências")
    print("5. 🌐 Teste em https://seudominio.com")
    print("\n📄 Consulte os arquivos criados para detalhes")
    print("\n🎉 Seu agente estará online em minutos!")

if __name__ == "__main__":
    main()
