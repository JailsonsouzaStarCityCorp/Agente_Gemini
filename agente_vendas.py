"""
Agente de Análise de Vendas
"""
import pandas as pd
import json
import logging
from typing import Dict, Any, Tuple
import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL
from utils import executar_com_seguranca, salvar_resultado

# Configurar API
genai.configure(api_key=GEMINI_API_KEY)

class AgenteAnaliseVendas:
    """Agente especializado em análise de dados de vendas"""
    
    def __init__(self):
        self.model = genai.GenerativeModel(GEMINI_MODEL)
        self.logger = logging.getLogger('agente.vendas')
    
    def processar_planilha(self, arquivo_excel: str) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Lê e processa planilha de vendas"""
        try:
            df = pd.read_excel(arquivo_excel)
            
            # Preparar dados para análise
            resumo_dados = {
                "total_linhas": len(df),
                "colunas": df.columns.tolist(),
                "vendas_totais": df['valor_venda'].sum() if 'valor_venda' in df.columns else 0,
                "periodo": f"{df['data'].min()} a {df['data'].max()}" if 'data' in df.columns else "Período não especificado",
                "timestamp_processamento": pd.Timestamp.now().isoformat()
            }
            
            self.logger.info(f"Planilha processada: {len(df)} registros")
            return df, resumo_dados
            
        except Exception as e:
            self.logger.error(f"Erro ao processar planilha: {str(e)}")
            raise
    
    def gerar_insights(self, dados_resumo: Dict[str, Any], amostra_dados: pd.DataFrame) -> str:
        """Usa Gemini para gerar insights inteligentes"""
        try:
            prompt = f"""
            Analise estes dados de vendas e gere insights profissionais:
            
            RESUMO DOS DADOS:
            {json.dumps(dados_resumo, indent=2, default=str)}
            
            AMOSTRA DOS DADOS:
            {amostra_dados.head(10).to_string()}
            
            Forneça uma análise estruturada com:
            1. 📈 PRINCIPAIS TENDÊNCIAS identificadas
            2. 🏆 PRODUTOS/PERÍODOS de maior performance
            3. 💡 RECOMENDAÇÕES de ação estratégica
            4. ⚠️ ALERTAS sobre possíveis problemas
            5. 📊 MÉTRICAS de performance sugeridas
            
            Seja objetivo, profissional e acionável.
            """
            
            response = self.model.generate_content(prompt)
            self.logger.info("Insights gerados com sucesso")
            return response.text
            
        except Exception as e:
            self.logger.error(f"Erro ao gerar insights: {str(e)}")
            return f"Erro na análise: {str(e)}"
    
    def executar_analise(self, arquivo: str) -> Dict[str, Any]:
        """Fluxo completo de análise de vendas"""
        self.logger.info(f"Iniciando análise do arquivo: {arquivo}")
        
        # Processar planilha
        resultado = executar_com_seguranca(self.processar_planilha, arquivo)
        if not resultado["sucesso"]:
            return resultado
        
        df, resumo = resultado["dados"]
        
        # Gerar insights
        insights = self.gerar_insights(resumo, df)
        
        # Preparar resultado final
        resultado_final = {
            "arquivo_origem": arquivo,
            "resumo": resumo,
            "insights": insights,
            "timestamp": pd.Timestamp.now().isoformat(),
            "status": "concluido"
        }
        
        # Salvar resultado
        arquivo_resultado = f"reports/analise_vendas_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.json"
        salvar_resultado(resultado_final, arquivo_resultado)
        
        self.logger.info("Análise de vendas concluída com sucesso")
        return {"sucesso": True, "dados": resultado_final}
