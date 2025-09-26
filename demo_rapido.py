"""
Demonstração Rápida do Sistema de Agentes de IA
Execute este arquivo para ver o sistema funcionando rapidamente
"""
import pandas as pd
from datetime import datetime, timedelta
import os

def criar_dados_exemplo():
    """Cria dados de exemplo para demonstração"""
    print("📊 Criando dados de exemplo...")
    
    # Dados de vendas
    dados_vendas = {
        'data': pd.date_range('2024-01-01', periods=30, freq='D'),
        'produto': ['Produto A', 'Produto B', 'Produto C'] * 10,
        'valor_venda': [100, 150, 200, 120, 180, 250, 90, 160, 220] * 3 + [100],
        'vendedor': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'] * 6,
        'regiao': ['Norte', 'Sul', 'Leste', 'Oeste'] * 7 + ['Norte', 'Sul']
    }
    
    df_vendas = pd.DataFrame(dados_vendas)
    df_vendas.to_excel('data/vendas_demo.xlsx', index=False)
    print("✅ Arquivo de vendas criado: data/vendas_demo.xlsx")
    
    return True

def demo_agente_vendas():
    """Demonstração do agente de vendas"""
    print("\n" + "="*50)
    print("📊 DEMONSTRAÇÃO - Agente de Análise de Vendas")
    print("="*50)
    
    try:
        from agente_vendas import AgenteAnaliseVendas
        
        agente = AgenteAnaliseVendas()
        resultado = agente.executar_analise('data/vendas_demo.xlsx')
        
        if resultado.get("sucesso"):
            print("✅ Análise concluída com sucesso!")
            print("\n📈 INSIGHTS GERADOS:")
            print("-" * 30)
            print(resultado["dados"]["insights"])
        else:
            print(f"❌ Erro: {resultado.get('erro')}")
            
    except Exception as e:
        print(f"❌ Erro na demonstração: {str(e)}")

def demo_agente_suporte():
    """Demonstração do agente de suporte"""
    print("\n" + "="*50)
    print("🎧 DEMONSTRAÇÃO - Agente de Suporte")
    print("="*50)
    
    try:
        from agente_suporte import AgenteSuporte
        
        agente = AgenteSuporte()
        
        perguntas_demo = [
            "Como faço um pedido?",
            "Qual o prazo de entrega?",
            "Posso cancelar meu pedido?"
        ]
        
        for i, pergunta in enumerate(perguntas_demo, 1):
            print(f"\n{i}. ❓ Pergunta: {pergunta}")
            resultado = agente.processar_solicitacao(pergunta)
            
            if resultado.get("sucesso"):
                dados = resultado["dados"]
                print(f"   📝 Resposta ({dados['urgencia']}): {dados['resposta'][:100]}...")
            else:
                print(f"   ❌ Erro: {resultado.get('erro')}")
                
    except Exception as e:
        print(f"❌ Erro na demonstração: {str(e)}")

def demo_agente_conteudo():
    """Demonstração do agente de conteúdo"""
    print("\n" + "="*50)
    print("✍️ DEMONSTRAÇÃO - Agente de Conteúdo")
    print("="*50)
    
    try:
        from agente_conteudo import AgenteConteudo
        
        agente = AgenteConteudo()
        
        # Post para Instagram
        print("\n📱 Post para Instagram:")
        post = agente.gerar_post_social(
            tema="Lançamento do novo produto",
            plataforma="Instagram",
            tom="empolgante",
            publico_alvo="jovens de 18-35 anos"
        )
        print(post)
        
        # Newsletter
        print("\n📧 Newsletter:")
        newsletter = agente.criar_newsletter(
            topicos=["Tendências do mercado", "Novos recursos"],
            publico_alvo="gestores de marketing"
        )
        print(newsletter[:200] + "...")
        
    except Exception as e:
        print(f"❌ Erro na demonstração: {str(e)}")

def verificar_estrutura():
    """Verifica se a estrutura do projeto está correta"""
    print("🔍 Verificando estrutura do projeto...")
    
    arquivos_necessarios = [
        'main.py', 'config.py', 'utils.py',
        'agente_vendas.py', 'agente_suporte.py',
        'agente_conteudo.py', 'agente_automatizado.py',
        'requirements.txt', 'README.md'
    ]
    
    diretorios_necessarios = ['data', 'reports', 'logs']
    
    # Verificar arquivos
    for arquivo in arquivos_necessarios:
        if os.path.exists(arquivo):
            print(f"✅ {arquivo}")
        else:
            print(f"❌ {arquivo} - FALTANDO")
    
    # Verificar diretórios
    for diretorio in diretorios_necessarios:
        if os.path.exists(diretorio):
            print(f"✅ {diretorio}/")
        else:
            print(f"❌ {diretorio}/ - FALTANDO")

def main():
    """Função principal da demonstração"""
    print("🚀 DEMONSTRAÇÃO RÁPIDA - Sistema de Agentes de IA")
    print("=" * 60)
    
    # Verificar estrutura
    verificar_estrutura()
    
    # Criar dados de exemplo
    if not os.path.exists('data/vendas_demo.xlsx'):
        criar_dados_exemplo()
    
    # Executar demonstrações
    demo_agente_vendas()
    demo_agente_suporte()
    demo_agente_conteudo()
    
    print("\n" + "="*60)
    print("🎉 DEMONSTRAÇÃO CONCLUÍDA!")
    print("="*60)
    print("📁 Verifique a pasta 'reports/' para ver os arquivos gerados")
    print("📚 Consulte o README.md para mais informações")
    print("🚀 Execute 'python main.py' para usar o sistema completo")

if __name__ == "__main__":
    main()
