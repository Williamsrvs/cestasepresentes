#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de diagnóstico para verificar a estrutura do banco de dados
"""

import mysql.connector
from mysql.connector import Error

db_config = {
    'host': 'auth-db1937.hstgr.io',
    'user': 'u799109175_cestas_present',
    'password': 'Q1k2v1y5@2025',  
    'database': 'u799109175_cestas_present',  
    'port': 3306
}

try:
    print("🔍 Conectando ao banco de dados...")
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    
    print("\n📊 Verificando banco de dados atual:")
    cursor.execute("SELECT DATABASE();")
    db_atual = cursor.fetchone()[0]
    print(f"   Database: {db_atual}")
    
    print("\n📋 Listando todas as tabelas:")
    cursor.execute("SHOW TABLES;")
    tabelas = cursor.fetchall()
    for tabela in tabelas:
        print(f"   - {tabela[0]}")
    
    print("\n🔎 Analisando tabela 'tbl_pedidos':")
    cursor.execute("DESCRIBE tbl_pedidos;")
    colunas = cursor.fetchall()
    print("   Colunas existentes:")
    for col in colunas:
        col_name = col[0]
        col_type = col[1]
        null = col[2]
        print(f"      - {col_name}: {col_type} (NULL: {null})")
    
    print("\n🔎 Analisando tabela 'tbl_detalhes_pedido':")
    cursor.execute("DESCRIBE tbl_detalhes_pedido;")
    colunas = cursor.fetchall()
    print("   Colunas existentes:")
    for col in colunas:
        col_name = col[0]
        col_type = col[1]
        null = col[2]
        print(f"      - {col_name}: {col_type} (NULL: {null})")
    
    print("\n✅ Diagnóstico concluído!")
    
    cursor.close()
    conexao.close()
    
except Error as e:
    print(f"❌ Erro: {e}")
