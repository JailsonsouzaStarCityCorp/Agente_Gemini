"""
Utilitários e funções auxiliares
"""
import logging
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

def setup_logging(log_file: str = 'logs/agente.log', level: str = 'INFO') -> logging.Logger:
    """Configura o sistema de logging"""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger('agente')

def executar_com_seguranca(func, *args, **kwargs) -> Dict[str, Any]:
    """Executa função com tratamento de erros"""
    try:
        resultado = func(*args, **kwargs)
        return {"sucesso": True, "dados": resultado}
    except Exception as e:
        logging.error(f"Erro na execução: {str(e)}")
        return {"sucesso": False, "erro": str(e)}

def salvar_resultado(dados: Any, arquivo: str) -> bool:
    """Salva dados em arquivo JSON"""
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False, default=str)
        return True
    except Exception as e:
        logging.error(f"Erro ao salvar arquivo {arquivo}: {str(e)}")
        return False

def carregar_dados(arquivo: str) -> Optional[Dict]:
    """Carrega dados de arquivo JSON"""
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Erro ao carregar arquivo {arquivo}: {str(e)}")
        return None

def formatar_timestamp() -> str:
    """Retorna timestamp formatado"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
