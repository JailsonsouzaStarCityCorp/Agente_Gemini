"""
Teste do Sistema de Agentes de IA
"""
def testar_imports():
    """Testa se todos os imports estão funcionando"""
    print("🔍 Testando imports...")
    
    try:
        import google.generativeai as genai
        print("✅ google.generativeai")
    except ImportError as e:
        print(f"❌ google.generativeai: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ pandas")
    except ImportError as e:
        print(f"❌ pandas: {e}")
        return False
    
    try:
        import schedule
        print("✅ schedule")
    except ImportError as e:
        print(f"❌ schedule: {e}")
        return False
    
    return True

def testar_configuracao():
    """Testa se a configuração está funcionando"""
    print("\n⚙️ Testando configuração...")
    
    try:
        from config import GEMINI_API_KEY, GEMINI_MODEL
        print(f"✅ API Key configurada: {GEMINI_API_KEY[:10]}...")
        print(f"✅ Modelo: {GEMINI_MODEL}")
        return True
    except Exception as e:
        print(f"❌ Erro na configuração: {e}")
        return False

def testar_agentes():
    """Testa se os agentes estão funcionando"""
    print("\n🤖 Testando agentes...")
    
    try:
        from agente_suporte import AgenteSuporte
        agente_suporte = AgenteSuporte()
        print("✅ Agente de Suporte carregado")
    except Exception as e:
        print(f"❌ Erro no Agente de Suporte: {e}")
        return False
    
    try:
        from agente_conteudo import AgenteConteudo
        agente_conteudo = AgenteConteudo()
        print("✅ Agente de Conteúdo carregado")
    except Exception as e:
        print(f"❌ Erro no Agente de Conteúdo: {e}")
        return False
    
    try:
        from agente_vendas import AgenteAnaliseVendas
        agente_vendas = AgenteAnaliseVendas()
        print("✅ Agente de Vendas carregado")
    except Exception as e:
        print(f"❌ Erro no Agente de Vendas: {e}")
        return False
    
    return True

def testar_agente_suporte():
    """Testa o agente de suporte com uma pergunta real"""
    print("\n🎧 Testando Agente de Suporte...")
    
    try:
        from agente_suporte import AgenteSuporte
        agente = AgenteSuporte()
        
        resultado = agente.processar_solicitacao("Como faço um pedido?")
        
        if resultado.get("sucesso"):
            dados = resultado["dados"]
            print("✅ Agente de Suporte funcionando!")
            print(f"📝 Resposta: {dados['resposta'][:100]}...")
            print(f"⚡ Urgência: {dados['urgencia']}")
            return True
        else:
            print(f"❌ Erro no processamento: {resultado.get('erro')}")
            return False
            
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        return False

def testar_agente_conteudo():
    """Testa o agente de conteúdo"""
    print("\n✍️ Testando Agente de Conteúdo...")
    
    try:
        from agente_conteudo import AgenteConteudo
        agente = AgenteConteudo()
        
        post = agente.gerar_post_social(
            tema="Teste do sistema",
            plataforma="Instagram",
            tom="profissional"
        )
        
        print("✅ Agente de Conteúdo funcionando!")
        print(f"📱 Post gerado: {post[:100]}...")
        return True
        
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        return False

def main():
    """Função principal de teste"""
    print("🧪 TESTE DO SISTEMA DE AGENTES DE IA")
    print("=" * 50)
    
    testes = [
        ("Imports", testar_imports),
        ("Configuração", testar_configuracao),
        ("Agentes", testar_agentes),
        ("Agente de Suporte", testar_agente_suporte),
        ("Agente de Conteúdo", testar_agente_conteudo)
    ]
    
    resultados = []
    
    for nome, teste in testes:
        try:
            resultado = teste()
            resultados.append((nome, resultado))
        except Exception as e:
            print(f"❌ Erro no teste {nome}: {e}")
            resultados.append((nome, False))
    
    # Resumo dos resultados
    print("\n" + "=" * 50)
    print("📊 RESUMO DOS TESTES")
    print("=" * 50)
    
    sucessos = 0
    for nome, resultado in resultados:
        status = "✅ PASSOU" if resultado else "❌ FALHOU"
        print(f"{nome}: {status}")
        if resultado:
            sucessos += 1
    
    print(f"\n🎯 Resultado: {sucessos}/{len(resultados)} testes passaram")
    
    if sucessos == len(resultados):
        print("🎉 SISTEMA 100% FUNCIONAL!")
        print("🚀 Execute 'python main.py' para usar o sistema completo")
    else:
        print("⚠️ Alguns testes falharam. Verifique os erros acima.")
    
    return sucessos == len(resultados)

if __name__ == "__main__":
    main()
