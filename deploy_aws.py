"""
Script para deploy automático na AWS
"""
import os
import shutil
import subprocess
from pathlib import Path

def criar_arquivos_aws():
    """Criar arquivos necessários para AWS"""
    
    print("☁️ Criando arquivos para deploy na AWS...")
    
    # Verificar se application.py existe
    if not Path('application.py').exists():
        print("❌ Arquivo application.py não encontrado!")
        return False
    
    # Verificar se .ebextensions existe
    if not Path('.ebextensions').exists():
        print("❌ Diretório .ebextensions não encontrado!")
        return False
    
    print("✅ Arquivos AWS verificados")
    return True

def criar_zip_aws():
    """Criar arquivo ZIP para AWS"""
    
    print("📦 Criando arquivo para AWS...")
    
    # Arquivos a incluir para AWS
    arquivos_incluir = [
        'application.py',
        'app.py',
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
        'uploads/',
        '.ebextensions/',
        'Dockerfile',
        '.dockerignore'
    ]
    
    # Criar diretório de deploy
    deploy_dir = Path('deploy_aws')
    if deploy_dir.exists():
        shutil.rmtree(deploy_dir)
    deploy_dir.mkdir(exist_ok=True)
    
    # Copiar arquivos
    for arquivo in arquivos_incluir:
        src = Path(arquivo)
        dst = deploy_dir / arquivo
        
        if src.is_dir():
            if src.exists():
                shutil.copytree(src, dst, dirs_exist_ok=True)
                print(f"📁 Copiado diretório: {arquivo}")
        elif src.exists():
            shutil.copy2(src, dst)
            print(f"📄 Copiado arquivo: {arquivo}")
        else:
            print(f"⚠️  Arquivo não encontrado: {arquivo}")
    
    # Criar ZIP
    zip_name = 'agente_aws_deploy'
    if Path(f'{zip_name}.zip').exists():
        os.remove(f'{zip_name}.zip')
    
    shutil.make_archive(zip_name, 'zip', deploy_dir)
    
    print(f"✅ Arquivo AWS criado: {zip_name}.zip")
    return True

def criar_comandos_aws():
    """Criar arquivo com comandos AWS"""
    
    comandos_content = """
# 🚀 COMANDOS PARA DEPLOY NA AWS

## 📋 PRÉ-REQUISITOS:
# 1. Instalar AWS CLI
pip install awscli

# 2. Configurar credenciais
aws configure
# AWS Access Key ID: [sua_access_key]
# AWS Secret Access Key: [sua_secret_key]
# Default region name: us-east-1
# Default output format: json

# 3. Instalar EB CLI
pip install awsebcli

## 🌟 MÉTODO 1: ELASTIC BEANSTALK (RECOMENDADO)

# Inicializar aplicação EB
eb init

# Criar ambiente
eb create production

# Deploy
eb deploy

# Abrir aplicação
eb open

# Ver logs
eb logs

# Configurar variáveis de ambiente
eb setenv GEMINI_API_KEY=sua_chave_gemini
eb setenv SECRET_KEY=sua_chave_secreta

## 🖥️ MÉTODO 2: EC2

# 1. Criar instância EC2
# 2. Conectar via SSH
ssh -i "sua-key.pem" ubuntu@ec2-xx-xx-xx-xx.compute-1.amazonaws.com

# 3. Instalar dependências
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv nginx -y

# 4. Configurar aplicação
sudo mkdir -p /var/www/agente
cd /var/www/agente
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 5. Configurar Gunicorn
pip install gunicorn
gunicorn --bind 0.0.0.0:5000 app:app

# 6. Configurar Nginx
sudo nano /etc/nginx/sites-available/agente
# Adicionar configuração do proxy

# 7. Configurar SSL
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d seu-dominio.com

## ⚡ MÉTODO 3: LAMBDA (SERVERLESS)

# 1. Instalar SAM CLI
pip install aws-sam-cli

# 2. Construir aplicação
sam build

# 3. Deploy
sam deploy --guided

# 4. Testar
sam local start-api

## 🐳 MÉTODO 4: DOCKER + ECR

# 1. Criar repositório ECR
aws ecr create-repository --repository-name agente-ia

# 2. Fazer login no ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com

# 3. Build da imagem
docker build -t agente-ia .

# 4. Tag da imagem
docker tag agente-ia:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/agente-ia:latest

# 5. Push para ECR
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/agente-ia:latest

## 🔧 COMANDOS ÚTEIS:

# Ver status da aplicação
eb status

# Ver logs em tempo real
eb logs --all

# Configurar variáveis de ambiente
eb setenv VARIAVEL=valor

# Abrir aplicação no navegador
eb open

# Terminar ambiente
eb terminate

# Listar ambientes
eb list

# Trocar de ambiente
eb use nome-do-ambiente
"""
    
    with open('COMANDOS_AWS.txt', 'w', encoding='utf-8') as f:
        f.write(comandos_content)
    
    print("✅ Comandos AWS criados: COMANDOS_AWS.txt")

def criar_guia_rapido_aws():
    """Criar guia rápido para AWS"""
    
    guia_content = """
# ⚡ GUIA RÁPIDO - DEPLOY NA AWS

## 🚀 ELASTIC BEANSTALK (MAIS FÁCIL):

### 1. PREPARAR:
pip install awscli awsebcli
aws configure

### 2. DEPLOY:
eb init
eb create production
eb deploy

### 3. CONFIGURAR:
eb setenv GEMINI_API_KEY=sua_chave
eb setenv SECRET_KEY=sua_chave_secreta

### 4. TESTAR:
eb open

## 🖥️ EC2 (MAIS CONTROLE):

### 1. CRIAR INSTÂNCIA:
- AWS Console → EC2
- Launch Instance
- Ubuntu 22.04 LTS
- t3.micro (gratuito)

### 2. CONFIGURAR:
ssh -i "key.pem" ubuntu@ec2-ip
sudo apt update && sudo apt install python3 python3-pip nginx -y

### 3. DEPLOY:
sudo mkdir -p /var/www/agente
cd /var/www/agente
# Upload arquivos
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 4. CONFIGURAR NGINX:
sudo nano /etc/nginx/sites-available/agente
# Configurar proxy para localhost:5000

## ⚡ LAMBDA (SERVERLESS):

### 1. INSTALAR SAM:
pip install aws-sam-cli

### 2. DEPLOY:
sam build
sam deploy --guided

## 🐳 DOCKER:

### 1. BUILD:
docker build -t agente-ia .

### 2. PUSH ECR:
aws ecr create-repository --repository-name agente-ia
docker tag agente-ia:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/agente-ia:latest
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/agente-ia:latest

## 💰 CUSTOS:
- EC2 t3.micro: ~$8.50/mês
- Elastic Beanstalk: ~$25/mês
- Lambda: ~$1-5/mês (por uso)

## 🆘 PROBLEMAS:
- Erro 500: Verificar logs (eb logs)
- Erro 404: Verificar configuração nginx
- Erro import: Verificar dependências
"""
    
    with open('GUIA_RAPIDO_AWS.txt', 'w', encoding='utf-8') as f:
        f.write(guia_content)
    
    print("✅ Guia rápido AWS criado: GUIA_RAPIDO_AWS.txt")

def criar_template_sam():
    """Criar template SAM para Lambda"""
    
    template_content = """
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
"""
    
    with open('template.yaml', 'w', encoding='utf-8') as f:
        f.write(template_content)
    
    print("✅ Template SAM criado: template.yaml")

def main():
    """Função principal"""
    print("☁️ PREPARANDO DEPLOY PARA AWS")
    print("="*50)
    
    # Verificar arquivos AWS
    if not criar_arquivos_aws():
        print("\n❌ Erro ao verificar arquivos AWS!")
        return
    
    # Criar ZIP para AWS
    if not criar_zip_aws():
        print("\n❌ Erro ao criar arquivo AWS!")
        return
    
    # Criar arquivos de ajuda
    criar_comandos_aws()
    criar_guia_rapido_aws()
    criar_template_sam()
    
    print("\n" + "="*50)
    print("✅ DEPLOY AWS PREPARADO!")
    print("="*50)
    print("\n📁 Arquivos criados:")
    print("   - agente_aws_deploy.zip")
    print("   - COMANDOS_AWS.txt")
    print("   - GUIA_RAPIDO_AWS.txt")
    print("   - template.yaml")
    print("\n🚀 MÉTODOS DISPONÍVEIS:")
    print("1. 🌟 Elastic Beanstalk (Recomendado)")
    print("2. 🖥️ EC2 (Mais controle)")
    print("3. ⚡ Lambda (Serverless)")
    print("4. 🐳 Docker + ECR")
    print("\n📄 Consulte os arquivos criados para detalhes")
    print("\n☁️ Seu agente estará rodando na AWS!")

if __name__ == "__main__":
    main()
