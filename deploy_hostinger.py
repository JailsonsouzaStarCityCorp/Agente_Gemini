"""
Script para deploy automático no Hostinger
"""
import os
import shutil
import subprocess
from pathlib import Path

def criar_arquivos_producao():
    """Criar arquivos necessários para produção"""
    
    print("📁 Criando arquivos de produção...")
    
    # Verificar se wsgi.py já existe
    if not Path('wsgi.py').exists():
        print("❌ Arquivo wsgi.py não encontrado!")
        return False
    
    # Verificar se .htaccess já existe
    if not Path('.htaccess').exists():
        print("❌ Arquivo .htaccess não encontrado!")
        return False
    
    # Verificar se config_prod.py já existe
    if not Path('config_prod.py').exists():
        print("❌ Arquivo config_prod.py não encontrado!")
        return False
    
    print("✅ Arquivos de produção verificados")
    return True

def criar_zip_deploy():
    """Criar arquivo ZIP para upload"""
    
    print("📦 Criando arquivo de deploy...")
    
    # Arquivos a incluir
    arquivos_incluir = [
        'app.py',
        'wsgi.py',
        '.htaccess',
        'config_prod.py',
        'requirements.txt',
        'agente_suporte.py',
        'agente_conteudo.py',
        'agente_vendas.py',
        'agente_automatizado.py',
        'config.py',
        'database.py',
        'integracoes.py',
        'utils.py',
        'templates/',
        'static/',
        'uploads/'
    ]
    
    # Criar diretório de deploy
    deploy_dir = Path('deploy')
    if deploy_dir.exists():
        shutil.rmtree(deploy_dir)
    deploy_dir.mkdir(exist_ok=True)
    
    # Copiar arquivos
    for arquivo in arquivos_incluir:
        src = Path(arquivo)
        dst = deploy_dir / arquivo
        
        if src.is_dir():
            if src.exists():
                shutil.copytree(src, dst, dirs_exist_ok=True)
                print(f"📁 Copiado diretório: {arquivo}")
        elif src.exists():
            shutil.copy2(src, dst)
            print(f"📄 Copiado arquivo: {arquivo}")
        else:
            print(f"⚠️  Arquivo não encontrado: {arquivo}")
    
    # Criar ZIP
    zip_name = 'agente_deploy'
    if Path(f'{zip_name}.zip').exists():
        os.remove(f'{zip_name}.zip')
    
    shutil.make_archive(zip_name, 'zip', deploy_dir)
    
    print(f"✅ Arquivo de deploy criado: {zip_name}.zip")
    return True

def verificar_estrutura():
    """Verificar se a estrutura está correta"""
    
    print("🔍 Verificando estrutura de arquivos...")
    
    arquivos_necessarios = [
        'app.py',
        'wsgi.py',
        '.htaccess',
        'config_prod.py',
        'requirements.txt',
        'templates/',
        'static/'
    ]
    
    arquivos_faltando = []
    for arquivo in arquivos_necessarios:
        if not Path(arquivo).exists():
            arquivos_faltando.append(arquivo)
    
    if arquivos_faltando:
        print("❌ Arquivos faltando:")
        for arquivo in arquivos_faltando:
            print(f"   - {arquivo}")
        return False
    
    print("✅ Estrutura verificada com sucesso")
    return True

def criar_instrucoes():
    """Criar arquivo de instruções"""
    
    instrucoes = """
# 🚀 INSTRUÇÕES DE DEPLOY NO HOSTINGER

## 📋 PASSOS PARA DEPLOY:

### 1. Upload dos Arquivos:
- Acesse o painel do Hostinger
- Vá para "Gerenciador de Arquivos"
- Navegue até a pasta `public_html`
- Faça upload do arquivo `agente_deploy.zip`
- Extraia o arquivo na pasta `public_html`

### 2. Configurar Variáveis de Ambiente:
- No painel do Hostinger, vá para "Variáveis de Ambiente"
- Adicione as seguintes variáveis:
  - SECRET_KEY: sua_chave_secreta_super_segura
  - GEMINI_API_KEY: sua_chave_gemini
  - OPENAI_API_KEY: sua_chave_openai
  - DATABASE_URL: sqlite:///agente_prod.db

### 3. Configurar Python:
- No painel do Hostinger, vá para "Python"
- Selecione a versão Python 3.8 ou superior
- Configure o arquivo de entrada como `wsgi.py`

### 4. Testar Aplicação:
- Acesse seu domínio
- Teste todas as funcionalidades
- Verifique se está funcionando corretamente

## 🔧 SOLUÇÃO DE PROBLEMAS:

### Erro 500:
- Verifique os logs de erro
- Confirme se todas as dependências estão instaladas
- Verifique as variáveis de ambiente

### Erro de Importação:
- Confirme se todos os arquivos foram enviados
- Verifique se o Python está configurado corretamente

### Erro de Permissão:
- Verifique as permissões dos arquivos
- Confirme se o diretório uploads tem permissão de escrita

## 📞 SUPORTE:
- Consulte a documentação do Hostinger
- Entre em contato com o suporte técnico
- Verifique os logs de erro para mais detalhes
"""
    
    with open('INSTRUCOES_DEPLOY.txt', 'w', encoding='utf-8') as f:
        f.write(instrucoes)
    
    print("📄 Arquivo de instruções criado: INSTRUCOES_DEPLOY.txt")

def main():
    """Função principal"""
    print("🚀 PREPARANDO DEPLOY PARA HOSTINGER")
    print("="*50)
    
    # Verificar estrutura
    if not verificar_estrutura():
        print("\n❌ Estrutura de arquivos incompleta!")
        print("   Certifique-se de que todos os arquivos estão presentes.")
        return
    
    # Verificar arquivos de produção
    if not criar_arquivos_producao():
        print("\n❌ Erro ao verificar arquivos de produção!")
        return
    
    # Criar ZIP de deploy
    if not criar_zip_deploy():
        print("\n❌ Erro ao criar arquivo de deploy!")
        return
    
    # Criar instruções
    criar_instrucoes()
    
    print("\n" + "="*50)
    print("✅ DEPLOY PREPARADO COM SUCESSO!")
    print("="*50)
    print("\n📋 PRÓXIMOS PASSOS:")
    print("1. 📤 Faça upload do arquivo 'agente_deploy.zip' para o Hostinger")
    print("2. 📁 Extraia o arquivo na pasta public_html")
    print("3. ⚙️  Configure as variáveis de ambiente no painel do Hostinger")
    print("4. 🐍 Configure o Python para usar wsgi.py")
    print("5. 🌐 Acesse seu domínio para testar")
    print("\n📄 Consulte o arquivo 'INSTRUCOES_DEPLOY.txt' para detalhes")
    print("\n🎉 Seu agente de IA estará online em breve!")

if __name__ == "__main__":
    main()
