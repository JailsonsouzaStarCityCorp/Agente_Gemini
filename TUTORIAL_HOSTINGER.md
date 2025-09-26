# 🌐 Tutorial Completo: Como Rodar no Hostinger

## 📋 **PRÉ-REQUISITOS**

### **✅ O que você precisa:**
- ✅ Conta no Hostinger com hospedagem Python
- ✅ Domínio configurado
- ✅ Arquivo `agente_deploy.zip` (já criado)

---

## 🚀 **PASSO A PASSO DETALHADO**

### **PASSO 1: Acessar o Painel do Hostinger**

1. **Acesse:** https://www.hostinger.com.br
2. **Faça login** na sua conta
3. **Clique** em "Painel de Controle" ou "hPanel"

### **PASSO 2: Configurar Python**

1. **No painel:** Procure por "Python" ou "Aplicações Python"
2. **Clique** em "Python"
3. **Selecione** seu domínio
4. **Configure:**
   - **Versão Python:** 3.8 ou superior
   - **Arquivo de entrada:** `wsgi.py`
   - **Pasta:** `public_html`
5. **Clique** em "Criar" ou "Salvar"

### **PASSO 3: Upload dos Arquivos**

#### **Método 1: Via Gerenciador de Arquivos**
1. **No painel:** Vá para "Gerenciador de Arquivos"
2. **Navegue** até a pasta `public_html`
3. **Clique** em "Upload"
4. **Selecione** o arquivo `agente_deploy.zip`
5. **Aguarde** o upload terminar
6. **Clique** com botão direito no arquivo ZIP
7. **Selecione** "Extrair" ou "Unzip"
8. **Confirme** a extração

#### **Método 2: Via FileZilla (FTP)**
1. **Baixe** o FileZilla
2. **Configure** com dados do Hostinger:
   - **Host:** ftp.seudominio.com
   - **Usuário:** seu_usuario
   - **Senha:** sua_senha
3. **Conecte** ao servidor
4. **Navegue** até `public_html`
5. **Faça upload** do `agente_deploy.zip`
6. **Extraia** o arquivo

### **PASSO 4: Configurar Variáveis de Ambiente**

1. **No painel:** Vá para "Variáveis de Ambiente"
2. **Clique** em "Adicionar Nova Variável"
3. **Adicione** as seguintes variáveis:

```
SECRET_KEY=sua_chave_secreta_muito_segura_123456789
GEMINI_API_KEY=AIzaSyBxEyDUMNA746H9kblcBCxtw8u8vDstvr8
OPENAI_API_KEY=sua_chave_openai_se_tiver
DATABASE_URL=sqlite:///agente_prod.db
FLASK_ENV=production
DEBUG=False
```

4. **Clique** em "Salvar" para cada variável

### **PASSO 5: Instalar Dependências**

1. **No painel:** Vá para "Terminal" ou "SSH"
2. **Execute** os comandos:
```bash
cd public_html
pip install -r requirements.txt
```

### **PASSO 6: Configurar Permissões**

1. **No Gerenciador de Arquivos:**
2. **Selecione** a pasta `uploads`
3. **Clique** com botão direito
4. **Selecione** "Permissões"
5. **Defina** como 755 ou 777
6. **Salve** as permissões

### **PASSO 7: Testar a Aplicação**

1. **Acesse:** https://seudominio.com
2. **Verifique** se a página carrega
3. **Teste** as funcionalidades:
   - Chat de suporte
   - Criação de conteúdo
   - Upload de arquivos
   - Dashboard

---

## 🔧 **CONFIGURAÇÕES ESPECÍFICAS DO HOSTINGER**

### **📄 Configuração do .htaccess**
O arquivo `.htaccess` já está incluído no pacote, mas verifique se contém:

```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ wsgi.py/$1 [QSA,L]

Header always set X-Content-Type-Options nosniff
Header always set X-Frame-Options DENY
Header always set X-XSS-Protection "1; mode=block"
```

### **🐍 Configuração do wsgi.py**
O arquivo `wsgi.py` já está configurado corretamente:

```python
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from app import app as application

if __name__ == "__main__":
    application.run()
```

### **⚙️ Configuração do Python**
No painel do Hostinger:
- **Versão:** Python 3.8 ou superior
- **Arquivo de entrada:** `wsgi.py`
- **Pasta:** `public_html`

---

## 🛠️ **SOLUÇÃO DE PROBLEMAS COMUNS**

### **❌ Erro 500 - Internal Server Error**

**Possíveis causas:**
1. Python não configurado
2. Arquivo `wsgi.py` não encontrado
3. Dependências não instaladas

**Soluções:**
1. Verifique se o Python está configurado
2. Confirme se `wsgi.py` é o arquivo de entrada
3. Execute: `pip install -r requirements.txt`

### **❌ Erro 404 - Page Not Found**

**Possíveis causas:**
1. Arquivos não extraídos
2. `.htaccess` não configurado
3. Estrutura de pastas incorreta

**Soluções:**
1. Extraia todos os arquivos do ZIP
2. Verifique se `.htaccess` está presente
3. Confirme a estrutura de pastas

### **❌ Erro de Importação**

**Possíveis causas:**
1. Módulos não instalados
2. Versão Python incompatível
3. Caminhos incorretos

**Soluções:**
1. Instale as dependências: `pip install -r requirements.txt`
2. Use Python 3.8 ou superior
3. Verifique os imports no código

### **❌ Erro de Permissão**

**Possíveis causas:**
1. Pasta `uploads` sem permissão
2. Arquivos com permissão incorreta

**Soluções:**
1. Defina permissão 755 para `uploads`
2. Verifique permissões dos arquivos

---

## 📞 **SUPORTE DO HOSTINGER**

### **🆘 Quando pedir ajuda:**
- Erro 500 persistente
- Problemas de configuração Python
- Erros de permissão
- Problemas de domínio

### **📧 Como contatar:**
1. **Chat online** no painel
2. **Ticket de suporte**
3. **Documentação** do Hostinger
4. **Fórum** da comunidade

---

## ✅ **CHECKLIST FINAL**

### **Antes de testar:**
- [ ] Python configurado (3.8+)
- [ ] Arquivo de entrada: `wsgi.py`
- [ ] Arquivos extraídos em `public_html`
- [ ] Variáveis de ambiente configuradas
- [ ] Dependências instaladas
- [ ] Permissões da pasta `uploads` configuradas

### **Teste de funcionalidades:**
- [ ] Página inicial carrega
- [ ] Chat de suporte funciona
- [ ] Criação de conteúdo funciona
- [ ] Upload de arquivos funciona
- [ ] Dashboard carrega
- [ ] Configurações acessíveis

---

## 🎯 **RESULTADO ESPERADO**

### **✅ Após seguir todos os passos:**
- **URL:** https://seudominio.com
- **Interface:** Carregando normalmente
- **Funcionalidades:** Todas operacionais
- **Performance:** Rápida e responsiva

### **🎉 Seu agente de IA estará online e acessível para:**
- Atendimento 24/7
- Criação de conteúdo
- Análise de dados
- Monitoramento em tempo real

---

## 🚀 **PRÓXIMOS PASSOS**

### **1. Personalizar:**
- Adicionar seu domínio
- Configurar APIs
- Personalizar interface

### **2. Otimizar:**
- Configurar SSL
- Otimizar performance
- Configurar backup

### **3. Expandir:**
- Adicionar funcionalidades
- Integrar mais APIs
- Implementar autenticação

---

**🎉 PARABÉNS! Seu agente de IA estará rodando no Hostinger!**

**🌐 Acesse: https://seudominio.com**

**✨ Desfrute de todas as funcionalidades online! ✨**
