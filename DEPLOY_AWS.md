# ☁️ Como Hospedar seu Agente de IA na AWS

## 🎯 **OPÇÕES DE HOSPEDAGEM NA AWS**

### **🚀 Métodos Recomendados:**
1. **AWS Elastic Beanstalk** (Mais fácil - Recomendado)
2. **AWS EC2** (Mais controle)
3. **AWS Lambda + API Gateway** (Serverless)
4. **AWS App Runner** (Containerizado)

---

## 🌟 **MÉTODO 1: AWS ELASTIC BEANSTALK (RECOMENDADO)**

### **✅ Vantagens:**
- **Fácil deploy** automático
- **Escalabilidade** automática
- **Monitoramento** integrado
- **Load balancer** incluído
- **SSL** automático

### **📋 Pré-requisitos:**
- ✅ Conta AWS
- ✅ AWS CLI instalado
- ✅ EB CLI instalado

---

## 🚀 **DEPLOY NO ELASTIC BEANSTALK**

### **PASSO 1: Preparar Arquivos**

#### **📄 Criar requirements.txt:**
```txt
Flask==2.3.3
Werkzeug==2.3.7
google-generativeai>=0.3.0
pandas>=1.5.0
openpyxl>=3.0.0
schedule>=1.2.0
requests>=2.28.0
gunicorn>=21.2.0
```

#### **📄 Criar application.py:**
```python
"""
Aplicação principal para AWS Elastic Beanstalk
"""
from app import app as application

if __name__ == "__main__":
    application.run()
```

#### **📄 Criar .ebextensions/01_packages.config:**
```yaml
packages:
  yum:
    python3-devel: []
    gcc: []
    gcc-c++: []
```

#### **📄 Criar .ebextensions/02_python.config:**
```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: application.py
  aws:elasticbeanstalk:application:environment:
    PYTHONPATH: "/var/app/current:$PYTHONPATH"
```

### **PASSO 2: Configurar AWS CLI**

```bash
# Instalar AWS CLI
pip install awscli

# Configurar credenciais
aws configure
# AWS Access Key ID: [sua_access_key]
# AWS Secret Access Key: [sua_secret_key]
# Default region name: us-east-1
# Default output format: json
```

### **PASSO 3: Instalar EB CLI**

```bash
# Windows
pip install awsebcli

# Linux/Mac
pip install awsebcli
```

### **PASSO 4: Deploy**

```bash
# Inicializar aplicação EB
eb init

# Criar ambiente
eb create production

# Deploy
eb deploy

# Abrir aplicação
eb open
```

---

## 🔧 **MÉTODO 2: AWS EC2 (MAIS CONTROLE)**

### **✅ Vantagens:**
- **Controle total** do servidor
- **Customização** completa
- **Custo** mais baixo para uso constante

### **📋 Pré-requisitos:**
- ✅ Conta AWS
- ✅ Key pair criado
- ✅ Security group configurado

---

## 🖥️ **DEPLOY NO EC2**

### **PASSO 1: Criar Instância EC2**

1. **Acesse:** AWS Console → EC2
2. **Clique:** "Launch Instance"
3. **Configure:**
   - **AMI:** Ubuntu Server 22.04 LTS
   - **Instance Type:** t3.micro (gratuito)
   - **Key Pair:** Selecione ou crie
   - **Security Group:** Configure portas 22 (SSH) e 80 (HTTP)

### **PASSO 2: Conectar via SSH**

```bash
# Conectar à instância
ssh -i "sua-key.pem" ubuntu@ec2-xx-xx-xx-xx.compute-1.amazonaws.com

# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python e dependências
sudo apt install python3 python3-pip python3-venv nginx -y

# Instalar Node.js (para build tools)
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### **PASSO 3: Configurar Aplicação**

```bash
# Criar usuário para aplicação
sudo useradd -m -s /bin/bash agente
sudo usermod -aG sudo agente

# Criar diretório da aplicação
sudo mkdir -p /var/www/agente
sudo chown agente:agente /var/www/agente

# Mudar para usuário agente
sudo su - agente

# Clonar ou fazer upload dos arquivos
cd /var/www/agente
# Fazer upload dos arquivos via SCP ou git clone
```

### **PASSO 4: Configurar Virtual Environment**

```bash
# Criar virtual environment
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Testar aplicação
python app.py
```

### **PASSO 5: Configurar Gunicorn**

```bash
# Instalar Gunicorn
pip install gunicorn

# Criar arquivo de configuração
cat > gunicorn.conf.py << EOF
bind = "127.0.0.1:5000"
workers = 3
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 100
preload_app = True
EOF

# Testar Gunicorn
gunicorn --config gunicorn.conf.py app:app
```

### **PASSO 6: Configurar Systemd Service**

```bash
# Criar arquivo de serviço
sudo tee /etc/systemd/system/agente.service << EOF
[Unit]
Description=Agente de IA Flask App
After=network.target

[Service]
User=agente
Group=agente
WorkingDirectory=/var/www/agente
Environment=PATH=/var/www/agente/venv/bin
ExecStart=/var/www/agente/venv/bin/gunicorn --config gunicorn.conf.py app:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Habilitar e iniciar serviço
sudo systemctl daemon-reload
sudo systemctl enable agente
sudo systemctl start agente
sudo systemctl status agente
```

### **PASSO 7: Configurar Nginx**

```bash
# Criar configuração do Nginx
sudo tee /etc/nginx/sites-available/agente << EOF
server {
    listen 80;
    server_name _;
    
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
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
```

### **PASSO 8: Configurar SSL com Let's Encrypt**

```bash
# Instalar Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obter certificado SSL
sudo certbot --nginx -d seu-dominio.com

# Configurar renovação automática
sudo crontab -e
# Adicionar linha:
# 0 12 * * * /usr/bin/certbot renew --quiet
```

---

## ⚡ **MÉTODO 3: AWS LAMBDA + API GATEWAY (SERVERLESS)**

### **✅ Vantagens:**
- **Sem servidor** para gerenciar
- **Pagamento** por uso
- **Escalabilidade** automática

### **📋 Pré-requisitos:**
- ✅ Conta AWS
- ✅ AWS SAM CLI instalado

---

## 🔄 **DEPLOY SERVERLESS**

### **PASSO 1: Criar template SAM**

#### **📄 template.yaml:**
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: Agente de IA Serverless

Globals:
  Function:
    Timeout: 30
    Runtime: python3.9
    Environment:
      Variables:
        GEMINI_API_KEY: !Ref GeminiApiKey
        SECRET_KEY: !Ref SecretKey

Parameters:
  GeminiApiKey:
    Type: String
    Description: Gemini API Key
    NoEcho: true
  SecretKey:
    Type: String
    Description: Secret Key for Flask
    NoEcho: true

Resources:
  AgenteFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: src/
      Handler: app.lambda_handler
      Events:
        Api:
          Type: Api
          Properties:
            Path: /{proxy+}
            Method: ANY
        RootApi:
          Type: Api
          Properties:
            Path: /
            Method: ANY

Outputs:
  AgenteApi:
    Description: "API Gateway endpoint URL"
    Value: !Sub "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/"
```

### **PASSO 2: Modificar app.py para Lambda**

#### **📄 src/app.py:**
```python
"""
Aplicação Flask para AWS Lambda
"""
from flask import Flask, render_template, request, jsonify
import json
import sys
import os
from datetime import datetime

# Adicionar o diretório atual ao path
sys.path.append('.')

# Importar os agentes
from agente_suporte import AgenteSuporte
from agente_conteudo import AgenteConteudo
from agente_vendas import AgenteAnaliseVendas
from config import config

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'agente_ia_secret_key_2024')

# Inicializar agentes
agente_suporte = AgenteSuporte()
agente_conteudo = AgenteConteudo()
agente_vendas = AgenteAnaliseVendas()

# Rotas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/suporte', methods=['POST'])
def api_suporte():
    # ... código da API ...
    pass

# Handler para Lambda
def lambda_handler(event, context):
    from awsgi import response
    return response(app, event, context, base64_content_types={"image/png"})
```

### **PASSO 3: Deploy com SAM**

```bash
# Construir aplicação
sam build

# Deploy
sam deploy --guided

# Testar
sam local start-api
```

---

## 🐳 **MÉTODO 4: AWS APP RUNNER (CONTAINERIZADO)**

### **✅ Vantagens:**
- **Deploy simples** via Docker
- **Escalabilidade** automática
- **Integração** com ECR

---

## 📦 **DEPLOY COM DOCKER**

### **PASSO 1: Criar Dockerfile**

#### **📄 Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Criar diretórios necessários
RUN mkdir -p uploads static/css static/js templates

# Expor porta
EXPOSE 8000

# Comando para executar
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "app:app"]
```

### **PASSO 2: Criar .dockerignore**

```dockerignore
__pycache__
*.pyc
*.pyo
*.pyd
.Python
env
pip-log.txt
pip-delete-this-directory.txt
.tox
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.git
.mypy_cache
.pytest_cache
.hypothesis

.DS_Store
.vscode
.idea
*.swp
*.swo

deploy/
*.zip
```

### **PASSO 3: Build e Push para ECR**

```bash
# Criar repositório ECR
aws ecr create-repository --repository-name agente-ia

# Fazer login no ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com

# Build da imagem
docker build -t agente-ia .

# Tag da imagem
docker tag agente-ia:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/agente-ia:latest

# Push para ECR
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/agente-ia:latest
```

### **PASSO 4: Criar App Runner Service**

```bash
# Criar arquivo de configuração
cat > apprunner.yaml << EOF
version: 1.0
runtime: docker
build:
  commands:
    build:
      - echo "Build completed on `date`"
run:
  runtime-version: latest
  command: gunicorn --bind 0.0.0.0:8000 --workers 3 app:app
  network:
    port: 8000
  env:
    - name: GEMINI_API_KEY
      value: "sua-chave-gemini"
    - name: SECRET_KEY
      value: "sua-chave-secreta"
EOF
```

---

## 🔧 **CONFIGURAÇÕES DE SEGURANÇA**

### **📄 Security Groups:**
```json
{
  "SecurityGroupRules": [
    {
      "IpProtocol": "tcp",
      "FromPort": 22,
      "ToPort": 22,
      "CidrIp": "0.0.0.0/0",
      "Description": "SSH"
    },
    {
      "IpProtocol": "tcp",
      "FromPort": 80,
      "ToPort": 80,
      "CidrIp": "0.0.0.0/0",
      "Description": "HTTP"
    },
    {
      "IpProtocol": "tcp",
      "FromPort": 443,
      "ToPort": 443,
      "CidrIp": "0.0.0.0/0",
      "Description": "HTTPS"
    }
  ]
}
```

### **📄 IAM Policy:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    }
  ]
}
```

---

## 💰 **ESTIMATIVA DE CUSTOS**

### **📊 Elastic Beanstalk (t3.micro):**
- **EC2:** ~$8.50/mês
- **Load Balancer:** ~$16.20/mês
- **Storage:** ~$1/mês
- **Total:** ~$25.70/mês

### **📊 EC2 (t3.micro):**
- **EC2:** ~$8.50/mês
- **Storage:** ~$1/mês
- **Data Transfer:** ~$1/mês
- **Total:** ~$10.50/mês

### **📊 Lambda:**
- **Requests:** ~$0.20/1M requests
- **Compute:** ~$0.0000166667/GB-second
- **Total:** ~$1-5/mês (dependendo do uso)

---

## 🚀 **RECOMENDAÇÃO**

### **🥇 Para Iniciantes:**
**AWS Elastic Beanstalk** - Mais fácil de configurar e gerenciar

### **🥈 Para Controle Total:**
**AWS EC2** - Mais flexibilidade e controle

### **🥉 Para Serverless:**
**AWS Lambda + API Gateway** - Pagamento por uso

---

## 📋 **CHECKLIST DE DEPLOY**

### **✅ Antes do Deploy:**
- [ ] Conta AWS configurada
- [ ] AWS CLI instalado e configurado
- [ ] Arquivos de aplicação preparados
- [ ] Variáveis de ambiente definidas

### **✅ Durante o Deploy:**
- [ ] Recursos AWS criados
- [ ] Aplicação deployada
- [ ] Configurações aplicadas
- [ ] Testes realizados

### **✅ Após o Deploy:**
- [ ] Aplicação acessível
- [ ] SSL configurado
- [ ] Monitoramento ativo
- [ ] Backup configurado

---

**🎉 Seu agente de IA estará rodando na AWS com alta disponibilidade e escalabilidade!**

**☁️ Escolha o método que melhor se adapta às suas necessidades!**
