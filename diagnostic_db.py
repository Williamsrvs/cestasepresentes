#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Diagnóstico de Conexão com Banco de Dados
Verifica todos os passos da conexão e mostra erros detalhados
"""

import os
import sys
import socket
from dotenv import load_dotenv

# Carregar variáveis de ambiente
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

print("\n" + "="*70)
print("🔍 DIAGNÓSTICO DE CONEXÃO - CATÁLOGO DIGITAL")
print("="*70)

# 1. Verificar variáveis de ambiente
print("\n📋 PASSO 1: VERIFICANDO VARIÁVEIS DE AMBIENTE")
print("-"*70)

host = os.getenv('MYSQL_HOST', 'localhost')
user = os.getenv('MYSQL_USER', 'root')
password = os.getenv('MYSQL_PASSWORD', '')
database = os.getenv('MYSQL_DB', 'u799109175_cestas_present')
port = int(os.getenv('MYSQL_PORT', 3306))

print(f"✓ Host: {host}")
print(f"✓ Usuário: {user}")
print(f"✓ Banco: {database}")
print(f"✓ Porta: {port}")
print(f"✓ Senha: {'*** (configurada)' if password else '(vazia - AVISO!)'}")

# 2. Verificar conectividade de rede
print("\n🌐 PASSO 2: VERIFICANDO CONECTIVIDADE DE REDE")
print("-"*70)

try:
    sock = socket.create_connection((host, port), timeout=5)
    sock.close()
    print(f"✓ Porta {port} acessível em {host}")
except socket.timeout:
    print(f"✗ ERRO: Timeout ao conectar em {host}:{port}")
    print(f"  Sugestões:")
    print(f"  • Verifique se MySQL está rodando")
    print(f"  • Verifique firewall local")
    print(f"  • Para Docker: docker ps (o container está rodando?)")
except socket.error as e:
    print(f"✗ ERRO: Não conseguiu conectar em {host}:{port}")
    print(f"  Detalhes: {e}")
    print(f"  Sugestões:")
    print(f"  • Verifique o endereço do host")
    print(f"  • Inicie o MySQL/MariaDB")
    print(f"  • Se usar Docker: docker run --name mysql-local -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=u799109175_cestas_present -p 3306:3306 -d mysql:8.0")

# 3. Verificar mysql.connector
print("\n📦 PASSO 3: VERIFICANDO BIBLIOTECAS PYTHON")
print("-"*70)

try:
    import mysql.connector
    print(f"✓ mysql-connector-python instalado (versão: {mysql.connector.__version__})")
except ImportError:
    print(f"✗ ERRO: mysql-connector-python não instalado")
    print(f"  Instale com: pip install mysql-connector-python")
    sys.exit(1)

# 4. Tentar conectar
print("\n🔗 PASSO 4: TENTANDO CONECTAR AO BANCO")
print("-"*70)

try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port,
        autocommit=False,
        connection_timeout=10
    )
    
    print(f"✓ CONEXÃO BEM-SUCEDIDA! ✅")
    
    # 5. Verificar tabelas
    print("\n📊 PASSO 5: VERIFICANDO TABELAS DO BANCO")
    print("-"*70)
    
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    
    if tables:
        print(f"✓ Encontradas {len(tables)} tabelas:")
        for table in tables:
            print(f"  • {table[0]}")
    else:
        print(f"⚠️  Nenhuma tabela encontrada no banco")
        print(f"  Dica: Execute 'python app.py' para criar as tabelas automaticamente")
    
    cursor.close()
    conn.close()
    
    print("\n" + "="*70)
    print("✅ TUDO OK! Você pode iniciar a aplicação com: python app.py")
    print("="*70 + "\n")

except mysql.connector.Error as e:
    print(f"✗ ERRO DE CONEXÃO: {e}")
    print(f"\nDiagnóstico do erro:")
    
    error_code = e.errno
    if error_code == 2003:
        print(f"  • Impossível conectar ao servidor MySQL")
        print(f"  • Verifique se o MySQL está rodando em {host}:{port}")
    elif error_code == 1045:
        print(f"  • Erro de autenticação (usuário ou senha incorretos)")
        print(f"  • Verifique credenciais no arquivo .env")
    elif error_code == 1049:
        print(f"  • Banco de dados '{database}' não existe")
        print(f\"  • Crie com: mysql -u {user} -p -e 'CREATE DATABASE u799109175_cestas_present;'\")
    else:
        print(f"  • Código de erro: {error_code}")
    
    sys.exit(1)

except Exception as e:
    print(f"✗ ERRO INESPERADO: {e}")
    print(f"  Tipo: {type(e).__name__}")
    sys.exit(1)
