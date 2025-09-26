"""
Sistema Avançado de Configurações do Agente de IA
"""
import os
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

class ConfiguracaoAgente:
    """Classe central de configurações do agente"""
    
    def __init__(self):
        self.carregar_configuracoes()
    
    def carregar_configuracoes(self):
        """Carrega todas as configurações do sistema"""
        
        # ===== CONFIGURAÇÕES DE API =====
        self.API_CONFIG = {
            'gemini': {
                'api_key': os.getenv('GEMINI_API_KEY', 'AIzaSyBxEyDUMNA746H9kblcBCxtw8u8vDstvr8'),
                'model': 'gemini-1.5-flash',
                'temperature': 0.7,
                'max_tokens': 2048,
                'timeout': 30
            },
            'openai': {
                'api_key': os.getenv('OPENAI_API_KEY', ''),
                'model': 'gpt-4',
                'temperature': 0.7,
                'max_tokens': 2048
            },
            'claude': {
                'api_key': os.getenv('CLAUDE_API_KEY', ''),
                'model': 'claude-3-sonnet-20240229',
                'temperature': 0.7,
                'max_tokens': 2048
            }
        }
        
        # ===== CONFIGURAÇÕES DE INTEGRAÇÃO =====
        self.INTEGRACOES = {
            'email': {
                'smtp_server': os.getenv('SMTP_SERVER', 'smtp.gmail.com'),
                'smtp_port': int(os.getenv('SMTP_PORT', '587')),
                'email_usuario': os.getenv('EMAIL_USUARIO', ''),
                'email_senha': os.getenv('EMAIL_SENHA', ''),
                'email_remetente': os.getenv('EMAIL_REMETENTE', ''),
                'habilitado': True
            },
            'whatsapp': {
                'api_key': os.getenv('WHATSAPP_API_KEY', ''),
                'numero_telefone': os.getenv('WHATSAPP_NUMERO', ''),
                'webhook_url': os.getenv('WHATSAPP_WEBHOOK', ''),
                'habilitado': False
            },
            'telegram': {
                'bot_token': os.getenv('TELEGRAM_BOT_TOKEN', ''),
                'chat_id': os.getenv('TELEGRAM_CHAT_ID', ''),
                'habilitado': False
            },
            'slack': {
                'webhook_url': os.getenv('SLACK_WEBHOOK', ''),
                'bot_token': os.getenv('SLACK_BOT_TOKEN', ''),
                'canal': os.getenv('SLACK_CANAL', '#geral'),
                'habilitado': False
            },
            'discord': {
                'webhook_url': os.getenv('DISCORD_WEBHOOK', ''),
                'bot_token': os.getenv('DISCORD_BOT_TOKEN', ''),
                'canal_id': os.getenv('DISCORD_CANAL_ID', ''),
                'habilitado': False
            },
            'teams': {
                'webhook_url': os.getenv('TEAMS_WEBHOOK', ''),
                'habilitado': False
            }
        }
        
        # ===== CONFIGURAÇÕES DE BANCO DE DADOS =====
        self.DATABASE_CONFIG = {
            'sqlite': {
                'arquivo': 'data/agente.db',
                'habilitado': True
            },
            'postgresql': {
                'host': os.getenv('DB_HOST', 'localhost'),
                'port': int(os.getenv('DB_PORT', '5432')),
                'database': os.getenv('DB_NAME', 'agente'),
                'usuario': os.getenv('DB_USER', ''),
                'senha': os.getenv('DB_PASSWORD', ''),
                'habilitado': False
            },
            'mysql': {
                'host': os.getenv('MYSQL_HOST', 'localhost'),
                'port': int(os.getenv('MYSQL_PORT', '3306')),
                'database': os.getenv('MYSQL_DB', 'agente'),
                'usuario': os.getenv('MYSQL_USER', ''),
                'senha': os.getenv('MYSQL_PASSWORD', ''),
                'habilitado': False
            },
            'mongodb': {
                'uri': os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'),
                'database': os.getenv('MONGODB_DB', 'agente'),
                'habilitado': False
            }
        }
        
        # ===== CONFIGURAÇÕES DE ARQUIVOS E PASTAS =====
        self.DIRETORIOS = {
            'data': Path('data'),
            'reports': Path('reports'),
            'logs': Path('logs'),
            'uploads': Path('uploads'),
            'downloads': Path('downloads'),
            'templates': Path('templates'),
            'backups': Path('backups'),
            'cache': Path('cache')
        }
        
        # Criar diretórios se não existirem
        for nome, diretorio in self.DIRETORIOS.items():
            diretorio.mkdir(exist_ok=True)
        
        # ===== CONFIGURAÇÕES DE LOGGING =====
        self.LOGGING_CONFIG = {
            'level': os.getenv('LOG_LEVEL', 'INFO'),
            'file': 'logs/agente.log',
            'max_size': 10 * 1024 * 1024,  # 10MB
            'backup_count': 5,
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'handlers': ['file', 'console', 'email'],
            'email_alerts': {
                'habilitado': False,
                'destinatarios': [],
                'nivel_critico': 'ERROR'
            }
        }
        
        # ===== CONFIGURAÇÕES DE AGENDAMENTO =====
        self.SCHEDULE_CONFIG = {
            'horarios_execucao': [9, 15, 21],
            'timezone': 'America/Sao_Paulo',
            'retry_attempts': 3,
            'retry_delay': 300,  # 5 minutos
            'max_concurrent_jobs': 5,
            'habilitado': True
        }
        
        # ===== CONFIGURAÇÕES DE SEGURANÇA =====
        self.SECURITY_CONFIG = {
            'api_rate_limit': 100,  # requests por hora
            'max_file_size': 50 * 1024 * 1024,  # 50MB
            'allowed_extensions': ['.xlsx', '.csv', '.json', '.txt', '.pdf'],
            'encryption_key': os.getenv('ENCRYPTION_KEY', ''),
            'session_timeout': 3600,  # 1 hora
            'backup_retention_days': 30
        }
        
        # ===== CONFIGURAÇÕES DE PERFORMANCE =====
        self.PERFORMANCE_CONFIG = {
            'max_workers': 4,
            'cache_size': 1000,
            'cache_ttl': 3600,  # 1 hora
            'memory_limit': 512 * 1024 * 1024,  # 512MB
            'timeout_requests': 30,
            'habilitar_cache': True
        }
        
        # ===== CONFIGURAÇÕES ESPECÍFICAS POR AGENTE =====
        self.AGENTE_CONFIG = {
            'vendas': {
                'colunas_obrigatorias': ['data', 'valor_venda'],
                'formato_data': '%Y-%m-%d',
                'analise_automatica': True,
                'gerar_graficos': True,
                'tendencias_dias': 30
            },
            'suporte': {
                'urgencia_padrao': 'MÉDIA',
                'tempo_resposta_esperado': 30,
                'base_conhecimento_auto': True,
                'escalonamento_automatico': True,
                'idiomas_suportados': ['pt', 'en', 'es']
            },
            'conteudo': {
                'tamanho_max_post': 2200,
                'tamanho_max_newsletter': 500,
                'hashtags_max': 5,
                'templates_personalizados': True,
                'analise_sentimento': True
            },
            'automatizado': {
                'monitoramento_pastas': True,
                'processamento_paralelo': True,
                'notificacoes_erro': True,
                'backup_automatico': True
            }
        }
        
        # ===== CONFIGURAÇÕES DE NOTIFICAÇÕES =====
        self.NOTIFICACOES = {
            'email': {
                'relatorios_diarios': True,
                'alertas_erro': True,
                'resumos_semanais': True
            },
            'webhook': {
                'url': os.getenv('WEBHOOK_URL', ''),
                'eventos': ['erro', 'sucesso', 'conclusao'],
                'habilitado': False
            },
            'push': {
                'fcm_server_key': os.getenv('FCM_SERVER_KEY', ''),
                'habilitado': False
            }
        }
        
        # ===== CONFIGURAÇÕES DE ANÁLISE =====
        self.ANALISE_CONFIG = {
            'sentimento': {
                'habilitado': True,
                'modelo': 'portuguese',
                'confianca_minima': 0.7
            },
            'classificacao': {
                'habilitado': True,
                'categorias': ['vendas', 'suporte', 'marketing', 'financeiro'],
                'auto_classificar': True
            },
            'metricas': {
                'coleta_automatica': True,
                'intervalo_coleta': 3600,  # 1 hora
                'retencao_dados': 90  # dias
            }
        }
    
    def salvar_configuracao(self, secao: str, config: Dict[str, Any]):
        """Salva configuração em arquivo JSON"""
        arquivo_config = f"config_{secao}.json"
        with open(arquivo_config, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
    
    def carregar_configuracao(self, secao: str) -> Dict[str, Any]:
        """Carrega configuração de arquivo JSON"""
        arquivo_config = f"config_{secao}.json"
        if Path(arquivo_config).exists():
            with open(arquivo_config, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def obter_configuracao(self, secao: str, chave: str = None):
        """Obtém configuração específica"""
        config = getattr(self, secao.upper() + '_CONFIG', {})
        if chave:
            return config.get(chave)
        return config
    
    def atualizar_configuracao(self, secao: str, chave: str, valor: Any):
        """Atualiza configuração específica"""
        config = getattr(self, secao.upper() + '_CONFIG', {})
        config[chave] = valor
        setattr(self, secao.upper() + '_CONFIG', config)
        self.salvar_configuracao(secao, config)

# Instância global de configuração
config = ConfiguracaoAgente()

# Variáveis de compatibilidade (para não quebrar código existente)
GEMINI_API_KEY = config.API_CONFIG['gemini']['api_key']
GEMINI_MODEL = config.API_CONFIG['gemini']['model']
LOG_LEVEL = config.LOGGING_CONFIG['level']
LOG_FILE = config.LOGGING_CONFIG['file']
DATA_DIR = config.DIRETORIOS['data']
REPORTS_DIR = config.DIRETORIOS['reports']
LOGS_DIR = config.DIRETORIOS['logs']
SCHEDULE_HOURS = config.SCHEDULE_CONFIG['horarios_execucao']
