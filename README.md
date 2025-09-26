# 🤖 Sistema de Agentes de IA - Gemini

Sistema profissional de agentes de IA especializados usando Google Gemini para automação de tarefas empresariais.

## 🚀 Funcionalidades

### 📊 Agente de Análise de Vendas
- Processamento automático de planilhas Excel
- Geração de insights inteligentes
- Análise de tendências e performance
- Relatórios estruturados

### 🎧 Agente de Suporte ao Cliente
- Respostas automáticas baseadas em FAQ
- Classificação de urgência
- Base de conhecimento integrada
- Histórico de atendimentos

### ✍️ Agente de Criação de Conteúdo
- Posts para redes sociais (Instagram, LinkedIn, Twitter, Facebook)
- Newsletters personalizadas
- Campanhas completas multi-plataforma
- Adaptação por público-alvo

### ⚙️ Agente Automatizado
- Execução programada de tarefas
- Monitoramento de pastas
- Processamento automático de arquivos
- Logs detalhados de atividades

## 📦 Instalação

1. **Clone ou baixe o projeto**
2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure a API Key do Gemini:**
   - Edite o arquivo `config.py`
   - Substitua a API key pela sua chave do Google AI Studio

## 🎯 Como Usar

### Execução Principal
```bash
python main.py
```

### Uso Individual dos Agentes

#### Agente de Vendas
```python
from agente_vendas import AgenteAnaliseVendas

agente = AgenteAnaliseVendas()
resultado = agente.executar_analise("vendas.xlsx")
print(resultado["dados"]["insights"])
```

#### Agente de Suporte
```python
from agente_suporte import AgenteSuporte

agente = AgenteSuporte()
resultado = agente.processar_solicitacao("Como faço um pedido?")
print(resultado["dados"]["resposta"])
```

#### Agente de Conteúdo
```python
from agente_conteudo import AgenteConteudo

agente = AgenteConteudo()
post = agente.gerar_post_social("Lançamento", "Instagram", "empolgante")
print(post)
```

## 📁 Estrutura do Projeto

```
agente-gemini/
├── main.py                 # Interface principal
├── config.py              # Configurações
├── utils.py               # Utilitários
├── agente_vendas.py       # Agente de vendas
├── agente_suporte.py      # Agente de suporte
├── agente_conteudo.py     # Agente de conteúdo
├── agente_automatizado.py # Agente automatizado
├── requirements.txt       # Dependências
├── README.md             # Documentação
├── data/                 # Pasta para arquivos de entrada
├── reports/              # Pasta para relatórios gerados
└── logs/                 # Pasta para logs do sistema
```

## ⚙️ Configurações

### Horários de Execução Automática
Edite `config.py` para alterar os horários:
```python
SCHEDULE_HOURS = [9, 15, 21]  # 9h, 15h, 21h
```

### Logs
Os logs são salvos em `logs/agente.log` com diferentes níveis:
- INFO: Operações normais
- ERROR: Erros e falhas
- DEBUG: Informações detalhadas

## 🔧 Personalização

### Base de Conhecimento (Suporte)
Edite a função `carregar_base_conhecimento()` em `agente_suporte.py` para incluir:
- Produtos da sua empresa
- FAQ específico
- Contatos de suporte

### Diretrizes de Conteúdo
Modifique as diretrizes em `agente_conteudo.py` para adaptar:
- Tom da marca
- Estrutura de posts
- Público-alvo específico

## 📊 Relatórios

Todos os agentes geram relatórios em JSON na pasta `reports/`:
- `analise_vendas_YYYYMMDD_HHMMSS.json`
- `suporte_YYYYMMDD_HHMMSS.json`
- `campanha_YYYYMMDD_HHMMSS.json`
- `rotina_automatica_YYYYMMDD_HHMMSS.json`

## 🛡️ Segurança

- API Key configurada via variável de ambiente
- Tratamento de erros em todas as operações
- Logs detalhados para auditoria
- Validação de entrada de dados

## 🚨 Solução de Problemas

### Erro de API Key
```
Erro: Invalid API key
```
**Solução:** Verifique se a API key está correta em `config.py`

### Erro de Dependências
```
ModuleNotFoundError: No module named 'google.generativeai'
```
**Solução:** Execute `pip install -r requirements.txt`

### Erro de Arquivo
```
FileNotFoundError: vendas.xlsx
```
**Solução:** Verifique se o arquivo existe e o caminho está correto

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique os logs em `logs/agente.log`
2. Consulte a documentação do Google Gemini AI
3. Verifique as configurações em `config.py`

## 📄 Licença

Este projeto é de uso livre para fins educacionais e comerciais.

---

**Desenvolvido com ❤️ usando Google Gemini AI**
