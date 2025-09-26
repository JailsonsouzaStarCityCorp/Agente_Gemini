# 🚀 INSTRUÇÕES RÁPIDAS - Sistema de Agentes de IA

## ⚡ Início Rápido

### 1. Instalação
```bash
python instalar.py
```

### 2. Configuração da API Key
- Edite o arquivo `config.py`
- Substitua `SUA_API_KEY_AQUI` pela sua chave do Google Gemini
- Obtenha sua chave em: https://makersuite.google.com/app/apikey

### 3. Teste Rápido
```bash
python demo_rapido.py
```

### 4. Uso Completo
```bash
python main.py
```

## 📋 Menu Principal

Quando executar `main.py`, você terá as opções:

1. **📊 Agente de Análise de Vendas**
   - Processa planilhas Excel
   - Gera insights automáticos
   - Cria relatórios estruturados

2. **🎧 Agente de Suporte ao Cliente**
   - Responde perguntas automaticamente
   - Classifica urgência
   - Usa base de conhecimento

3. **✍️ Agente de Criação de Conteúdo**
   - Posts para redes sociais
   - Newsletters personalizadas
   - Campanhas completas

4. **⚙️ Agente Automatizado**
   - Execução programada
   - Monitoramento de pastas
   - Processamento automático

## 📁 Estrutura de Arquivos

```
agente-gemini/
├── main.py                 # 🎯 Interface principal
├── demo_rapido.py          # ⚡ Demonstração rápida
├── instalar.py             # 📦 Script de instalação
├── config.py               # ⚙️ Configurações
├── utils.py                # 🔧 Utilitários
├── agente_vendas.py        # 📊 Análise de vendas
├── agente_suporte.py       # 🎧 Suporte ao cliente
├── agente_conteudo.py      # ✍️ Criação de conteúdo
├── agente_automatizado.py  # ⚙️ Automação
├── exemplo_uso.py          # 📚 Exemplos de uso
├── requirements.txt        # 📦 Dependências
├── README.md              # 📖 Documentação completa
├── data/                  # 📊 Arquivos de entrada
├── reports/               # 📄 Relatórios gerados
└── logs/                  # 📝 Logs do sistema
```

## 🎯 Exemplos de Uso

### Análise de Vendas
```python
from agente_vendas import AgenteAnaliseVendas
agente = AgenteAnaliseVendas()
resultado = agente.executar_analise("vendas.xlsx")
```

### Suporte ao Cliente
```python
from agente_suporte import AgenteSuporte
agente = AgenteSuporte()
resultado = agente.processar_solicitacao("Como faço um pedido?")
```

### Criação de Conteúdo
```python
from agente_conteudo import AgenteConteudo
agente = AgenteConteudo()
post = agente.gerar_post_social("Lançamento", "Instagram", "empolgante")
```

## 🔧 Personalização

### Base de Conhecimento (Suporte)
Edite `agente_suporte.py` → função `carregar_base_conhecimento()`

### Horários de Execução
Edite `config.py` → `SCHEDULE_HOURS = [9, 15, 21]`

### Configurações de Log
Edite `config.py` → `LOG_LEVEL = 'INFO'`

## 🚨 Solução de Problemas

### Erro de API Key
```
Erro: Invalid API key
```
**Solução:** Configure sua API key em `config.py`

### Erro de Dependências
```
ModuleNotFoundError
```
**Solução:** Execute `pip install -r requirements.txt`

### Arquivo não encontrado
```
FileNotFoundError
```
**Solução:** Verifique se o arquivo existe e o caminho está correto

## 📞 Suporte

1. **Logs:** Verifique `logs/agente.log`
2. **Documentação:** Consulte `README.md`
3. **Exemplos:** Execute `exemplo_uso.py`
4. **Teste:** Execute `demo_rapido.py`

## 🎉 Pronto para Usar!

Seu sistema de agentes de IA está 100% funcional e profissional!

- ✅ Código otimizado e organizado
- ✅ Documentação completa
- ✅ Exemplos práticos
- ✅ Tratamento de erros
- ✅ Logs detalhados
- ✅ Interface amigável

**Execute `python main.py` e comece a usar!**
