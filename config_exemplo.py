"""
Arquivo de configuração de exemplo
Copie este arquivo para config.py e ajuste as configurações
"""
import os
from pathlib import Path

# Configurações da API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'SUA_API_KEY_AQUI')
GEMINI_MODEL = 'gemini-pro'

# Configurações de logging
LOG_LEVEL = 'INFO'
LOG_FILE = 'logs/agente.log'

# Configurações de arquivos
DATA_DIR = Path('data')
REPORTS_DIR = Path('reports')
LOGS_DIR = Path('logs')

# Criar diretórios se não existirem
for directory in [DATA_DIR, REPORTS_DIR, LOGS_DIR]:
    directory.mkdir(exist_ok=True)

# Configurações de agendamento
SCHEDULE_HOURS = [9, 15, 21]  # Horários de execução automática

# Configurações específicas por agente
CONFIG_VENDAS = {
    'colunas_obrigatorias': ['data', 'valor_venda'],
    'formato_data': '%Y-%m-%d'
}

CONFIG_SUPORTE = {
    'urgencia_padrao': 'MÉDIA',
    'tempo_resposta_esperado': 30  # minutos
}

CONFIG_CONTEUDO = {
    'tamanho_max_post': 2200,
    'tamanho_max_newsletter': 500,
    'hashtags_max': 5
}
