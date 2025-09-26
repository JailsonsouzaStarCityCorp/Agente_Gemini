"""
Script para iniciar a interface web do Sistema de Agentes de IA
"""
import os
import sys
import subprocess
from pathlib import Path

def verificar_dependencias():
    """Verificar se as dependências estão instaladas"""
    try:
        import flask
        print("✅ Flask instalado")
        return True
    except ImportError:
        print("❌ Flask não encontrado")
        return False

def instalar_dependencias():
    """Instalar dependências necessárias"""
    print("📦 Instalando dependências...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def criar_diretorios():
    """Criar diretórios necessários"""
    diretorios = ['uploads', 'templates', 'static', 'static/css', 'static/js']
    
    for diretorio in diretorios:
        Path(diretorio).mkdir(exist_ok=True)
        print(f"📁 Diretório criado: {diretorio}")

def iniciar_servidor():
    """Iniciar o servidor web"""
    print("\n" + "="*60)
    print("🌐 INICIANDO INTERFACE WEB")
    print("="*60)
    print("📱 Acesse: http://localhost:5000")
    print("🔄 Para parar: Ctrl+C")
    print("="*60)
    
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"❌ Erro ao iniciar servidor: {e}")
        return False

def main():
    """Função principal"""
    print("🚀 SISTEMA DE AGENTES DE IA - INTERFACE WEB")
    print("="*50)
    
    # Verificar se estamos no diretório correto
    if not Path("app.py").exists():
        print("❌ Arquivo app.py não encontrado!")
        print("   Certifique-se de estar no diretório correto.")
        return
    
    # Criar diretórios necessários
    criar_diretorios()
    
    # Verificar dependências
    if not verificar_dependencias():
        print("\n📦 Instalando dependências...")
        if not instalar_dependencias():
            print("❌ Não foi possível instalar as dependências.")
            return
    
    # Iniciar servidor
    iniciar_servidor()

if __name__ == "__main__":
    main()
