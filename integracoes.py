"""
Sistema Avançado de Integrações do Agente de IA
"""
import json
import requests
import smtplib
import sqlite3
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict, List, Any, Optional
from datetime import datetime
from config import config

class IntegracaoEmail:
    """Integração com sistemas de email"""
    
    def __init__(self):
        self.config = config.INTEGRACOES['email']
        self.logger = logging.getLogger('integracao.email')
    
    def enviar_email(self, destinatario: str, assunto: str, corpo: str, html: bool = False):
        """Envia email"""
        try:
            if not self.config['habilitado']:
                self.logger.warning("Integração de email desabilitada")
                return False
            
            msg = MIMEMultipart()
            msg['From'] = self.config['email_remetente']
            msg['To'] = destinatario
            msg['Subject'] = assunto
            
            if html:
                msg.attach(MIMEText(corpo, 'html'))
            else:
                msg.attach(MIMEText(corpo, 'plain'))
            
            server = smtplib.SMTP(self.config['smtp_server'], self.config['smtp_port'])
            server.starttls()
            server.login(self.config['email_usuario'], self.config['email_senha'])
            server.send_message(msg)
            server.quit()
            
            self.logger.info(f"Email enviado para {destinatario}")
            return True
            
        except Exception as e:
            self.logger.error(f"Erro ao enviar email: {str(e)}")
            return False
    
    def enviar_relatorio(self, destinatarios: List[str], relatorio: Dict[str, Any]):
        """Envia relatório por email"""
        assunto = f"Relatório do Agente - {datetime.now().strftime('%d/%m/%Y')}"
        
        corpo = f"""
        Relatório do Sistema de Agentes de IA
        
        Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}
        
        Resumo:
        - Total de processamentos: {relatorio.get('total_processamentos', 0)}
        - Sucessos: {relatorio.get('sucessos', 0)}
        - Erros: {relatorio.get('erros', 0)}
        
        Detalhes:
        {json.dumps(relatorio, indent=2, ensure_ascii=False)}
        """
        
        for destinatario in destinatarios:
            self.enviar_email(destinatario, assunto, corpo)

class IntegracaoWhatsApp:
    """Integração com WhatsApp Business API"""
    
    def __init__(self):
        self.config = config.INTEGRACOES['whatsapp']
        self.logger = logging.getLogger('integracao.whatsapp')
    
    def enviar_mensagem(self, numero: str, mensagem: str):
        """Envia mensagem via WhatsApp"""
        try:
            if not self.config['habilitado']:
                self.logger.warning("Integração WhatsApp desabilitada")
                return False
            
            url = f"https://graph.facebook.com/v17.0/{self.config['numero_telefone']}/messages"
            headers = {
                'Authorization': f"Bearer {self.config['api_key']}",
                'Content-Type': 'application/json'
            }
            
            data = {
                "messaging_product": "whatsapp",
                "to": numero,
                "type": "text",
                "text": {"body": mensagem}
            }
            
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code == 200:
                self.logger.info(f"Mensagem WhatsApp enviada para {numero}")
                return True
            else:
                self.logger.error(f"Erro ao enviar WhatsApp: {response.text}")
                return False
                
        except Exception as e:
            self.logger.error(f"Erro na integração WhatsApp: {str(e)}")
            return False

class IntegracaoTelegram:
    """Integração com Telegram Bot"""
    
    def __init__(self):
        self.config = config.INTEGRACOES['telegram']
        self.logger = logging.getLogger('integracao.telegram')
    
    def enviar_mensagem(self, mensagem: str, chat_id: str = None):
        """Envia mensagem via Telegram"""
        try:
            if not self.config['habilitado']:
                self.logger.warning("Integração Telegram desabilitada")
                return False
            
            chat_id = chat_id or self.config['chat_id']
            url = f"https://api.telegram.org/bot{self.config['bot_token']}/sendMessage"
            
            data = {
                'chat_id': chat_id,
                'text': mensagem,
                'parse_mode': 'HTML'
            }
            
            response = requests.post(url, data=data)
            
            if response.status_code == 200:
                self.logger.info(f"Mensagem Telegram enviada para {chat_id}")
                return True
            else:
                self.logger.error(f"Erro ao enviar Telegram: {response.text}")
                return False
                
        except Exception as e:
            self.logger.error(f"Erro na integração Telegram: {str(e)}")
            return False

class IntegracaoSlack:
    """Integração com Slack"""
    
    def __init__(self):
        self.config = config.INTEGRACOES['slack']
        self.logger = logging.getLogger('integracao.slack')
    
    def enviar_mensagem(self, mensagem: str, canal: str = None):
        """Envia mensagem para canal do Slack"""
        try:
            if not self.config['habilitado']:
                self.logger.warning("Integração Slack desabilitada")
                return False
            
            canal = canal or self.config['canal']
            url = self.config['webhook_url']
            
            data = {
                "channel": canal,
                "text": mensagem,
                "username": "Agente IA",
                "icon_emoji": ":robot_face:"
            }
            
            response = requests.post(url, json=data)
            
            if response.status_code == 200:
                self.logger.info(f"Mensagem Slack enviada para {canal}")
                return True
            else:
                self.logger.error(f"Erro ao enviar Slack: {response.text}")
                return False
                
        except Exception as e:
            self.logger.error(f"Erro na integração Slack: {str(e)}")
            return False

class IntegracaoDiscord:
    """Integração com Discord"""
    
    def __init__(self):
        self.config = config.INTEGRACOES['discord']
        self.logger = logging.getLogger('integracao.discord')
    
    def enviar_mensagem(self, mensagem: str, canal_id: str = None):
        """Envia mensagem para canal do Discord"""
        try:
            if not self.config['habilitado']:
                self.logger.warning("Integração Discord desabilitada")
                return False
            
            canal_id = canal_id or self.config['canal_id']
            url = f"https://discord.com/api/v10/channels/{canal_id}/messages"
            
            headers = {
                'Authorization': f"Bot {self.config['bot_token']}",
                'Content-Type': 'application/json'
            }
            
            data = {
                "content": mensagem
            }
            
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code == 200:
                self.logger.info(f"Mensagem Discord enviada para canal {canal_id}")
                return True
            else:
                self.logger.error(f"Erro ao enviar Discord: {response.text}")
                return False
                
        except Exception as e:
            self.logger.error(f"Erro na integração Discord: {str(e)}")
            return False

class IntegracaoTeams:
    """Integração com Microsoft Teams"""
    
    def __init__(self):
        self.config = config.INTEGRACOES['teams']
        self.logger = logging.getLogger('integracao.teams')
    
    def enviar_mensagem(self, mensagem: str, titulo: str = "Notificação do Agente"):
        """Envia mensagem para Teams"""
        try:
            if not self.config['habilitado']:
                self.logger.warning("Integração Teams desabilitada")
                return False
            
            url = self.config['webhook_url']
            
            data = {
                "@type": "MessageCard",
                "@context": "http://schema.org/extensions",
                "themeColor": "0076D7",
                "summary": titulo,
                "sections": [{
                    "activityTitle": titulo,
                    "activitySubtitle": f"Agente IA - {datetime.now().strftime('%d/%m/%Y %H:%M')}",
                    "activityImage": "https://adaptivecards.io/content/robots/Robot1.png",
                    "text": mensagem,
                    "markdown": True
                }]
            }
            
            response = requests.post(url, json=data)
            
            if response.status_code == 200:
                self.logger.info("Mensagem Teams enviada")
                return True
            else:
                self.logger.error(f"Erro ao enviar Teams: {response.text}")
                return False
                
        except Exception as e:
            self.logger.error(f"Erro na integração Teams: {str(e)}")
            return False

class GerenciadorIntegracoes:
    """Gerenciador central de todas as integrações"""
    
    def __init__(self):
        self.email = IntegracaoEmail()
        self.whatsapp = IntegracaoWhatsApp()
        self.telegram = IntegracaoTelegram()
        self.slack = IntegracaoSlack()
        self.discord = IntegracaoDiscord()
        self.teams = IntegracaoTeams()
        self.logger = logging.getLogger('gerenciador.integracoes')
    
    def enviar_notificacao_global(self, mensagem: str, tipo: str = "info"):
        """Envia notificação para todos os canais habilitados"""
        resultados = {}
        
        # Email
        if config.INTEGRACOES['email']['habilitado']:
            resultados['email'] = self.email.enviar_email(
                config.INTEGRACOES['email']['email_remetente'],
                f"Notificação do Agente - {tipo.upper()}",
                mensagem
            )
        
        # WhatsApp
        if config.INTEGRACOES['whatsapp']['habilitado']:
            resultados['whatsapp'] = self.whatsapp.enviar_mensagem(
                config.INTEGRACOES['whatsapp']['numero_telefone'],
                mensagem
            )
        
        # Telegram
        if config.INTEGRACOES['telegram']['habilitado']:
            resultados['telegram'] = self.telegram.enviar_mensagem(mensagem)
        
        # Slack
        if config.INTEGRACOES['slack']['habilitado']:
            resultados['slack'] = self.slack.enviar_mensagem(mensagem)
        
        # Discord
        if config.INTEGRACOES['discord']['habilitado']:
            resultados['discord'] = self.discord.enviar_mensagem(mensagem)
        
        # Teams
        if config.INTEGRACOES['teams']['habilitado']:
            resultados['teams'] = self.teams.enviar_mensagem(mensagem)
        
        self.logger.info(f"Notificação enviada para {sum(resultados.values())} canais")
        return resultados
    
    def enviar_relatorio_completo(self, relatorio: Dict[str, Any]):
        """Envia relatório completo para todos os canais"""
        mensagem = f"""
        📊 RELATÓRIO DO AGENTE DE IA
        
        📅 Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}
        
        📈 Estatísticas:
        • Processamentos: {relatorio.get('total_processamentos', 0)}
        • Sucessos: {relatorio.get('sucessos', 0)}
        • Erros: {relatorio.get('erros', 0)}
        • Taxa de sucesso: {relatorio.get('taxa_sucesso', 0):.1f}%
        
        🔧 Agentes:
        • Vendas: {relatorio.get('vendas_processados', 0)} análises
        • Suporte: {relatorio.get('suporte_atendidos', 0)} atendimentos
        • Conteúdo: {relatorio.get('conteudos_gerados', 0)} criações
        
        ⚠️ Alertas: {relatorio.get('alertas', 0)}
        """
        
        return self.enviar_notificacao_global(mensagem, "relatorio")

# Instância global do gerenciador
gerenciador_integracoes = GerenciadorIntegracoes()
