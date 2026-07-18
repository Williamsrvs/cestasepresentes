#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificador Final de Configuração
Valida se tudo está pronto para rodar
"""

import os
import sys
from dotenv import load_dotenv
import mysql.connector

def check_mark(condition, message):
    """Mostra checkmark ou X"""
    status = "✅" if condition else "❌"
    print(f"{status} {message}")
    return condition

def main():
    print("\n" + "="*70)
    print("📋 CHECKLIST DE CONFIGURAÇÃO - CATÁLOGO DIGITAL")
    print("="*70)
    
    # 1. Verificar arquivo .env
    print("\n🔍 1. ARQUIVO DE CONFIGURAÇÃO")
    print("-"*70)
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    env_exists = check_mark(os.path.exists(env_path), "Arquivo .env existe")
    
    if not env_exists:
        print("❌ Crie o arquivo .env na raiz do projeto")
        return False
    
    # 2. Carregar variáveis
    print("\n🔍 2. VARIÁVEIS DE AMBIENTE")
    print("-"*70)
    load_dotenv(dotenv_path=env_path)
    
    host = os.getenv('MYSQL_HOST')
    user = os.getenv('MYSQL_USER')
    password = os.getenv('MYSQL_PASSWORD')
    database = os.getenv('MYSQL_DB')
    port_str = os.getenv('MYSQL_PORT')
    
    check_mark(host, f"MYSQL_HOST configurado: {host}")
    check_mark(user, f"MYSQL_USER configurado: {user}")
    check_mark(password, f"MYSQL_PASSWORD: {'definida' if password else 'VAZIA - ⚠️'}")
    check_mark(database, f"MYSQL_DB configurado: {database}")
    check_mark(port_str, f"MYSQL_PORT configurado: {port_str}")
    
    if not all([host, user, database, port_str]):
        print("\n❌ Algumas variáveis estão vazias no .env")
        return False
    
    try:
        port = int(port_str)
    except ValueError:
        print(f"\n❌ MYSQL_PORT inválido: {port_str} (deve ser número)")
        return False
    
    # 3. Verificar bibliotecas
    print("\n🔍 3. BIBLIOTECAS PYTHON")
    print("-"*70)
    
    try:
        import mysql.connector
        from packaging import version
        v = mysql.connector.__version__
        is_good = version.parse(v) >= version.parse("8.2.0")
        check_mark(is_good, f"mysql-connector-python: {v} {'✅' if is_good else '(deve ser >= 8.2.0)'}")
    except ImportError:
        check_mark(False, "mysql-connector-python não instalado")
        return False
    
    try:
        import flask
        check_mark(True, f"Flask: {flask.__version__}")
    except ImportError:
        check_mark(False, "Flask não instalado")
        return False
    
    # 4. Conectividade
    print("\n🔍 4. CONECTIVIDADE")
    print("-"*70)
    
    import socket
    try:
        sock = socket.create_connection((host, port), timeout=3)
        sock.close()
        check_mark(True, f"Porta {port} em {host} acessível")
    except (socket.timeout, socket.error):
        check_mark(False, f"Porta {port} em {host} NÃO acessível")
        print("   → MySQL está rodando?")
        return False
    
    # 5. Autenticação
    print("\n🔍 5. AUTENTICAÇÃO")
    print("-"*70)
    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password or None,
            database=database,
            port=port,
            connection_timeout=5
        )
        check_mark(True, "Login no MySQL bem-sucedido")
        
        # Verificar tabelas
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        check_mark(len(tables) > 0, f"Tabelas no banco: {len(tables)} encontradas")
        
        cursor.close()
        conn.close()
        
    except mysql.connector.Error as e:
        check_mark(False, f"Erro ao conectar: {str(e)[:60]}")
        print(f"   → Verifique usuario/senha no .env")
        return False
    
    # 6. Arquivos necessários
    print("\n🔍 6. ARQUIVOS DO PROJETO")
    print("-"*70)
    
    required_files = [
        'app/routes.py',
        'app/config.py',
        'app/schema.sql',
        'requirements.txt'
    ]
    
    all_files_exist = True
    for file in required_files:
        path = os.path.join(os.path.dirname(__file__), file)
        exists = os.path.exists(path)
        check_mark(exists, file)
        all_files_exist = all_files_exist and exists
    
    # Resumo
    print("\n" + "="*70)
    if all_files_exist:
        print("✅ TUDO OK! Você pode iniciar a aplicação!")
        print("="*70)
        print("\nPróximo comando:")
        print("   python app.py")
        print("\nOu acesse: http://localhost:5000")
        print("="*70 + "\n")
        return True
    else:
        print("❌ Verifique os erros acima")
        print("="*70 + "\n")
        return False

if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⚠️  Operação cancelada")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)
