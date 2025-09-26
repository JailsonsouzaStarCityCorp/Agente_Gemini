# ⚙️ Configurações Avançadas do Agente de IA

## 🎯 Visão Geral

O sistema agora possui um sistema de configuração extremamente robusto com **mais de 50 opções de integração e personalização**. Todas as configurações são gerenciadas centralmente e podem ser modificadas via interface interativa.

## 🔧 Sistema de Configuração

### 📋 Estrutura de Configurações

```
config.py
├── API_CONFIG (APIs de IA)
├── INTEGRACOES (Comunicação)
├── DATABASE_CONFIG (Bancos de dados)
├── LOGGING_CONFIG (Sistema de logs)
├── SCHEDULE_CONFIG (Agendamento)
├── SECURITY_CONFIG (Segurança)
├── PERFORMANCE_CONFIG (Performance)
├── AGENTE_CONFIG (Configurações por agente)
├── NOTIFICACOES (Sistema de notificações)
└── ANALISE_CONFIG (Análise avançada)
```

## 🔑 Configurações de API

### 🤖 Múltiplas APIs de IA Suportadas

```python
API_CONFIG = {
    'gemini': {
        'api_key': 'sua_chave_gemini',
        'model': 'gemini-1.5-flash',
        'temperature': 0.7,
        'max_tokens': 2048,
        'timeout': 30
    },
    'openai': {
        'api_key': 'sua_chave_openai',
        'model': 'gpt-4',
        'temperature': 0.7,
        'max_tokens': 2048
    },
    'claude': {
        'api_key': 'sua_chave_claude',
        'model': 'claude-3-sonnet-20240229',
        'temperature': 0.7,
        'max_tokens': 2048
    }
}
```

## 📧 Integrações de Comunicação

### 🌐 Canais Suportados

1. **Email (SMTP)**
   - Gmail, Outlook, servidores customizados
   - Relatórios automáticos
   - Alertas de erro

2. **WhatsApp Business API**
   - Mensagens automáticas
   - Notificações de status
   - Suporte ao cliente

3. **Telegram Bot**
   - Notificações em tempo real
   - Comandos personalizados
   - Grupos e canais

4. **Slack**
   - Webhooks personalizados
   - Canais específicos
   - Integração com workflows

5. **Discord**
   - Bots personalizados
   - Canais de notificação
   - Comandos slash

6. **Microsoft Teams**
   - Webhooks de notificação
   - Cards interativos
   - Integração empresarial

### 🔧 Configuração de Integrações

```python
# Exemplo: Configurar WhatsApp
INTEGRACOES = {
    'whatsapp': {
        'api_key': 'seu_token_whatsapp',
        'numero_telefone': '+5511999999999',
        'webhook_url': 'https://seu-webhook.com',
        'habilitado': True
    }
}
```

## 🗄️ Configurações de Banco de Dados

### 📊 Bancos Suportados

1. **SQLite** (Padrão)
   - Arquivo local
   - Zero configuração
   - Ideal para desenvolvimento

2. **PostgreSQL**
   - Produção
   - Alta performance
   - Suporte a JSON

3. **MySQL**
   - Compatibilidade
   - Replicação
   - Backup automático

4. **MongoDB**
   - Documentos flexíveis
   - Escalabilidade
   - Agregações avançadas

### 🔧 Configuração de Banco

```python
DATABASE_CONFIG = {
    'postgresql': {
        'host': 'localhost',
        'port': 5432,
        'database': 'agente',
        'usuario': 'usuario',
        'senha': 'senha',
        'habilitado': True
    }
}
```

## 🔒 Configurações de Segurança

### 🛡️ Recursos de Segurança

- **Rate Limiting**: Controle de requisições por hora
- **Validação de Arquivos**: Extensões e tamanhos permitidos
- **Criptografia**: Chaves de criptografia para dados sensíveis
- **Timeout de Sessão**: Controle de tempo de sessão
- **Backup Automático**: Retenção de dados configurável

```python
SECURITY_CONFIG = {
    'api_rate_limit': 100,  # requests/hora
    'max_file_size': 50 * 1024 * 1024,  # 50MB
    'allowed_extensions': ['.xlsx', '.csv', '.json', '.txt', '.pdf'],
    'encryption_key': 'sua_chave_criptografia',
    'session_timeout': 3600,  # 1 hora
    'backup_retention_days': 30
}
```

## ⚡ Configurações de Performance

### 🚀 Otimizações Disponíveis

- **Workers Paralelos**: Processamento simultâneo
- **Cache Inteligente**: Redução de requisições
- **Limite de Memória**: Controle de recursos
- **Timeout de Requisições**: Prevenção de travamentos

```python
PERFORMANCE_CONFIG = {
    'max_workers': 4,
    'cache_size': 1000,
    'cache_ttl': 3600,  # 1 hora
    'memory_limit': 512 * 1024 * 1024,  # 512MB
    'timeout_requests': 30,
    'habilitar_cache': True
}
```

## 🎯 Configurações por Agente

### 📊 Agente de Vendas
```python
'vendas': {
    'colunas_obrigatorias': ['data', 'valor_venda'],
    'formato_data': '%Y-%m-%d',
    'analise_automatica': True,
    'gerar_graficos': True,
    'tendencias_dias': 30
}
```

### 🎧 Agente de Suporte
```python
'suporte': {
    'urgencia_padrao': 'MÉDIA',
    'tempo_resposta_esperado': 30,
    'base_conhecimento_auto': True,
    'escalonamento_automatico': True,
    'idiomas_suportados': ['pt', 'en', 'es']
}
```

### ✍️ Agente de Conteúdo
```python
'conteudo': {
    'tamanho_max_post': 2200,
    'tamanho_max_newsletter': 500,
    'hashtags_max': 5,
    'templates_personalizados': True,
    'analise_sentimento': True
}
```

### ⚙️ Agente Automatizado
```python
'automatizado': {
    'monitoramento_pastas': True,
    'processamento_paralelo': True,
    'notificacoes_erro': True,
    'backup_automatico': True
}
```

## 📱 Sistema de Notificações

### 🔔 Tipos de Notificação

1. **Email**
   - Relatórios diários
   - Alertas de erro
   - Resumos semanais

2. **Webhook**
   - Eventos customizados
   - Integração com sistemas externos
   - Callbacks personalizados

3. **Push Notifications**
   - FCM (Firebase)
   - Notificações móveis
   - Alertas em tempo real

### 📊 Configuração de Notificações

```python
NOTIFICACOES = {
    'email': {
        'relatorios_diarios': True,
        'alertas_erro': True,
        'resumos_semanais': True
    },
    'webhook': {
        'url': 'https://seu-webhook.com',
        'eventos': ['erro', 'sucesso', 'conclusao'],
        'habilitado': True
    }
}
```

## 📈 Análise Avançada

### 🧠 Recursos de IA

1. **Análise de Sentimento**
   - Modelos em português/inglês
   - Confiança configurável
   - Classificação automática

2. **Classificação Inteligente**
   - Categorias personalizadas
   - Auto-classificação
   - Aprendizado contínuo

3. **Métricas Automáticas**
   - Coleta em tempo real
   - Retenção configurável
   - Dashboards dinâmicos

### 🔧 Configuração de Análise

```python
ANALISE_CONFIG = {
    'sentimento': {
        'habilitado': True,
        'modelo': 'portuguese',
        'confianca_minima': 0.7
    },
    'classificacao': {
        'habilitado': True,
        'categorias': ['vendas', 'suporte', 'marketing', 'financeiro'],
        'auto_classificar': True
    },
    'metricas': {
        'coleta_automatica': True,
        'intervalo_coleta': 3600,  # 1 hora
        'retencao_dados': 90  # dias
    }
}
```

## 🎛️ Configurador Interativo

### 🖥️ Interface de Configuração

Execute o configurador interativo:

```bash
python configurador.py
```

### 📋 Menu de Configuração

1. **🔑 Configurações de API**
   - Múltiplas APIs de IA
   - Chaves e modelos
   - Parâmetros de temperatura

2. **📧 Integrações de Comunicação**
   - Email, WhatsApp, Telegram
   - Slack, Discord, Teams
   - Configuração passo a passo

3. **🗄️ Configurações de Banco de Dados**
   - SQLite, PostgreSQL, MySQL, MongoDB
   - Conexões e credenciais
   - Migração de dados

4. **📊 Configurações de Análise**
   - Sentimento e classificação
   - Métricas automáticas
   - Modelos de IA

5. **🔒 Configurações de Segurança**
   - Rate limiting
   - Validação de arquivos
   - Criptografia

6. **⚡ Configurações de Performance**
   - Workers e cache
   - Limites de memória
   - Timeouts

7. **📱 Configurações de Notificações**
   - Email e webhooks
   - Push notifications
   - Eventos personalizados

8. **🎯 Configurações por Agente**
   - Vendas, Suporte, Conteúdo
   - Parâmetros específicos
   - Comportamento personalizado

9. **📈 Visualizar Estatísticas**
   - Dashboard em tempo real
   - Métricas de uso
   - Performance do sistema

10. **🧪 Testar Integrações**
    - Teste de todos os canais
    - Validação de configurações
    - Relatórios de status

11. **💾 Backup/Restore**
    - Backup automático
    - Restauração de configurações
    - Versionamento

## 🔄 Backup e Restore

### 💾 Sistema de Backup

```python
# Backup automático
config.salvar_configuracao('api', config.API_CONFIG)
config.salvar_configuracao('integracoes', config.INTEGRACOES)

# Restore
config.carregar_configuracao('api')
config.carregar_configuracao('integracoes')
```

### 📁 Estrutura de Backup

```
backups/
├── backup_20241225_143022.json
├── backup_20241225_143022.db
├── config_api.json
├── config_integracoes.json
└── config_database.json
```

## 🚀 Como Usar

### 1. **Configuração Inicial**
```bash
python configurador.py
```

### 2. **Configuração via Código**
```python
from config import config

# Atualizar configuração
config.atualizar_configuracao('api', 'gemini', {
    'api_key': 'nova_chave',
    'model': 'gemini-1.5-flash'
})

# Obter configuração
api_config = config.obter_configuracao('api', 'gemini')
```

### 3. **Variáveis de Ambiente**
```bash
export GEMINI_API_KEY="sua_chave"
export OPENAI_API_KEY="sua_chave"
export SMTP_SERVER="smtp.gmail.com"
export EMAIL_USUARIO="seu_email@gmail.com"
```

## 📊 Monitoramento

### 📈 Dashboard em Tempo Real

- **Processamentos**: Total, sucessos, erros
- **Performance**: Tempo de resposta, uso de memória
- **Integrações**: Status dos canais
- **Métricas**: KPIs personalizados

### 🔍 Logs Detalhados

```
logs/
├── agente.log
├── integracoes.log
├── database.log
└── performance.log
```

## 🎉 Benefícios

### ✅ **Flexibilidade Total**
- Mais de 50 opções de configuração
- Interface interativa amigável
- Backup e restore automático

### ✅ **Integração Completa**
- 6 canais de comunicação
- 4 tipos de banco de dados
- 3 APIs de IA diferentes

### ✅ **Segurança Avançada**
- Rate limiting
- Criptografia
- Validação de arquivos

### ✅ **Performance Otimizada**
- Cache inteligente
- Processamento paralelo
- Controle de recursos

### ✅ **Monitoramento Completo**
- Dashboard em tempo real
- Logs detalhados
- Métricas automáticas

**Seu agente de IA agora é um sistema empresarial completo! 🚀**
