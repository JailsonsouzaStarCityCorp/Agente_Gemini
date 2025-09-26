"""
Script de instalação e configuração do Sistema de Agentes de IA
"""
import os
import sys
import subprocess
from pathlib import Path

def instalar_dependencias():
    """Instala as dependências necessárias"""
    print("📦 Instalando dependências...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def criar_diretorios():
    """Cria os diretórios necessários"""
    print("📁 Criando diretórios...")
    diretorios = ['data', 'reports', 'logs']
    
    for diretorio in diretorios:
        Path(diretorio).mkdir(exist_ok=True)
        print(f"✅ Diretório '{diretorio}' criado")
    
    return True

def configurar_api_key():
    """Configura a API key do Gemini"""
    print("\n🔑 Configuração da API Key do Gemini")
    print("-" * 40)
    print("Para usar o sistema, você precisa de uma API key do Google Gemini.")
    print("1. Acesse: https://makersuite.google.com/app/apikey")
    print("2. Crie uma nova API key")
    print("3. Cole a chave abaixo")
    
    api_key = input("\nDigite sua API key (ou pressione Enter para pular): ").strip()
    
    if api_key:
        # Atualizar o arquivo config.py
        try:
            with open('config.py', 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            conteudo = conteudo.replace('AIzaSyBxEyDUMNA746H9kblcBCxtw8u8vDstvr8', api_key)
            
            with open('config.py', 'w', encoding='utf-8') as f:
                f.write(conteudo)
            
            print("✅ API key configurada com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao configurar API key: {e}")
            return False
    else:
        print("⚠️  API key não configurada. Você pode configurar depois editando config.py")
        return True

def testar_instalacao():
    """Testa se a instalação foi bem-sucedida"""
    print("\n🧪 Testando instalação...")
    try:
        # Testar imports
        import google.generativeai as genai
        import pandas as pd
        import schedule
        
        print("✅ Todas as dependências importadas com sucesso!")
        
        # Testar estrutura de arquivos
        arquivos_necessarios = [
            'main.py', 'config.py', 'utils.py',
            'agente_vendas.py', 'agente_suporte.py',
            'agente_conteudo.py', 'agente_automatizado.py'
        ]
        
        for arquivo in arquivos_necessarios:
            if not Path(arquivo).exists():
                print(f"❌ Arquivo '{arquivo}' não encontrado!")
                return False
        
        print("✅ Todos os arquivos necessários estão presentes!")
        return True
        
    except ImportError as e:
        print(f"❌ Erro ao importar dependências: {e}")
        return False

def main():
    """Função principal de instalação"""
    print("🚀 INSTALAÇÃO DO SISTEMA DE AGENTES DE IA")
    print("=" * 50)
    
    # Verificar Python
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 ou superior é necessário!")
        return False
    
    print(f"✅ Python {sys.version} detectado")
    
    # Instalar dependências
    if not instalar_dependencias():
        return False
    
    # Criar diretórios
    if not criar_diretorios():
        return False
    
    # Configurar API key
    configurar_api_key()
    
    # Testar instalação
    if testar_instalacao():
        print("\n🎉 INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
        print("=" * 50)
        print("Para usar o sistema:")
        print("1. Execute: python main.py")
        print("2. Ou execute: python exemplo_uso.py")
        print("\n📚 Consulte o README.md para mais informações")
        return True
    else:
        print("\n❌ INSTALAÇÃO FALHOU!")
        print("Verifique os erros acima e tente novamente")
        return False

if __name__ == "__main__":
    sucesso = main()
    input("\nPressione Enter para sair...")
    sys.exit(0 if sucesso else 1)
