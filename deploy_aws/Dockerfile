FROM python:3.9-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Criar diretórios necessários
RUN mkdir -p uploads static/css static/js templates

# Expor porta
EXPOSE 8000

# Comando para executar
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "app:app"]
