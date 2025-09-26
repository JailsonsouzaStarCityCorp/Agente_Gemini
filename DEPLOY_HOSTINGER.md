# 🌐 Como Hospedar seu Agente de IA no Hostinger

## 📋 **PRÉ-REQUISITOS**

### **✅ Conta no Hostinger:**
- Plano de hospedagem com suporte a Python
- Acesso ao painel de controle
- Domínio configurado

### **✅ Arquivos Necessários:**
- Todos os arquivos do seu agente
- Arquivos de configuração para produção
- Scripts de deploy

---

## 🚀 **MÉTODO 1: HOSPEDAGEM COMPARTILHADA (RECOMENDADO)**

### **1. Preparar Arquivos para Produção:**

#### **📁 Estrutura de Arquivos:**
```
public_html/
├── app.py                 # Aplicação principal
├── requirements.txt       # Dependências
├── wsgi.py               # Configuração WSGI
├── .htaccess             # Configurações Apache
├── config_prod.py        # Configurações de produção
├── agente_suporte.py     # Agente de suporte
├── agente_conteudo.py    # Agente de conteúdo
├── agente_vendas.py      # Agente de vendas
├── agente_automatizado.py # Agente automatizado
├── config.py             # Configurações
├── database.py           # Banco de dados
├── integracoes.py        # Integrações
├── utils.py              # Utilitários
├── templates/            # Templates HTML
├── static/               # Arquivos estáticos
└── uploads/              # Uploads
```

### **2. Criar Arquivos de Configuração:**

#### **📄 wsgi.py:**
```python
import sys
import os

# Adicionar o diretório atual ao path
sys.path.insert(0, os.path.dirname(__file__))

from app import app as application

if __name__ == "__main__":
    application.run()
```

#### **📄 .htaccess:**
```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ wsgi.py/$1 [QSA,L]

# Configurações de segurança
Header always set X-Content-Type-Options nosniff
Header always set X-Frame-Options DENY
Header always set X-XSS-Protection "1; mode=block"

# Cache para arquivos estáticos
<FilesMatch "\.(css|js|png|jpg|jpeg|gif|ico|svg)$">
    ExpiresActive On
    ExpiresDefault "access plus 1 month"
</FilesMatch>
```

#### **📄 config_prod.py:**
```python
"""
Configurações para produção no Hostinger
"""
import os

class ConfigProducao:
    # Configurações do Flask
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sua_chave_secreta_super_segura_aqui')
    DEBUG = False
    TESTING = False
    
    # Configurações de banco de dados
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///agente_prod.db')
    
    # Configurações de API
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
    
    # Configurações de upload
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    UPLOAD_FOLDER = 'uploads'
    
    # Configurações de segurança
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Configurações de CORS
    CORS_ORIGINS = ['https://seudominio.com']
```

### **3. Modificar app.py para Produção:**

#### **📄 app_prod.py:**
```python
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
from config_prod import ConfigProducao

# Importar os agentes
from agente_suporte import AgenteSuporte
from agente_conteudo import AgenteConteudo
from agente_vendas import AgenteAnaliseVendas
from agente_automatizado import AgenteAutomatizado
from database import db_manager
from integracoes import gerenciador_integracoes
from config import config

app = Flask(__name__)
app.config.from_object(ConfigProducao)

# Inicializar agentes
agente_suporte = AgenteSuporte()
agente_conteudo = AgenteConteudo()
agente_vendas = AgenteAnaliseVendas()
agente_automatizado = AgenteAutomatizado()

# Rotas (mesmo código das rotas originais)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suporte')
def suporte():
    return render_template('suporte.html')

@app.route('/conteudo')
def conteudo():
    return render_template('conteudo.html')

@app.route('/vendas')
def vendas():
    return render_template('vendas.html')

@app.route('/dashboard')
def dashboard():
    try:
        stats = db_manager.obter_estatisticas()
        return render_template('dashboard.html', stats=stats)
    except Exception as e:
        return render_template('dashboard.html', stats={}, error=str(e))

@app.route('/configuracao')
def configuracao():
    return render_template('configuracao.html')

# APIs (mesmo código das APIs originais)
@app.route('/api/suporte', methods=['POST'])
def api_suporte():
    # ... código da API de suporte ...
    pass

@app.route('/api/conteudo', methods=['POST'])
def api_conteudo():
    # ... código da API de conteúdo ...
    pass

@app.route('/api/vendas', methods=['POST'])
def api_vendas():
    # ... código da API de vendas ...
    pass

@app.route('/api/estatisticas')
def api_estatisticas():
    # ... código da API de estatísticas ...
    pass

@app.route('/api/integracoes/teste', methods=['POST'])
def api_testar_integracoes():
    # ... código da API de integrações ...
    pass

@app.route('/api/configuracao', methods=['GET', 'POST'])
def api_configuracao():
    # ... código da API de configuração ...
    pass

if __name__ == '__main__':
    # Criar diretórios necessários
    Path('uploads').mkdir(exist_ok=True)
    Path('templates').mkdir(exist_ok=True)
    Path('static').mkdir(exist_ok=True)
    Path('static/css').mkdir(exist_ok=True)
    Path('static/js').mkdir(exist_ok=True)
    
    app.run(debug=False, host='0.0.0.0', port=5000)
```

---

## 🔧 **MÉTODO 2: VPS (MAIS AVANÇADO)**

### **1. Configurar VPS no Hostinger:**

#### **📋 Passos:**
1. **Contratar VPS** no Hostinger
2. **Configurar SSH** para acesso
3. **Instalar Python** e dependências
4. **Configurar Nginx** como proxy reverso
5. **Configurar SSL** com Let's Encrypt

#### **📄 setup_vps.sh:**
```bash
#!/bin/bash

# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python e dependências
sudo apt install python3 python3-pip python3-venv nginx -y

# Criar usuário para aplicação
sudo useradd -m -s /bin/bash agente
sudo usermod -aG sudo agente

# Criar diretório da aplicação
sudo mkdir -p /var/www/agente
sudo chown agente:agente /var/www/agente

# Configurar Nginx
sudo tee /etc/nginx/sites-available/agente << EOF
server {
    listen 80;
    server_name seudominio.com www.seudominio.com;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
    
    location /static {
        alias /var/www/agente/static;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
EOF

# Ativar site
sudo ln -s /etc/nginx/sites-available/agente /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# Configurar SSL
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d seudominio.com -d www.seudominio.com

echo "VPS configurado com sucesso!"
```

#### **📄 systemd_service.service:**
```ini
[Unit]
Description=Agente de IA Flask App
After=network.target

[Service]
User=agente
Group=agente
WorkingDirectory=/var/www/agente
Environment=PATH=/var/www/agente/venv/bin
ExecStart=/var/www/agente/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:5000 wsgi:application
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## 📦 **SCRIPT DE DEPLOY AUTOMÁTICO**

### **📄 deploy_hostinger.py:**
```python
"""
Script para deploy automático no Hostinger
"""
import os
import shutil
import subprocess
from pathlib import Path

def criar_arquivos_producao():
    """Criar arquivos necessários para produção"""
    
    # Criar wsgi.py
    wsgi_content = '''import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from app import app as application

if __name__ == "__main__":
    application.run()
'''
    
    with open('wsgi.py', 'w', encoding='utf-8') as f:
        f.write(wsgi_content)
    
    # Criar .htaccess
    htaccess_content = '''RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ wsgi.py/$1 [QSA,L]

Header always set X-Content-Type-Options nosniff
Header always set X-Frame-Options DENY
Header always set X-XSS-Protection "1; mode=block"

<FilesMatch "\\.(css|js|png|jpg|jpeg|gif|ico|svg)$">
    ExpiresActive On
    ExpiresDefault "access plus 1 month"
</FilesMatch>
'''
    
    with open('.htaccess', 'w', encoding='utf-8') as f:
        f.write(htaccess_content)
    
    # Criar config_prod.py
    config_prod_content = '''import os

class ConfigProducao:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sua_chave_secreta_super_segura_aqui')
    DEBUG = False
    TESTING = False
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///agente_prod.db')
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = 'uploads'
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
'''
    
    with open('config_prod.py', 'w', encoding='utf-8') as f:
        f.write(config_prod_content)
    
    print("✅ Arquivos de produção criados")

def criar_zip_deploy():
    """Criar arquivo ZIP para upload"""
    
    # Arquivos a incluir
    arquivos_incluir = [
        'app.py',
        'wsgi.py',
        '.htaccess',
        'config_prod.py',
        'requirements.txt',
        'agente_suporte.py',
        'agente_conteudo.py',
        'agente_vendas.py',
        'agente_automatizado.py',
        'config.py',
        'database.py',
        'integracoes.py',
        'utils.py',
        'templates/',
        'static/',
        'uploads/'
    ]
    
    # Criar diretório de deploy
    deploy_dir = Path('deploy')
    deploy_dir.mkdir(exist_ok=True)
    
    # Copiar arquivos
    for arquivo in arquivos_incluir:
        src = Path(arquivo)
        dst = deploy_dir / arquivo
        
        if src.is_dir():
            shutil.copytree(src, dst, dirs_exist_ok=True)
        elif src.exists():
            shutil.copy2(src, dst)
    
    # Criar ZIP
    shutil.make_archive('agente_deploy', 'zip', deploy_dir)
    
    print("✅ Arquivo de deploy criado: agente_deploy.zip")
    print("📤 Faça upload deste arquivo para o Hostinger")

def main():
    """Função principal"""
    print("🚀 PREPARANDO DEPLOY PARA HOSTINGER")
    print("="*50)
    
    criar_arquivos_producao()
    criar_zip_deploy()
    
    print("\n📋 PRÓXIMOS PASSOS:")
    print("1. Faça upload do arquivo 'agente_deploy.zip' para o Hostinger")
    print("2. Extraia o arquivo na pasta public_html")
    print("3. Configure as variáveis de ambiente no painel do Hostinger")
    print("4. Acesse seu domínio para testar")

if __name__ == "__main__":
    main()
```

---

## 🔐 **CONFIGURAÇÃO DE SEGURANÇA**

### **📄 .env (Variáveis de Ambiente):**
```bash
# Configurações de produção
SECRET_KEY=sua_chave_secreta_super_segura_aqui
DEBUG=False
DATABASE_URL=sqlite:///agente_prod.db

# APIs
GEMINI_API_KEY=sua_chave_gemini_aqui
OPENAI_API_KEY=sua_chave_openai_aqui

# Integrações
EMAIL_SMTP=seu_smtp_aqui
WHATSAPP_TOKEN=seu_token_whatsapp_aqui
TELEGRAM_BOT=seu_bot_telegram_aqui
```

### **📄 security.py:**
```python
"""
Configurações de segurança para produção
"""
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def configurar_seguranca(app):
    """Configurar medidas de segurança"""
    
    # Rate limiting
    limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=["200 per day", "50 per hour"]
    )
    
    # Headers de segurança
    @app.after_request
    def after_request(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response
    
    return limiter
```

---

## 📋 **CHECKLIST DE DEPLOY**

### **✅ Antes do Deploy:**
- [ ] Testar aplicação localmente
- [ ] Verificar todas as dependências
- [ ] Configurar variáveis de ambiente
- [ ] Otimizar arquivos estáticos
- [ ] Configurar banco de dados

### **✅ Durante o Deploy:**
- [ ] Fazer upload dos arquivos
- [ ] Configurar .htaccess
- [ ] Configurar wsgi.py
- [ ] Testar aplicação
- [ ] Configurar SSL

### **✅ Após o Deploy:**
- [ ] Testar todas as funcionalidades
- [ ] Verificar logs de erro
- [ ] Configurar backup automático
- [ ] Monitorar performance
- [ ] Configurar domínio

---

## 🚀 **EXECUTAR DEPLOY**

### **1. Preparar Arquivos:**
```powershell
cd "c:\Users\DJ City\Documents\agente gemini"
python deploy_hostinger.py
```

### **2. Upload para Hostinger:**
1. Acesse o painel do Hostinger
2. Vá para "Gerenciador de Arquivos"
3. Navegue até a pasta `public_html`
4. Faça upload do arquivo `agente_deploy.zip`
5. Extraia o arquivo

### **3. Configurar Variáveis:**
1. No painel do Hostinger, vá para "Variáveis de Ambiente"
2. Adicione as variáveis do arquivo `.env`
3. Salve as configurações

### **4. Testar:**
1. Acesse seu domínio
2. Teste todas as funcionalidades
3. Verifique se está funcionando

---

## 🎯 **RESULTADO FINAL**

**✅ Seu agente de IA estará online e acessível via web!**

**🌐 URL:** https://seudominio.com

**🎉 Funcionalidades disponíveis:**
- Chat com IA
- Criação de conteúdo
- Análise de vendas
- Dashboard
- Configurações

---

*Deploy desenvolvido com ❤️ para máxima compatibilidade com Hostinger*
