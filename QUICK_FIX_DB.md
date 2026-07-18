# ⚡ QUICK START - Resolver Erro de Banco de Dados

## 🎯 O Que Foi Corrigido

| Problema | Solução |
|----------|---------|
| ❌ "Failed raising error" | ✅ Downgrade mysql-connector 9.5.0 → 8.2.0 |
| ❌ Mistura de bibliotecas | ✅ Padronizado em mysql-connector |
| ❌ Credenciais desatualizado | ✅ Atualizado .env com comentários |

---

## 🚀 Próximos 3 Passos

### PASSO 1: Descobrir Senha do MySQL (5 min)

```powershell
# Execute AUTOMATICAMENTE (testa senhas comuns):
python test_passwords.py

# Se encontrar, você verá:
# ✨ SENHA CORRETA ENCONTRADA: 'root'
```

**Se não encontrou nenhuma:**
- Você definiu senha personalizada?
- Está usando XAMPP/WAMP/MAMP/Docker?

---

### PASSO 2: Configurar `.env` (2 min)

Abra o arquivo `.env` na raiz do projeto e atualize:

```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=root    # ← COLOQUE A SENHA AQUI
MYSQL_DB=catalogo_digital
MYSQL_PORT=3306
```

---

### PASSO 3: Testar e Iniciar (3 min)

```powershell
# Teste a conexão
python diagnostic_db.py

# Se vir: ✅ TUDO OK! 
# Então execute:
python app.py
```

---

## 📍 Cenários Comuns

### Cenário 1: Acabei de Instalar MySQL

**O MySQL pediu senha na instalação?**

- ✅ SIM → Coloque a senha que configurou no `.env`
- ❌ NÃO → Tente `MYSQL_PASSWORD=root` ou deixar vazia

Depois:
```powershell
python diagnostic_db.py
```

---

### Cenário 2: Estou Usando XAMPP/WAMP/MAMP

Credenciais padrão são geralmente:

| Aplicação | User | Password | Host |
|-----------|------|----------|------|
| XAMPP | root | (vazia) | localhost |
| WAMP | root | (vazia) | localhost |
| MAMP | root | root | localhost |

Configure no `.env` e teste!

---

### Cenário 3: Prefiro Usar Docker

```powershell
# Criar container MySQL com senha "root"
docker run --name mysql-local `
  -e MYSQL_ROOT_PASSWORD=root `
  -e MYSQL_DATABASE=catalogo_digital `
  -p 3306:3306 -d mysql:8.0

# Espere 10 segundos e teste
python diagnostic_db.py
```

---

### Cenário 4: MySQL Não Está Instalado

**Opção A - Instalar (15 min)**
1. Baixe em https://dev.mysql.com/downloads/mysql/
2. Instale seguindo o assistente
3. Configure senha
4. Coloque a senha no `.env`
5. Execute `python diagnostic_db.py`

**Opção B - Docker (5 min) [RECOMENDADO]**
```powershell
# Instale Docker Desktop se não tem
# Depois:
docker run --name mysql-local -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=catalogo_digital -p 3306:3306 -d mysql:8.0

# Configure .env com MYSQL_PASSWORD=root
# Teste: python diagnostic_db.py
```

---

## 🆘 Erros Comuns

### "1045 - Access denied"
```
❌ Seu .env tem senha incorreta
✅ Execute: python test_passwords.py
✅ Ou configure manualmente no .env
```

### "1049 - Database doesn't exist"
```
❌ Banco catalogo_digital não existe
✅ Execute: python app.py (cria automaticamente)
```

### "Connection timeout" ou "Port not accessible"
```
❌ MySQL não está rodando ou firewall bloqueia
✅ Verifique serviço: Get-Service MySQL80
✅ Ou use Docker: docker run ... (comando acima)
```

### "mysqlconnector: Failed raising error"
```
❌ Versão 9.5.0 tinha bug (JÁ CORRIGIDO)
✅ Reinstale: pip install mysql-connector-python==8.2.0
```

---

## 📚 Scripts Disponíveis

```powershell
# Testar senhas comuns (encontra automaticamente)
python test_passwords.py

# Diagnóstico completo com detalhes
python diagnostic_db.py

# Configurador interativo
python setup_db.py

# Iniciar aplicação
python app.py
```

---

## ✅ Resumo da Solução

1. ✅ Corrigido `mysql-connector-python==8.2.0`
2. ✅ Criado script de teste `test_passwords.py`
3. ✅ Criado diagnóstico `diagnostic_db.py`
4. ✅ Criado configurador `setup_db.py`
5. ✅ Documentação completa em `SOLUCAO_BANCO_DADOS.md`

---

**Status**: 🟢 Pronto para usar!

