<<<<<<< HEAD
# Configuração para Desenvolvimento Local

## Problema
O servidor local não consegue conectar ao banco de dados remoto do Render. Isso é esperado porque:
- O banco remoto pode estar bloqueando conexões de IPs locais
- Firewall local pode estar bloqueando porta 3306

## Solução

### 1. Configure um MySQL local
Você tem 2 opções:

#### Opção A: Usar MySQL/MariaDB instalado localmente
```bash
# No Windows, verifique se MySQL está rodando
# Painel de Controle > Serviços > MySQL80

# Ou via PowerShell (como admin)
Get-Service MySQL80
```

#### Opção B: Usar Docker (Recomendado)
```bash
# Instale Docker Desktop
# Depois execute:
docker run --name mysql-local -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=catalogo_digital -p 3306:3306 -d mysql:8.0
```

### 2. Ajuste o arquivo `.env`

Edite `.env` na raiz do projeto com suas credenciais locais:

```env
# Desenvolvimento Local
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=root         # Sua senha local
MYSQL_DB=catalogo_digital
MYSQL_PORT=3306

FLASK_ENV=development
SECRET_KEY=dev-secret-key
```

### 3. Crie o banco de dados

```bash
# Via MySQL CLI
mysql -u root -p
CREATE DATABASE IF NOT EXISTS catalogo_digital;
USE catalogo_digital;
source app/schema.sql;
exit
```

### 4. Instale dependências (se necessário)
```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação
```bash
python app.py
```

A aplicação agora usará:
- **Localmente**: `localhost` (seu `.env`)
- **No Render**: Variáveis de ambiente do Render

## Para Produção no Render

As variáveis de ambiente são configuradas no painel do Render:
- `MYSQL_HOST=auth-db1937.hstgr.io`
- `MYSQL_USER=u799109175_cestas_present`
- `MYSQL_PASSWORD=Ccap2004`
- `MYSQL_DB=u799109175_cestas_present`
- `MYSQL_PORT=3306`
- `FLASK_ENV=production`

---

**Nota**: Não faça commit do arquivo `.env` com dados sensíveis. Ele já está em `.gitignore`.
=======
# Configuração para Desenvolvimento Local

## Problema
O servidor local não consegue conectar ao banco de dados remoto do Render. Isso é esperado porque:
- O banco remoto pode estar bloqueando conexões de IPs locais
- Firewall local pode estar bloqueando porta 3306

## Solução

### 1. Configure um MySQL local
Você tem 2 opções:

#### Opção A: Usar MySQL/MariaDB instalado localmente
```bash
# No Windows, verifique se MySQL está rodando
# Painel de Controle > Serviços > MySQL80

# Ou via PowerShell (como admin)
Get-Service MySQL80
```

#### Opção B: Usar Docker (Recomendado)
```bash
# Instale Docker Desktop
# Depois execute:
docker run --name mysql-local -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=catalogo_digital -p 3306:3306 -d mysql:8.0
```

### 2. Ajuste o arquivo `.env`

Edite `.env` na raiz do projeto com suas credenciais locais:

```env
# Desenvolvimento Local
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=root         # Sua senha local
MYSQL_DB=catalogo_digital
MYSQL_PORT=3306

FLASK_ENV=development
SECRET_KEY=dev-secret-key
```

### 3. Crie o banco de dados

```bash
# Via MySQL CLI
mysql -u root -p
CREATE DATABASE IF NOT EXISTS catalogo_digital;
USE catalogo_digital;
source app/schema.sql;
exit
```

### 4. Instale dependências (se necessário)
```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação
```bash
python app.py
```

A aplicação agora usará:
- **Localmente**: `localhost` (seu `.env`)
- **No Render**: Variáveis de ambiente do Render

## Para Produção no Render

As variáveis de ambiente são configuradas no painel do Render:
- `MYSQL_HOST=auth-db1937.hstgr.io`
- `MYSQL_USER=u799109175_cestas_present`
- `MYSQL_PASSWORD=Q1k2v1y5@2025`
- `MYSQL_DB=u799109175_cestas_present`
- `MYSQL_PORT=3306`
- `FLASK_ENV=production`

---

**Nota**: Não faça commit do arquivo `.env` com dados sensíveis. Ele já está em `.gitignore`.
>>>>>>> 0e55895f93f44ec8fd1c355af29c4c5ef6a3027e
