"""
Agente de Suporte Offline - Funciona sem API
"""
import json
import logging
import pandas as pd
from typing import Dict, Any, List
from utils import executar_com_seguranca, salvar_resultado

class AgenteSuporteOffline:
    """Agente de suporte que funciona offline"""
    
    def __init__(self):
        self.logger = logging.getLogger('agente.suporte.offline')
        self.base_conhecimento = self.carregar_base_conhecimento()
        self.respostas_predefinidas = self.carregar_respostas_predefinidas()
    
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
    
    def carregar_respostas_predefinidas(self) -> Dict[str, str]:
        """Carrega respostas pré-definidas para perguntas comuns"""
        return {
            "pedido": "Para fazer um pedido, você pode:\n1. Acessar nossa loja online\n2. Entrar em contato pelo telefone (11) 99999-9999\n3. Enviar email para vendas@empresa.com\n\nNossa equipe está pronta para te ajudar! 😊",
            
            "entrega": "Nossos prazos de entrega são:\n• Região Metropolitana: 2-3 dias úteis\n• Interior: 5-7 dias úteis\n• Outros estados: 7-10 dias úteis\n\nVocê pode acompanhar seu pedido pelo código de rastreamento! 📦",
            
            "devolução": "Nossa política de devolução:\n• Prazo: 30 dias após o recebimento\n• Produto deve estar em perfeito estado\n• Sem custos para devolução\n• Reembolso em até 5 dias úteis\n\nPara iniciar uma devolução, entre em contato conosco! 🔄",
            
            "pagamento": "Aceitamos as seguintes formas de pagamento:\n• Cartão de crédito (Visa, Mastercard, Elo)\n• PIX (desconto de 5%)\n• Boleto bancário\n• Cartão de débito\n\nPagamento seguro e protegido! 💳",
            
            "suporte": "Nosso suporte está disponível:\n• Chat online: 24/7\n• Telefone: (11) 99999-9999\n• Email: suporte@empresa.com\n• WhatsApp: (11) 99999-9999\n\nSempre prontos para te ajudar! 🎧",
            
            "produto": "Nossos produtos principais:\n• Produto A: Solução empresarial completa\n• Produto B: Ferramenta de análise de dados\n• Produto C: Sistema de automação\n\nQuer saber mais sobre algum produto específico? 😊"
        }
    
    def identificar_tipo_pergunta(self, pergunta: str) -> str:
        """Identifica o tipo de pergunta baseado em palavras-chave"""
        pergunta_lower = pergunta.lower()
        
        if any(palavra in pergunta_lower for palavra in ['pedido', 'comprar', 'adquirir', 'encomendar']):
            return 'pedido'
        elif any(palavra in pergunta_lower for palavra in ['entrega', 'prazo', 'quando chega', 'demora']):
            return 'entrega'
        elif any(palavra in pergunta_lower for palavra in ['devolução', 'devolver', 'trocar', 'reembolso']):
            return 'devolução'
        elif any(palavra in pergunta_lower for palavra in ['pagamento', 'pagar', 'cartão', 'pix', 'boleto']):
            return 'pagamento'
        elif any(palavra in pergunta_lower for palavra in ['suporte', 'ajuda', 'problema', 'dúvida']):
            return 'suporte'
        elif any(palavra in pergunta_lower for palavra in ['produto', 'serviço', 'o que vocês vendem']):
            return 'produto'
        else:
            return 'geral'
    
    def gerar_resposta_offline(self, pergunta: str) -> str:
        """Gera resposta offline baseada em templates"""
        tipo = self.identificar_tipo_pergunta(pergunta)
        
        if tipo in self.respostas_predefinidas:
            resposta = self.respostas_predefinidas[tipo]
        else:
            resposta = f"""Olá! 👋 

Obrigado por entrar em contato conosco!

Sua pergunta: "{pergunta}"

Nossa equipe de suporte está analisando sua solicitação e retornará em breve.

Enquanto isso, você pode:
• Acessar nosso FAQ: www.empresa.com/faq
• Entrar em contato: (11) 99999-9999
• Enviar email: suporte@empresa.com

Atenciosamente,
Equipe de Suporte 🎧"""
        
        return resposta
    
    def classificar_urgencia_offline(self, pergunta: str) -> str:
        """Classifica urgência baseada em palavras-chave"""
        pergunta_lower = pergunta.lower()
        
        # Palavras de alta urgência
        alta_urgencia = ['urgente', 'emergência', 'problema crítico', 'não funciona', 'erro', 'falha']
        if any(palavra in pergunta_lower for palavra in alta_urgencia):
            return 'ALTA'
        
        # Palavras de baixa urgência
        baixa_urgencia = ['informação', 'dúvida', 'curiosidade', 'preço', 'catálogo']
        if any(palavra in pergunta_lower for palavra in baixa_urgencia):
            return 'BAIXA'
        
        # Padrão é média urgência
        return 'MÉDIA'
    
    def processar_solicitacao(self, pergunta: str) -> Dict[str, Any]:
        """Processa solicitação completa de suporte"""
        try:
            self.logger.info(f"Processando pergunta: {pergunta[:50]}...")
            
            # Gerar resposta offline
            resposta = self.gerar_resposta_offline(pergunta)
            
            # Classificar urgência
            urgencia = self.classificar_urgencia_offline(pergunta)
            
            resultado_final = {
                "pergunta": pergunta,
                "resposta": resposta,
                "urgencia": urgencia,
                "timestamp": pd.Timestamp.now().isoformat(),
                "status": "processado",
                "modo": "offline"
            }
            
            # Salvar histórico
            arquivo_historico = f"reports/suporte_offline_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.json"
            salvar_resultado(resultado_final, arquivo_historico)
            
            self.logger.info("Solicitação processada com sucesso (modo offline)")
            return {"sucesso": True, "dados": resultado_final}
            
        except Exception as e:
            self.logger.error(f"Erro no processamento offline: {str(e)}")
            return {"sucesso": False, "erro": str(e)}
