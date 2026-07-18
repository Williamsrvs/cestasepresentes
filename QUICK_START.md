# 🎯 GUIA RÁPIDO DE DEPLOY - CATÁLOGO DIGITAL

## 🚀 Começar Agora

### 1️⃣ Setup Local (Para Testes)
```bash
# Clone/Baixe o projeto
cd "Catálogo Digital"

# Crie ambiente virtual
python -m venv venv

# Ative (Windows)
venv\Scripts\activate
# Ou (Linux/Mac)
source venv/bin/activate

# Instale dependências
pip install -r requirements.txt

# Configure o .env
cp .env.example .env
# Edite .env com suas credenciais

# Inicialize o banco
mysql < app/schema.sql
python create_views.py

# Inicie
python app.py
```

**Resultado:** App rodando em `http://localhost:5000`

---

## 🐳 Deploy com Docker (Recomendado)

### Setup
```bash
# Prepare arquivo .env
cp .env.example .env
# Edite .env com credenciais

# Inicie com Docker Compose
docker-compose up -d

# Logs
docker-compose logs -f web
```

**Resultado:** App rodando em `https://localhost`

---

## ☁️ Deploy em Nuvem

### Heroku / Railway
```bash
# Prepare .env (não commit isso!)
cp .env.example .env

# Commit código
git add .
git commit -m "Deploy ready"

# Faça push
git push heroku main
# ou
railway deploy
```

### AWS / Azure / DigitalOcean
```bash
# SSH no servidor
ssh usuario@seu-servidor

# Clone repositório
git clone seu-repo
cd Catálogo\ Digital

# Siga passos de Setup Local acima

# Configure Nginx (use nginx.conf como template)
sudo cp nginx.conf /etc/nginx/sites-available/catalogo
sudo ln -s /etc/nginx/sites-available/catalogo /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx

# Configure systemd service
sudo cp catalogo.service /etc/systemd/system/
sudo systemctl start catalogo-digital
sudo systemctl enable catalogo-digital
```

---

## 📋 Arquivos Importantes

| Arquivo | Uso |
|---------|-----|
| `requirements.txt` | Instalar dependências: `pip install -r requirements.txt` |
| `.env.example` | Template de variáveis (copiar para `.env`) |
| `app.py` | Executar: `python app.py` |
| `wsgi.py` | Gunicorn: `gunicorn wsgi:app` |
| `Dockerfile` | Build Docker: `docker build -t catalogo-digital .` |
| `docker-compose.yml` | Orquestração: `docker-compose up -d` |
| `nginx.conf` | Configuração reverso proxy |
| `Procfile` | Deploy Heroku/Railway |
| `setup.sh` | Script automático (Linux/Mac) |
| `README.md` | Documentação completa |
| `DEPLOY_CHECKLIST.md` | Passo a passo de deploy |

---

## ⚙️ Variáveis de Ambiente (.env)

**OBRIGATÓRIAS:**
```
MYSQL_HOST=seu-banco.com
MYSQL_USER=usuario
MYSQL_PASSWORD=senha
MYSQL_DB=database
SECRET_KEY=chave-secreta-unica
```

**OPCIONAIS:**
```
FLASK_ENV=production
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
WHATSAPP_LOJISTA=55XXXXXXXXX
LOG_LEVEL=INFO
```

---

## 🔒 Segurança Antes do Deploy

```bash
# ✅ Checklist
[ ] .env configurado (não commitado)
[ ] SECRET_KEY alterado
[ ] Certificado SSL preparado
[ ] Banco de dados backup
[ ] Permissões de arquivos verificadas
[ ] Logs habilitados
[ ] Firewall configurado
[ ] CORS (se necessário) configurado
```

---

## 🆘 Troubleshooting Rápido

### Erro: "Cannot connect to database"
```bash
python diagnostic.py
# Verifique credenciais no .env
```

### Erro: "Port 5000 already in use"
```bash
# Mude a porta no .env
FLASK_PORT=8000
python app.py
```

### Erro: "ChromeDriver not found"
```bash
# Será baixado automaticamente por webdriver-manager
# Ou reinstale:
pip install webdriver-manager --force-reinstall
```

### WhatsApp não funciona
```bash
# Verifique se tem Chrome instalado
# Teste envio manualmente
python -c "from selenium import webdriver; print('Selenium OK')"
```

---

## 📊 Monitoramento

### Ver logs
```bash
# Local
tail -f app_errors.log

# Docker
docker-compose logs -f web

# VPS
journalctl -u catalogo-digital -f
```

### Health check
```bash
curl http://seu-servidor/health
# Deve retornar: OK
```

---

## 🔄 Atualizar em Produção

```bash
# Baixe atualizações
git pull origin main

# Reinstale dependências (se houver mudanças)
pip install -r requirements.txt

# Reinicie serviço
systemctl restart catalogo-digital
# Ou Docker:
docker-compose restart web

# Verifique logs
tail -f app_errors.log
```

---

## 📞 Precisa de Ajuda?

Consulte:
- **README.md** - Documentação completa
- **DEPLOY_CHECKLIST.md** - Passo a passo detalhado
- **ARQUIVOS_DEPLOY.md** - Lista de arquivos
- **diagnostic.py** - Diagnóstico automático

---

## ✅ Status: PRONTO PARA DEPLOY

Seu projeto foi preparado com:
- ✅ Dependências definidas (requirements.txt)
- ✅ Configuração production-ready
- ✅ Docker & Docker Compose
- ✅ Nginx com SSL
- ✅ Scripts de setup
- ✅ Documentação completa
- ✅ Checklist de deployment

**Escolha um método acima e inicie o deploy!** 🚀

---

**Última atualização:** 27 de novembro de 2025
