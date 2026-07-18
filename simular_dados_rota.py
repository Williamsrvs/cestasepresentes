#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste que simula exatamente o que a rota retorna
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from config import db_config
import mysql.connector

print("="*70)
print("🔍 SIMULANDO EXATAMENTE O QUE A ROTA /pedidos_cliente RETORNA")
print("="*70)

try:
    print("\n📡 Conectando ao banco...")
    conn = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database'],
        port=db_config['port']
    )
    
    cur = conn.cursor(dictionary=True)
    
    # Executar EXATAMENTE a mesma query que a rota executa
    print("📦 Executando: SELECT id_prod, nome_prod, valor FROM tbl_prod WHERE ativo = 1 ORDER BY nome_prod ASC")
    cur.execute("SELECT id_prod, nome_prod, valor FROM tbl_prod WHERE ativo = 1 ORDER BY nome_prod ASC")
    produtos = cur.fetchall()
    
    print(f"\n✅ {len(produtos)} produtos encontrados\n")
    
    # Simular o Jinja2 template
    print("📄 JAVASCRIPT QUE SERÁ GERADO (Jinja2):\n")
    print("let produtosDisponiveis = [")
    
    for i, produto in enumerate(produtos):
        virgula = "," if i < len(produtos) - 1 else ""
        print(f'    {{ id: {produto["id_prod"]}, nome: "{produto["nome_prod"]}", valor: {produto["valor"]} }}{virgula}')
    
    print("];")
    
    print("\n" + "="*70)
    print("✅ ESTRUTURA DOS DADOS:")
    print("="*70)
    
    if produtos:
        p = produtos[0]
        print(f"\nPrimeiro produto:")
        print(f"  - Chave 'id_prod': {p['id_prod']} (tipo: {type(p['id_prod']).__name__})")
        print(f"  - Chave 'nome_prod': {p['nome_prod']} (tipo: {type(p['nome_prod']).__name__})")
        print(f"  - Chave 'valor': {p['valor']} (tipo: {type(p['valor']).__name__})")
        print(f"\n✅ Todas as chaves esperadas estão presentes!")
    
    cur.close()
    conn.close()
    
except Exception as e:
    print(f"\n❌ ERRO: {e}")
    import traceback
    traceback.print_exc()
