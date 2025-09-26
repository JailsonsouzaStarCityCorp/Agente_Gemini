"""
Exemplos de uso dos Agentes de IA
"""
import pandas as pd
from agente_vendas import AgenteAnaliseVendas
from agente_suporte import AgenteSuporte
from agente_conteudo import AgenteConteudo

def exemplo_agente_vendas():
    """Exemplo de uso do agente de vendas"""
    print("📊 EXEMPLO - Agente de Análise de Vendas")
    print("-" * 50)
    
    # Criar dados de exemplo
    dados_exemplo = {
        'data': pd.date_range('2024-01-01', periods=30, freq='D'),
        'produto': ['Produto A', 'Produto B', 'Produto C'] * 10,
        'valor_venda': [100, 150, 200] * 10,
        'vendedor': ['João', 'Maria', 'Pedro'] * 10
    }
    
    df = pd.DataFrame(dados_exemplo)
    arquivo_exemplo = 'data/vendas_exemplo.xlsx'
    df.to_excel(arquivo_exemplo, index=False)
    
    # Usar o agente
    agente = AgenteAnaliseVendas()
    resultado = agente.executar_analise(arquivo_exemplo)
    
    if resultado.get("sucesso"):
        print("✅ Análise concluída!")
        print(f"📈 Insights gerados:")
        print(resultado["dados"]["insights"])
    else:
        print(f"❌ Erro: {resultado.get('erro')}")

def exemplo_agente_suporte():
    """Exemplo de uso do agente de suporte"""
    print("\n🎧 EXEMPLO - Agente de Suporte")
    print("-" * 50)
    
    agente = AgenteSuporte()
    
    perguntas_exemplo = [
        "Como faço um pedido?",
        "Qual o prazo de entrega?",
        "Posso cancelar meu pedido?",
        "Meu produto chegou com defeito"
    ]
    
    for pergunta in perguntas_exemplo:
        print(f"\n❓ Pergunta: {pergunta}")
        resultado = agente.processar_solicitacao(pergunta)
        
        if resultado.get("sucesso"):
            dados = resultado["dados"]
            print(f"📝 Resposta ({dados['urgencia']}): {dados['resposta'][:100]}...")
        else:
            print(f"❌ Erro: {resultado.get('erro')}")

def exemplo_agente_conteudo():
    """Exemplo de uso do agente de conteúdo"""
    print("\n✍️ EXEMPLO - Agente de Conteúdo")
    print("-" * 50)
    
    agente = AgenteConteudo()
    
    # Exemplo 1: Post para Instagram
    print("\n📱 Post para Instagram:")
    post_insta = agente.gerar_post_social(
        tema="Lançamento do novo produto",
        plataforma="Instagram",
        tom="empolgante",
        publico_alvo="jovens de 18-35 anos"
    )
    print(post_insta)
    
    # Exemplo 2: Newsletter
    print("\n📧 Newsletter:")
    newsletter = agente.criar_newsletter(
        topicos=["Tendências do mercado", "Novos recursos", "Cases de sucesso"],
        publico_alvo="gestores de marketing",
        empresa="TechCorp"
    )
    print(newsletter[:200] + "...")

def exemplo_campanha_completa():
    """Exemplo de campanha completa"""
    print("\n🚀 EXEMPLO - Campanha Completa")
    print("-" * 50)
    
    agente = AgenteConteudo()
    
    resultado = agente.gerar_campanha_completa(
        tema="Black Friday 2024",
        plataformas=["Instagram", "LinkedIn", "Facebook"],
        publico_alvo="clientes ativos"
    )
    
    if resultado.get("sucesso"):
        print("✅ Campanha completa gerada!")
        print("📄 Arquivo salvo em: reports/")
        
        # Mostrar resumo
        dados = resultado["dados"]
        print(f"📊 Plataformas: {list(dados['plataformas'].keys())}")
        print(f"📝 Newsletter: {len(dados['newsletter'])} caracteres")
    else:
        print(f"❌ Erro: {resultado.get('erro')}")

if __name__ == "__main__":
    print("🤖 EXEMPLOS DE USO - Sistema de Agentes de IA")
    print("=" * 60)
    
    try:
        # Executar exemplos
        exemplo_agente_vendas()
        exemplo_agente_suporte()
        exemplo_agente_conteudo()
        exemplo_campanha_completa()
        
        print("\n✅ Todos os exemplos executados com sucesso!")
        print("📁 Verifique a pasta 'reports/' para ver os arquivos gerados")
        
    except Exception as e:
        print(f"❌ Erro na execução dos exemplos: {str(e)}")
        print("💡 Certifique-se de que todas as dependências estão instaladas")
