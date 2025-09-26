"""
Sistema de Agentes de IA - Interface Principal
"""
import sys
import logging
from pathlib import Path
from utils import setup_logging
from agente_vendas import AgenteAnaliseVendas
from agente_suporte import AgenteSuporte
from agente_conteudo import AgenteConteudo
from agente_automatizado import AgenteAutomatizado

def menu_principal():
    """Menu principal do sistema"""
    print("\n" + "="*60)
    print("🤖 SISTEMA DE AGENTES DE IA - GEMINI")
    print("="*60)
    print("1. 📊 Agente de Análise de Vendas")
    print("2. 🎧 Agente de Suporte ao Cliente")
    print("3. ✍️  Agente de Criação de Conteúdo")
    print("4. ⚙️  Agente Automatizado")
    print("5. ⚙️  Configurador Avançado")
    print("6. 📈 Dashboard e Estatísticas")
    print("7. 🧪 Teste de Integrações")
    print("8. ❌ Sair")
    print("="*60)
    
    return input("Escolha uma opção (1-8): ").strip()

def executar_agente_vendas():
    """Interface para o agente de vendas"""
    print("\n📊 AGENTE DE ANÁLISE DE VENDAS")
    print("-" * 40)
    
    arquivo = input("Digite o caminho do arquivo Excel: ").strip()
    if not arquivo:
        print("❌ Caminho do arquivo é obrigatório!")
        return
    
    agente = AgenteAnaliseVendas()
    resultado = agente.executar_analise(arquivo)
    
    if resultado.get("sucesso"):
        print("\n✅ Análise concluída com sucesso!")
        print(f"📄 Arquivo processado: {arquivo}")
        print(f"📊 Insights gerados:")
        print("-" * 40)
        print(resultado["dados"]["insights"])
    else:
        print(f"❌ Erro na análise: {resultado.get('erro', 'Erro desconhecido')}")

def executar_agente_suporte():
    """Interface para o agente de suporte"""
    print("\n🎧 AGENTE DE SUPORTE AO CLIENTE")
    print("-" * 40)
    
    pergunta = input("Digite a pergunta do cliente: ").strip()
    if not pergunta:
        print("❌ Pergunta é obrigatória!")
        return
    
    agente = AgenteSuporte()
    resultado = agente.processar_solicitacao(pergunta)
    
    if resultado.get("sucesso"):
        dados = resultado["dados"]
        print(f"\n✅ Resposta gerada (Urgência: {dados['urgencia']})")
        print("-" * 40)
        print(dados["resposta"])
    else:
        print(f"❌ Erro no processamento: {resultado.get('erro', 'Erro desconhecido')}")

def executar_agente_conteudo():
    """Interface para o agente de conteúdo"""
    print("\n✍️  AGENTE DE CRIAÇÃO DE CONTEÚDO")
    print("-" * 40)
    print("1. Gerar post para rede social")
    print("2. Criar newsletter")
    print("3. Gerar campanha completa")
    
    opcao = input("Escolha uma opção (1-3): ").strip()
    
    agente = AgenteConteudo()
    
    if opcao == "1":
        tema = input("Tema do post: ").strip()
        plataforma = input("Plataforma (Instagram/LinkedIn/Twitter/Facebook): ").strip()
        tom = input("Tom (profissional/descontraído/empolgante): ").strip()
        
        if tema and plataforma and tom:
            post = agente.gerar_post_social(tema, plataforma, tom)
            print(f"\n✅ Post gerado para {plataforma}:")
            print("-" * 40)
            print(post)
        else:
            print("❌ Todos os campos são obrigatórios!")
    
    elif opcao == "2":
        topicos = input("Tópicos (separados por vírgula): ").strip().split(",")
        publico = input("Público-alvo: ").strip()
        
        if topicos and publico:
            newsletter = agente.criar_newsletter([t.strip() for t in topicos], publico)
            print(f"\n✅ Newsletter criada:")
            print("-" * 40)
            print(newsletter)
        else:
            print("❌ Tópicos e público-alvo são obrigatórios!")
    
    elif opcao == "3":
        tema = input("Tema da campanha: ").strip()
        plataformas = input("Plataformas (separadas por vírgula): ").strip().split(",")
        publico = input("Público-alvo: ").strip()
        
        if tema and plataformas and publico:
            resultado = agente.gerar_campanha_completa(tema, [p.strip() for p in plataformas], publico)
            if resultado.get("sucesso"):
                print(f"\n✅ Campanha completa gerada!")
                print(f"📄 Arquivo salvo em: reports/")
            else:
                print(f"❌ Erro na campanha: {resultado.get('erro')}")
        else:
            print("❌ Todos os campos são obrigatórios!")
    
    else:
        print("❌ Opção inválida!")

def executar_agente_automatizado():
    """Interface para o agente automatizado"""
    print("\n⚙️  AGENTE AUTOMATIZADO")
    print("-" * 40)
    print("1. Executar rotina manual")
    print("2. Iniciar agente em modo contínuo")
    print("3. Voltar ao menu principal")
    
    opcao = input("Escolha uma opção (1-3): ").strip()
    
    agente = AgenteAutomatizado()
    
    if opcao == "1":
        print("🔄 Executando rotina manual...")
        agente.executar_rotina_automatica()
        print("✅ Rotina executada!")
    
    elif opcao == "2":
        print("🚀 Iniciando agente em modo contínuo...")
        print("⚠️  Pressione Ctrl+C para parar")
        agente.iniciar_agente()
    
    elif opcao == "3":
        return
    
    else:
        print("❌ Opção inválida!")

def executar_configurador():
    """Executa o configurador avançado"""
    print("\n⚙️  CONFIGURADOR AVANÇADO")
    print("-" * 40)
    
    try:
        from configurador import ConfiguradorInterativo
        configurador = ConfiguradorInterativo()
        configurador.menu_principal()
    except ImportError as e:
        print(f"❌ Erro ao importar configurador: {str(e)}")
    except Exception as e:
        print(f"❌ Erro no configurador: {str(e)}")

def executar_dashboard():
    """Executa dashboard e estatísticas"""
    print("\n📈 DASHBOARD E ESTATÍSTICAS")
    print("-" * 40)
    
    try:
        from database import db_manager
        stats = db_manager.obter_estatisticas()
        
        print("📊 ESTATÍSTICAS DO SISTEMA")
        print("-" * 30)
        print(f"🔄 Processamentos: {stats.get('processamentos', {}).get('total', 0)}")
        print(f"✅ Sucessos: {stats.get('processamentos', {}).get('sucessos', 0)}")
        print(f"❌ Erros: {stats.get('processamentos', {}).get('erros', 0)}")
        print(f"📈 Taxa de sucesso: {stats.get('processamentos', {}).get('taxa_sucesso', 0):.1f}%")
        print(f"💰 Vendas: {stats.get('vendas', {}).get('total_vendas', 0)}")
        print(f"💵 Valor total: R$ {stats.get('vendas', {}).get('valor_total', 0):.2f}")
        print(f"🎧 Atendimentos: {stats.get('suporte', {}).get('total_atendimentos', 0)}")
        print(f"✍️ Conteúdos: {stats.get('conteudo', {}).get('total_conteudos', 0)}")
        
    except Exception as e:
        print(f"❌ Erro ao obter estatísticas: {str(e)}")

def executar_teste_integracoes():
    """Executa teste de integrações"""
    print("\n🧪 TESTE DE INTEGRAÇÕES")
    print("-" * 40)
    
    try:
        from integracoes import gerenciador_integracoes
        from datetime import datetime
        
        mensagem_teste = f"🧪 Teste do Agente de IA - {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        
        print("Enviando mensagem de teste para todos os canais...")
        resultados = gerenciador_integracoes.enviar_notificacao_global(mensagem_teste, "teste")
        
        print("\n📊 Resultados dos testes:")
        for canal, sucesso in resultados.items():
            status = "✅ Sucesso" if sucesso else "❌ Falhou"
            print(f"{canal.upper()}: {status}")
            
    except Exception as e:
        print(f"❌ Erro no teste de integrações: {str(e)}")

def main():
    """Função principal"""
    # Configurar logging
    logger = setup_logging()
    logger.info("Sistema de Agentes de IA iniciado")
    
    try:
        while True:
            opcao = menu_principal()
            
            if opcao == "1":
                executar_agente_vendas()
            elif opcao == "2":
                executar_agente_suporte()
            elif opcao == "3":
                executar_agente_conteudo()
            elif opcao == "4":
                executar_agente_automatizado()
            elif opcao == "5":
                executar_configurador()
            elif opcao == "6":
                executar_dashboard()
            elif opcao == "7":
                executar_teste_integracoes()
            elif opcao == "8":
                print("\n👋 Obrigado por usar o Sistema de Agentes de IA!")
                break
            else:
                print("❌ Opção inválida! Tente novamente.")
            
            input("\nPressione Enter para continuar...")
    
    except KeyboardInterrupt:
        print("\n\n👋 Sistema interrompido pelo usuário. Até logo!")
    except Exception as e:
        logger.error(f"Erro no sistema: {str(e)}")
        print(f"❌ Erro no sistema: {str(e)}")

if __name__ == "__main__":
    main()
