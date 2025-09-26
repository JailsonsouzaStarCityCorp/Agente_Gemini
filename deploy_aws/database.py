"""
Sistema Avançado de Banco de Dados do Agente de IA
"""
import sqlite3
import json
import logging
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from pathlib import Path
from config import config

class DatabaseManager:
    """Gerenciador central de banco de dados"""
    
    def __init__(self):
        self.config = config.DATABASE_CONFIG
        self.logger = logging.getLogger('database.manager')
        self.conexao = None
        self.inicializar_banco()
    
    def inicializar_banco(self):
        """Inicializa o banco de dados SQLite"""
        try:
            if self.config['sqlite']['habilitado']:
                self.conexao = sqlite3.connect(
                    self.config['sqlite']['arquivo'],
                    check_same_thread=False
                )
                self.conexao.row_factory = sqlite3.Row
                self.criar_tabelas()
                self.logger.info("Banco de dados SQLite inicializado")
            else:
                self.logger.warning("SQLite desabilitado")
        except Exception as e:
            self.logger.error(f"Erro ao inicializar banco: {str(e)}")
    
    def criar_tabelas(self):
        """Cria todas as tabelas necessárias"""
        cursor = self.conexao.cursor()
        
        # Tabela de sessões
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT,
                inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                fim TIMESTAMP,
                status TEXT DEFAULT 'ativa',
                dados TEXT
            )
        ''')
        
        # Tabela de processamentos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS processamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                arquivo TEXT,
                status TEXT NOT NULL,
                inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                fim TIMESTAMP,
                resultado TEXT,
                erro TEXT,
                usuario TEXT
            )
        ''')
        
        # Tabela de vendas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data DATE,
                produto TEXT,
                valor DECIMAL(10,2),
                vendedor TEXT,
                regiao TEXT,
                processamento_id INTEGER,
                FOREIGN KEY (processamento_id) REFERENCES processamentos (id)
            )
        ''')
        
        # Tabela de suporte
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS suporte (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pergunta TEXT NOT NULL,
                resposta TEXT,
                urgencia TEXT,
                satisfacao INTEGER,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                usuario TEXT,
                processamento_id INTEGER,
                FOREIGN KEY (processamento_id) REFERENCES processamentos (id)
            )
        ''')
        
        # Tabela de conteúdo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conteudo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                tema TEXT,
                plataforma TEXT,
                conteudo TEXT,
                publico_alvo TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                usuario TEXT,
                processamento_id INTEGER,
                FOREIGN KEY (processamento_id) REFERENCES processamentos (id)
            )
        ''')
        
        # Tabela de métricas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS metricas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                valor DECIMAL(10,2),
                unidade TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                categoria TEXT,
                tags TEXT
            )
        ''')
        
        # Tabela de logs
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs_sistema (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nivel TEXT NOT NULL,
                mensagem TEXT NOT NULL,
                modulo TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                dados TEXT
            )
        ''')
        
        # Tabela de configurações
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS configuracoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chave TEXT UNIQUE NOT NULL,
                valor TEXT,
                tipo TEXT,
                descricao TEXT,
                atualizado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabela de usuários
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE,
                perfil TEXT,
                ativo BOOLEAN DEFAULT 1,
                criado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                ultimo_acesso TIMESTAMP
            )
        ''')
        
        # Tabela de integrações
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS integracoes_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                destino TEXT,
                status TEXT,
                mensagem TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                dados TEXT
            )
        ''')
        
        self.conexao.commit()
        self.logger.info("Tabelas criadas com sucesso")
    
    def inserir_processamento(self, tipo: str, arquivo: str = None, usuario: str = None) -> int:
        """Insere novo processamento e retorna ID"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute('''
                INSERT INTO processamentos (tipo, arquivo, status, usuario)
                VALUES (?, ?, 'iniciado', ?)
            ''', (tipo, arquivo, usuario))
            
            processamento_id = cursor.lastrowid
            self.conexao.commit()
            
            self.logger.info(f"Processamento {processamento_id} inserido")
            return processamento_id
            
        except Exception as e:
            self.logger.error(f"Erro ao inserir processamento: {str(e)}")
            return None
    
    def atualizar_processamento(self, processamento_id: int, status: str, resultado: str = None, erro: str = None):
        """Atualiza status do processamento"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute('''
                UPDATE processamentos 
                SET status = ?, resultado = ?, erro = ?, fim = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (status, resultado, erro, processamento_id))
            
            self.conexao.commit()
            self.logger.info(f"Processamento {processamento_id} atualizado para {status}")
            
        except Exception as e:
            self.logger.error(f"Erro ao atualizar processamento: {str(e)}")
    
    def inserir_venda(self, data: str, produto: str, valor: float, vendedor: str, regiao: str, processamento_id: int):
        """Insere dados de venda"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute('''
                INSERT INTO vendas (data, produto, valor, vendedor, regiao, processamento_id)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (data, produto, valor, vendedor, regiao, processamento_id))
            
            self.conexao.commit()
            
        except Exception as e:
            self.logger.error(f"Erro ao inserir venda: {str(e)}")
    
    def inserir_suporte(self, pergunta: str, resposta: str, urgencia: str, usuario: str, processamento_id: int):
        """Insere atendimento de suporte"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute('''
                INSERT INTO suporte (pergunta, resposta, urgencia, usuario, processamento_id)
                VALUES (?, ?, ?, ?, ?)
            ''', (pergunta, resposta, urgencia, usuario, processamento_id))
            
            self.conexao.commit()
            
        except Exception as e:
            self.logger.error(f"Erro ao inserir suporte: {str(e)}")
    
    def inserir_conteudo(self, tipo: str, tema: str, plataforma: str, conteudo: str, publico_alvo: str, usuario: str, processamento_id: int):
        """Insere conteúdo gerado"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute('''
                INSERT INTO conteudo (tipo, tema, plataforma, conteudo, publico_alvo, usuario, processamento_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (tipo, tema, plataforma, conteudo, publico_alvo, usuario, processamento_id))
            
            self.conexao.commit()
            
        except Exception as e:
            self.logger.error(f"Erro ao inserir conteúdo: {str(e)}")
    
    def inserir_metrica(self, nome: str, valor: float, unidade: str, categoria: str, tags: List[str] = None):
        """Insere métrica do sistema"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute('''
                INSERT INTO metricas (nome, valor, unidade, categoria, tags)
                VALUES (?, ?, ?, ?, ?)
            ''', (nome, valor, unidade, categoria, json.dumps(tags or [])))
            
            self.conexao.commit()
            
        except Exception as e:
            self.logger.error(f"Erro ao inserir métrica: {str(e)}")
    
    def obter_estatisticas(self, periodo_dias: int = 30) -> Dict[str, Any]:
        """Obtém estatísticas do sistema"""
        try:
            cursor = self.conexao.cursor()
            
            # Processamentos
            cursor.execute('''
                SELECT COUNT(*) as total,
                       SUM(CASE WHEN status = 'concluido' THEN 1 ELSE 0 END) as sucessos,
                       SUM(CASE WHEN status = 'erro' THEN 1 ELSE 0 END) as erros
                FROM processamentos 
                WHERE inicio >= datetime('now', '-{} days')
            '''.format(periodo_dias))
            
            stats_processamento = cursor.fetchone()
            
            # Vendas
            cursor.execute('''
                SELECT COUNT(*) as total_vendas,
                       SUM(valor) as valor_total,
                       AVG(valor) as valor_medio
                FROM vendas 
                WHERE data >= date('now', '-{} days')
            '''.format(periodo_dias))
            
            stats_vendas = cursor.fetchone()
            
            # Suporte
            cursor.execute('''
                SELECT COUNT(*) as total_atendimentos,
                       COUNT(CASE WHEN urgencia = 'ALTA' THEN 1 END) as urgencia_alta
                FROM suporte 
                WHERE timestamp >= datetime('now', '-{} days')
            '''.format(periodo_dias))
            
            stats_suporte = cursor.fetchone()
            
            # Conteúdo
            cursor.execute('''
                SELECT COUNT(*) as total_conteudos,
                       COUNT(CASE WHEN plataforma = 'Instagram' THEN 1 END) as instagram,
                       COUNT(CASE WHEN plataforma = 'LinkedIn' THEN 1 END) as linkedin
                FROM conteudo 
                WHERE timestamp >= datetime('now', '-{} days')
            '''.format(periodo_dias))
            
            stats_conteudo = cursor.fetchone()
            
            return {
                'periodo_dias': periodo_dias,
                'processamentos': {
                    'total': stats_processamento['total'] or 0,
                    'sucessos': stats_processamento['sucessos'] or 0,
                    'erros': stats_processamento['erros'] or 0,
                    'taxa_sucesso': (stats_processamento['sucessos'] or 0) / max(stats_processamento['total'] or 1, 1) * 100
                },
                'vendas': {
                    'total_vendas': stats_vendas['total_vendas'] or 0,
                    'valor_total': stats_vendas['valor_total'] or 0,
                    'valor_medio': stats_vendas['valor_medio'] or 0
                },
                'suporte': {
                    'total_atendimentos': stats_suporte['total_atendimentos'] or 0,
                    'urgencia_alta': stats_suporte['urgencia_alta'] or 0
                },
                'conteudo': {
                    'total_conteudos': stats_conteudo['total_conteudos'] or 0,
                    'instagram': stats_conteudo['instagram'] or 0,
                    'linkedin': stats_conteudo['linkedin'] or 0
                }
            }
            
        except Exception as e:
            self.logger.error(f"Erro ao obter estatísticas: {str(e)}")
            return {}
    
    def obter_relatorio_detalhado(self, data_inicio: str, data_fim: str) -> Dict[str, Any]:
        """Obtém relatório detalhado do período"""
        try:
            cursor = self.conexao.cursor()
            
            # Processamentos por tipo
            cursor.execute('''
                SELECT tipo, COUNT(*) as quantidade, status
                FROM processamentos 
                WHERE inicio BETWEEN ? AND ?
                GROUP BY tipo, status
            ''', (data_inicio, data_fim))
            
            processamentos_por_tipo = {}
            for row in cursor.fetchall():
                tipo = row['tipo']
                if tipo not in processamentos_por_tipo:
                    processamentos_por_tipo[tipo] = {}
                processamentos_por_tipo[tipo][row['status']] = row['quantidade']
            
            # Top produtos vendidos
            cursor.execute('''
                SELECT produto, COUNT(*) as quantidade, SUM(valor) as valor_total
                FROM vendas 
                WHERE data BETWEEN ? AND ?
                GROUP BY produto
                ORDER BY quantidade DESC
                LIMIT 10
            ''', (data_inicio, data_fim))
            
            top_produtos = [dict(row) for row in cursor.fetchall()]
            
            # Atendimentos por urgência
            cursor.execute('''
                SELECT urgencia, COUNT(*) as quantidade
                FROM suporte 
                WHERE timestamp BETWEEN ? AND ?
                GROUP BY urgencia
            ''', (data_inicio, data_fim))
            
            atendimentos_urgencia = {row['urgencia']: row['quantidade'] for row in cursor.fetchall()}
            
            return {
                'periodo': {'inicio': data_inicio, 'fim': data_fim},
                'processamentos_por_tipo': processamentos_por_tipo,
                'top_produtos': top_produtos,
                'atendimentos_urgencia': atendimentos_urgencia
            }
            
        except Exception as e:
            self.logger.error(f"Erro ao obter relatório: {str(e)}")
            return {}
    
    def fechar_conexao(self):
        """Fecha conexão com banco"""
        if self.conexao:
            self.conexao.close()
            self.logger.info("Conexão com banco fechada")

# Instância global do gerenciador
db_manager = DatabaseManager()
