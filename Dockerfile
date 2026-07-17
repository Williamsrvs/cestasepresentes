# Dockerfile para Catálogo Digital

FROM python:3.11-slim

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    mariadb-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Criar pasta de uploads
RUN mkdir -p app/static/uploads && chmod 755 app/static/uploads

# Expor porta
EXPOSE 5000

# Variáveis de ambiente
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Iniciar aplicação em produção com Gunicorn (servidor WSGI multi-worker).
# O servidor de desenvolvimento do Flask (`python app.py`) não é adequado
# para produção e não mantém conexões estáveis sob carga.
CMD ["gunicorn", "--workers=4", "--worker-class=sync", "--bind=0.0.0.0:5000", "--timeout=120", "--access-logfile=-", "--error-logfile=-", "wsgi:app"]
