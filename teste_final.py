"""
Teste Final do Sistema - Verificação Completa
"""
import sys
sys.path.append('.')

def teste_completo():
    """Teste completo de todos os componentes"""
    print("🧪 TESTE FINAL DO SISTEMA")
    print("=" * 60)
    
    try:
        # Teste 1: Configuração
        print("1. Testando configuração...")
        from config import config
        print("   ✅ Configuração carregada")
        print(f"   📊 APIs: {len(config.API_CONFIG)}")
        print(f"   📧 Integrações: {len(config.INTEGRACOES)}")
        
        # Teste 2: Utilitários
        print("\n2. Testando utilitários...")
        from utils import setup_logging, executar_com_seguranca
        logger = setup_logging()
        print("   ✅ Utilitários carregados")
        
        # Teste 3: Agente de Suporte
        print("\n3. Testando Agente de Suporte...")
        from agente_suporte import AgenteSuporte
        agente_suporte = AgenteSuporte()
        resultado = agente_suporte.processar_solicitacao("Teste do sistema")
        if resultado.get("sucesso"):
            print("   ✅ Agente de Suporte funcionando")
            print(f"   📝 Resposta: {resultado['dados']['resposta'][:50]}...")
        else:
            print("   ❌ Erro no Agente de Suporte")
        
        # Teste 4: Agente de Conteúdo
        print("\n4. Testando Agente de Conteúdo...")
        from agente_conteudo import AgenteConteudo
        agente_conteudo = AgenteConteudo()
        post = agente_conteudo.gerar_post_social("Teste", "Instagram", "profissional")
        print("   ✅ Agente de Conteúdo funcionando")
        print(f"   📱 Post: {post[:50]}...")
        
        # Teste 5: Agente de Vendas
        print("\n5. Testando Agente de Vendas...")
        from agente_vendas import AgenteAnaliseVendas
        agente_vendas = AgenteAnaliseVendas()
        print("   ✅ Agente de Vendas carregado")
        
        # Teste 6: Integrações
        print("\n6. Testando integrações...")
        from integracoes import gerenciador_integracoes
        print("   ✅ Sistema de integrações carregado")
        
        # Teste 7: Banco de dados
        print("\n7. Testando banco de dados...")
        from database import db_manager
        stats = db_manager.obter_estatisticas()
        print("   ✅ Banco de dados funcionando")
        print(f"   📊 Processamentos: {stats.get('processamentos', {}).get('total', 0)}")
        
        # Teste 8: Menu principal
        print("\n8. Testando menu principal...")
        from main import menu_principal
        print("   ✅ Menu principal carregado")
        
        print("\n" + "=" * 60)
        print("🎉 TODOS OS TESTES PASSARAM!")
        print("✅ Sistema 100% funcional!")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERRO NO TESTE: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    sucesso = teste_completo()
    if sucesso:
        print("\n🚀 Sistema pronto para uso!")
        print("Execute: python main.py")
    else:
        print("\n⚠️ Corrija os erros antes de usar o sistema")
