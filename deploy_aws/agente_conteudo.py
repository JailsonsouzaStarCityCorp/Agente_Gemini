"""
Agente de Criação de Conteúdo
"""
import json
import logging
import pandas as pd
from typing import Dict, Any, List
import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL
from utils import executar_com_seguranca, salvar_resultado

# Configurar API
genai.configure(api_key=GEMINI_API_KEY)

class AgenteConteudo:
    """Agente especializado em criação de conteúdo para marketing"""
    
    def __init__(self):
        self.model = genai.GenerativeModel(GEMINI_MODEL)
        self.logger = logging.getLogger('agente.conteudo')
    
    def gerar_post_social(self, tema: str, plataforma: str, tom: str, publico_alvo: str = "geral") -> str:
        """Gera posts adaptados para cada rede social"""
        try:
            diretrizes_plataforma = {
                "Instagram": "- Use hashtags relevantes (3-5)\n- Inclua emojis moderadamente\n- Foque em visual e storytelling\n- Máximo 2.200 caracteres",
                "LinkedIn": "- Tom profissional e informativo\n- Evite emojis excessivos\n- Inclua dados e insights\n- Máximo 1.300 caracteres",
                "Twitter": "- Seja conciso e direto\n- Use hashtags estratégicas (1-2)\n- Engaje com perguntas\n- Máximo 280 caracteres",
                "Facebook": "- Tom conversacional\n- Use emojis moderadamente\n- Inclua call-to-action claro\n- Máximo 63.206 caracteres"
            }
            
            prompt = f"""
            Crie um post para {plataforma} sobre: {tema}
            
            Público-alvo: {publico_alvo}
            Tom desejado: {tom}
            
            Diretrizes específicas para {plataforma}:
            {diretrizes_plataforma.get(plataforma, "- Adapte o conteúdo para a plataforma")}
            
            ESTRUTURA DO POST:
            1. Hook/gancho inicial (primeira linha impactante)
            2. Desenvolvimento do tema
            3. Call-to-action claro
            4. Hashtags relevantes (se aplicável)
            
            Seja criativo, engajador e alinhado com a marca.
            """
            
            response = self.model.generate_content(prompt)
            self.logger.info(f"Post gerado para {plataforma} sobre {tema}")
            return response.text
            
        except Exception as e:
            self.logger.error(f"Erro ao gerar post: {str(e)}")
            return f"Erro na criação do conteúdo: {str(e)}"
    
    def criar_newsletter(self, topicos: List[str], publico_alvo: str, empresa: str = "Nossa empresa") -> str:
        """Gera newsletter personalizada"""
        try:
            prompt = f"""
            Crie uma newsletter profissional para: {publico_alvo}
            
            Empresa: {empresa}
            Tópicos a abordar:
            {chr(10).join([f"- {topico}" for topico in topicos])}
            
            ESTRUTURA DA NEWSLETTER:
            1. Assunto chamativo (máximo 50 caracteres)
            2. Introdução personalizada e envolvente
            3. Desenvolvimento dos tópicos com subtítulos
            4. Call-to-action claro e direcionado
            5. Despedida profissional
            
            DIRETRIZES:
            - Tom: profissional mas acessível
            - Linguagem: clara e objetiva
            - Formatação: use quebras de linha e subtítulos
            - Comprimento: 300-500 palavras
            - Inclua valor real para o leitor
            """
            
            response = self.model.generate_content(prompt)
            self.logger.info(f"Newsletter criada para {publico_alvo}")
            return response.text
            
        except Exception as e:
            self.logger.error(f"Erro ao criar newsletter: {str(e)}")
            return f"Erro na criação da newsletter: {str(e)}"
    
    def gerar_campanha_completa(self, tema: str, plataformas: List[str], publico_alvo: str) -> Dict[str, Any]:
        """Gera campanha completa para múltiplas plataformas"""
        try:
            campanha = {
                "tema": tema,
                "publico_alvo": publico_alvo,
                "plataformas": {},
                "newsletter": "",
                "timestamp": pd.Timestamp.now().isoformat()
            }
            
            # Gerar posts para cada plataforma
            for plataforma in plataformas:
                post = self.gerar_post_social(tema, plataforma, "profissional", publico_alvo)
                campanha["plataformas"][plataforma] = post
            
            # Gerar newsletter
            topicos = [f"Tema principal: {tema}", "Dicas práticas", "Cases de sucesso", "Próximos passos"]
            newsletter = self.criar_newsletter(topicos, publico_alvo)
            campanha["newsletter"] = newsletter
            
            # Salvar campanha
            arquivo_campanha = f"reports/campanha_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.json"
            salvar_resultado(campanha, arquivo_campanha)
            
            self.logger.info(f"Campanha completa gerada para {tema}")
            return {"sucesso": True, "dados": campanha}
            
        except Exception as e:
            self.logger.error(f"Erro ao gerar campanha: {str(e)}")
            return {"sucesso": False, "erro": str(e)}
