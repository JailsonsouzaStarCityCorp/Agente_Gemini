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
