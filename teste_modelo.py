"""
Teste do modelo Gemini corrigido
"""
import sys
sys.path.append('.')

def teste_modelo():
    print("🧪 Testando modelo Gemini corrigido...")
    
    try:
        from agente_suporte import AgenteSuporte
        agente = AgenteSuporte()
        
        resultado = agente.processar_solicitacao("Teste do sistema")
        
        if resultado.get("sucesso"):
            print("✅ Agente funcionando com modelo correto!")
            resposta = resultado["dados"]["resposta"]
            print("Resposta:", resposta[:100] + "...")
        else:
            print("❌ Erro no agente")
            print("Erro:", resultado.get("erro", "Desconhecido"))
            
    except Exception as e:
        print("❌ Erro no teste:", str(e))

if __name__ == "__main__":
    teste_modelo()
