"""
Agente Automatizado com Agendamento
"""
import schedule
import time
import logging
import pandas as pd
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL, SCHEDULE_HOURS
from utils import executar_com_seguranca, salvar_resultado, formatar_timestamp

# Configurar API
genai.configure(api_key=GEMINI_API_KEY)

class AgenteAutomatizado:
    """Agente com capacidades de automação e agendamento"""
    
    def __init__(self):
        self.model = genai.GenerativeModel(GEMINI_MODEL)
        self.logger = logging.getLogger('agente.automatizado')
        self.log_atividades = []
        self.importar_agentes()
    
    def importar_agentes(self):
        """Importa outros agentes para uso integrado"""
        try:
            from agente_vendas import AgenteAnaliseVendas
            from agente_suporte import AgenteSuporte
            from agente_conteudo import AgenteConteudo
            
            self.agente_vendas = AgenteAnaliseVendas()
            self.agente_suporte = AgenteSuporte()
            self.agente_conteudo = AgenteConteudo()
            
            self.logger.info("Agentes importados com sucesso")
        except ImportError as e:
            self.logger.error(f"Erro ao importar agentes: {str(e)}")
    
    def monitorar_pasta_relatorios(self, caminho_pasta: str = "data") -> List[Path]:
        """Monitora pasta para novos relatórios"""
        try:
            pasta = Path(caminho_pasta)
            if not pasta.exists():
                pasta.mkdir(exist_ok=True)
                return []
            
            arquivos_novos = []
            tempo_atual = time.time()
            
            for arquivo in pasta.glob("*.xlsx"):
                # Arquivos modificados na última hora
                if arquivo.stat().st_mtime > tempo_atual - 3600:
                    arquivos_novos.append(arquivo)
            
            self.logger.info(f"Encontrados {len(arquivos_novos)} novos arquivos")
            return arquivos_novos
            
        except Exception as e:
            self.logger.error(f"Erro ao monitorar pasta: {str(e)}")
            return []
    
    def processar_arquivo_automaticamente(self, arquivo: Path) -> Dict[str, Any]:
        """Processa arquivo automaticamente baseado no tipo"""
        try:
            self.logger.info(f"Processando arquivo: {arquivo.name}")
            
            # Determinar tipo de processamento baseado no nome
            if "vendas" in arquivo.name.lower():
                resultado = self.agente_vendas.executar_analise(str(arquivo))
            else:
                # Processamento genérico
                resultado = self.processar_arquivo_generico(arquivo)
            
            return resultado
            
        except Exception as e:
            self.logger.error(f"Erro ao processar arquivo {arquivo.name}: {str(e)}")
            return {"sucesso": False, "erro": str(e)}
    
    def processar_arquivo_generico(self, arquivo: Path) -> Dict[str, Any]:
        """Processamento genérico para arquivos não específicos"""
        try:
            prompt = f"""
            Analise este arquivo e forneça um resumo executivo:
            Nome: {arquivo.name}
            Tamanho: {arquivo.stat().st_size} bytes
            Modificado: {datetime.fromtimestamp(arquivo.stat().st_mtime)}
            
            Forneça:
            1. Tipo de arquivo identificado
            2. Possíveis usos
            3. Recomendações de processamento
            """
            
            response = self.model.generate_content(prompt)
            
            resultado = {
                "arquivo": arquivo.name,
                "analise": response.text,
                "timestamp": formatar_timestamp(),
                "tipo": "processamento_generico"
            }
            
            return {"sucesso": True, "dados": resultado}
            
        except Exception as e:
            return {"sucesso": False, "erro": str(e)}
    
    def executar_rotina_automatica(self):
        """Execução automática programada"""
        self.logger.info(f"🤖 Iniciando rotina automática - {formatar_timestamp()}")
        
        try:
            # Monitorar novos arquivos
            novos_arquivos = self.monitorar_pasta_relatorios()
            
            resultados = []
            for arquivo in novos_arquivos:
                resultado = self.processar_arquivo_automaticamente(arquivo)
                resultados.append(resultado)
                
                # Log da atividade
                self.log_atividades.append({
                    "timestamp": formatar_timestamp(),
                    "arquivo": arquivo.name,
                    "status": "processado" if resultado.get("sucesso") else "erro",
                    "resultado": resultado
                })
            
            # Salvar log de atividades
            if resultados:
                arquivo_log = f"reports/rotina_automatica_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                salvar_resultado({
                    "timestamp": formatar_timestamp(),
                    "arquivos_processados": len(novos_arquivos),
                    "resultados": resultados
                }, arquivo_log)
            
            self.logger.info(f"✅ Rotina automática concluída - {len(novos_arquivos)} arquivos processados")
            
        except Exception as e:
            self.logger.error(f"❌ Erro na rotina automática: {str(e)}")
    
    def programar_execucoes(self):
        """Programa execuções automáticas"""
        try:
            # Limpar agendamentos existentes
            schedule.clear()
            
            # Programar execuções nos horários configurados
            for hora in SCHEDULE_HOURS:
                schedule.every().day.at(f"{hora:02d}:00").do(self.executar_rotina_automatica)
            
            # Execução de teste a cada hora
            schedule.every().hour.do(self.executar_rotina_automatica)
            
            self.logger.info(f"⏰ Agente programado para executar às {SCHEDULE_HOURS}")
            self.logger.info("Pressione Ctrl+C para parar o agente")
            
            # Loop principal
            while True:
                schedule.run_pending()
                time.sleep(60)  # Verificar a cada minuto
                
        except KeyboardInterrupt:
            self.logger.info("🛑 Agente interrompido pelo usuário")
        except Exception as e:
            self.logger.error(f"Erro no agendamento: {str(e)}")
    
    def iniciar_agente(self):
        """Inicia o agente automatizado"""
        self.logger.info("🚀 Iniciando Agente Automatizado")
        self.programar_execucoes()
