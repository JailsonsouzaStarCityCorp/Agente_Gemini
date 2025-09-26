# 🚀 Guia Rápido - Deploy no Hostinger

## ⚡ **DEPLOY EM 5 PASSOS**

### **1. 📦 Arquivo Pronto:**
✅ **Arquivo criado:** `agente_deploy.zip`
✅ **Localização:** `c:\Users\DJ City\Documents\agente gemini\agente_deploy.zip`

### **2. 📤 Upload para Hostinger:**
1. **Acesse:** Painel do Hostinger
2. **Vá para:** Gerenciador de Arquivos
3. **Navegue até:** `public_html`
4. **Faça upload:** `agente_deploy.zip`
5. **Extraia** o arquivo na pasta `public_html`

### **3. ⚙️ Configurar Python:**
1. **No painel:** Vá para "Python"
2. **Versão:** Selecione Python 3.8+
3. **Arquivo de entrada:** `wsgi.py`
4. **Salve** as configurações

### **4. 🔐 Variáveis de Ambiente:**
No painel do Hostinger, adicione:
```
SECRET_KEY=sua_chave_secreta_super_segura
GEMINI_API_KEY=sua_chave_gemini
OPENAI_API_KEY=sua_chave_openai
DATABASE_URL=sqlite:///agente_prod.db
```

### **5. 🌐 Testar:**
- **Acesse:** https://seudominio.com
- **Teste:** Todas as funcionalidades
- **Verifique:** Se está funcionando

---

## 🎯 **RESULTADO FINAL**

**✅ Seu agente de IA estará online!**

**🌐 URL:** https://seudominio.com

**🎉 Funcionalidades disponíveis:**
- Chat com IA
- Criação de conteúdo
- Análise de vendas
- Dashboard
- Configurações

---

## 🆘 **SOLUÇÃO RÁPIDA DE PROBLEMAS**

### **❌ Erro 500:**
- Verifique se o Python está configurado
- Confirme se `wsgi.py` é o arquivo de entrada
- Verifique os logs de erro

### **❌ Erro de Importação:**
- Confirme se todos os arquivos foram enviados
- Verifique se o Python está na versão 3.8+

### **❌ Erro de Permissão:**
- Verifique se a pasta `uploads` tem permissão de escrita
- Confirme as permissões dos arquivos

---

## 📞 **SUPORTE**

- **Documentação:** `DEPLOY_HOSTINGER.md`
- **Instruções:** `INSTRUCOES_DEPLOY.txt`
- **Suporte Hostinger:** Painel de controle

---

**🎉 PRONTO! Seu agente de IA estará online em minutos!**
