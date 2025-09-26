"""
Agente de Suporte ao Cliente
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

class AgenteSuporte:
    """Agente especializado em atendimento ao cliente"""
    
    def __init__(self):
        self.model = genai.GenerativeModel(GEMINI_MODEL)
        self.logger = logging.getLogger('agente.suporte')
        self.base_conhecimento = self.carregar_base_conhecimento()
    
    def carregar_base_conhecimento(self) -> Dict[str, List[str]]:
        """Carrega FAQ e documentos de produto"""
        return {
            "produtos": [
                "Produto A - Solução empresarial completa",
                "Produto B - Ferramenta de análise de dados", 
                "Produto C - Sistema de automação"
            ],
            "faq": [
                "Como fazer um pedido? - Acesse nossa loja online ou entre em contato",
                "Política de devolução - 30 dias para devolução sem custos",
                "Formas de pagamento - Cartão, PIX, Boleto bancário",
                "Prazo de entrega - 5 a 10 dias úteis",
                "Suporte técnico - Disponível 24/7 via chat"
            ],
            "contatos": {
                "telefone": "(11) 99999-9999",
                "email": "suporte@empresa.com",
                "chat": "Disponível no site"
            }
        }
    
    def responder_pergunta(self, pergunta_usuario: str) -> str:
        """Gera resposta inteligente usando Gemini + base de conhecimento"""
        try:
            contexto = f"""
            PERGUNTA DO USUÁRIO: {pergunta_usuario}
            
            BASE DE CONHECIMENTO:
            Produtos disponíveis: {', '.join(self.base_conhecimento['produtos'])}
            
            FAQ principais:
            {chr(10).join(self.base_conhecimento['faq'])}
            
            Contatos de suporte:
            {json.dumps(self.base_conhecimento['contatos'], indent=2)}
            
            INSTRUÇÕES:
            - Seja prestativo, profissional e empático
            - Use informações da base de conhecimento quando relevante
            - Se não souber algo específico, oriente a procurar suporte humano
            - Seja conciso mas completo na resposta
            - Use emojis moderadamente para tornar a resposta mais amigável
            - Sempre ofereça canais de contato adicionais
            """
            
            response = self.model.generate_content(contexto)
            self.logger.info(f"Resposta gerada para pergunta: {pergunta_usuario[:50]}...")
            return response.text
            
        except Exception as e:
            self.logger.error(f"Erro ao gerar resposta: {str(e)}")
            # Usar modo offline como fallback
            return self.responder_pergunta_offline(pergunta_usuario)
    
    def responder_pergunta_offline(self, pergunta_usuario: str) -> str:
        """Resposta offline quando a API não está disponível"""
        pergunta_lower = pergunta_usuario.lower()
        
        # Respostas pré-definidas baseadas em palavras-chave
        if any(palavra in pergunta_lower for palavra in ['pedido', 'comprar', 'adquirir']):
            return """Olá! 👋 Ficaremos felizes em te ajudar a fazer seu pedido!

Você pode realizar sua compra de duas maneiras:

1. **Através da nossa loja online:** Acesse www.empresa.com
2. **Entrando em contato:** Telefone (11) 99999-9999

Nossa equipe de vendas está pronta para te atender e esclarecer todas as dúvidas!

Atenciosamente,
Equipe de Vendas 💼"""
        
        elif any(palavra in pergunta_lower for palavra in ['entrega', 'prazo', 'quando chega']):
            return """Olá! 📦 

Sobre o prazo de entrega:

• **Região Metropolitana:** 2-3 dias úteis
• **Interior:** 5-7 dias úteis  
• **Outros estados:** 7-10 dias úteis

Você receberá um código de rastreamento por email assim que o pedido for enviado.

Alguma dúvida específica sobre entrega? Estamos aqui para ajudar! 🚚"""
        
        elif any(palavra in pergunta_lower for palavra in ['devolução', 'devolver', 'trocar']):
            return """Olá! 🔄

Nossa política de devolução:

• **Prazo:** 30 dias após o recebimento
• **Condição:** Produto em perfeito estado
• **Custo:** Sem custos para devolução
• **Reembolso:** Até 5 dias úteis

Para iniciar uma devolução, entre em contato conosco:
📞 (11) 99999-9999
📧 suporte@empresa.com

Estamos prontos para te ajudar! 😊"""
        
        else:
            return f"""Olá! 👋 

Obrigado por entrar em contato conosco!

Sua pergunta: "{pergunta_usuario}"

Nossa equipe de suporte está analisando sua solicitação e retornará em breve.

**Canais de contato:**
📞 Telefone: (11) 99999-9999
📧 Email: suporte@empresa.com
💬 Chat: Disponível no site

Atenciosamente,
Equipe de Suporte 🎧"""
    
    def classificar_urgencia(self, pergunta: str) -> str:
        """Classifica urgência da solicitação"""
        try:
            prompt = f"""
            Classifique a urgência desta solicitação de suporte:
            "{pergunta}"
            
            Considere:
            - BAIXA: Dúvidas gerais, informações sobre produtos
            - MÉDIA: Problemas não críticos, solicitações de suporte
            - ALTA: Problemas críticos, urgências, reclamações
            
            Retorne apenas: BAIXA, MÉDIA ou ALTA
            """
            
            response = self.model.generate_content(prompt)
            urgencia = response.text.strip().upper()
            
            # Validar resposta
            if urgencia not in ['BAIXA', 'MÉDIA', 'ALTA']:
                urgencia = 'MÉDIA'  # Default seguro
            
            self.logger.info(f"Urgência classificada como: {urgencia}")
            return urgencia
            
        except Exception as e:
            self.logger.error(f"Erro ao classificar urgência: {str(e)}")
            return self.classificar_urgencia_offline(pergunta)
    
    def classificar_urgencia_offline(self, pergunta: str) -> str:
        """Classifica urgência offline baseada em palavras-chave"""
        pergunta_lower = pergunta.lower()
        
        # Palavras de alta urgência
        alta_urgencia = ['urgente', 'emergência', 'problema crítico', 'não funciona', 'erro', 'falha', 'quebrado']
        if any(palavra in pergunta_lower for palavra in alta_urgencia):
            return 'ALTA'
        
        # Palavras de baixa urgência
        baixa_urgencia = ['informação', 'dúvida', 'curiosidade', 'preço', 'catálogo', 'horário']
        if any(palavra in pergunta_lower for palavra in baixa_urgencia):
            return 'BAIXA'
        
        # Padrão é média urgência
        return 'MÉDIA'
    
    def processar_solicitacao(self, pergunta: str) -> Dict[str, Any]:
        """Processa solicitação completa de suporte"""
        resultado = executar_com_seguranca(self.responder_pergunta, pergunta)
        if not resultado["sucesso"]:
            return resultado
        
        resposta = resultado["dados"]
        urgencia = self.classificar_urgencia(pergunta)
        
        resultado_final = {
            "pergunta": pergunta,
            "resposta": resposta,
            "urgencia": urgencia,
            "timestamp": pd.Timestamp.now().isoformat(),
            "status": "processado"
        }
        
        # Salvar histórico
        arquivo_historico = f"reports/suporte_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.json"
        salvar_resultado(resultado_final, arquivo_historico)
        
        return {"sucesso": True, "dados": resultado_final}
