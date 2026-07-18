#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Teste direto do banco de dados - SEM precisar do Flask
Mostra se há produtos cadastrados e se o endpoint funcionaria
"""

import mysql.connector
import json

# Importar configuração
from config import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB

print("=" * 60)
print("🧪 TESTE DIRETO DO BANCO DE DADOS")
print("=" * 60)

try:
    # Conectar ao banco
    conexao = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    
    cursor = conexao.cursor(dictionary=True)
    
    # Teste 1: Contar todos os produtos
    print("\n📊 Teste 1: Total de Produtos")
    cursor.execute("SELECT COUNT(*) as total FROM tbl_prod")
    total = cursor.fetchone()['total']
    print(f"   Total de produtos: {total}")
    
    # Teste 2: Contar produtos ativos
    print("\n✅ Teste 2: Produtos ATIVOS (ativo=1)")
    cursor.execute("SELECT COUNT(*) as total FROM tbl_prod WHERE ativo = 1")
    ativos = cursor.fetchone()['total']
    print(f"   Total de produtos ativos: {ativos}")
    
    if ativos > 0:
        print("   ✅ OK - Há produtos disponíveis!")
    else:
        print("   ⚠️  PROBLEMA - Nenhum produto ativo!")
        print("   → Vá para http://localhost:5000/produto")
        print("   → Cadastre um produto")
        print("   → Marque como ATIVO")
    
    # Teste 3: Listar produtos ativos
    print("\n📋 Teste 3: Listando Produtos Ativos")
    cursor.execute("""
        SELECT id_prod, nome_prod, valor, ativo 
        FROM tbl_prod 
        WHERE ativo = 1
        ORDER BY nome_prod
    """)
    
    produtos = cursor.fetchall()
    
    if produtos:
        print(f"\n   Encontrados {len(produtos)} produtos:")
        for i, prod in enumerate(produtos, 1):
            print(f"   {i}. {prod['nome_prod']} - R$ {prod['valor']}")
    else:
        print("   ❌ Nenhum produto encontrado")
    
    # Teste 4: Simular resposta da API
    print("\n🔌 Teste 4: Simular Resposta da API /api/produtos")
    cursor.execute("""
        SELECT id_prod, nome_prod, valor 
        FROM tbl_prod 
        WHERE ativo = 1
    """)
    
    produtos_api = cursor.fetchall()
    resposta_api = {
        "status": "sucesso",
        "productos": produtos_api,
        "total": len(produtos_api)
    }
    
    print("   Resposta que a API /api/produtos retornaria:")
    print(json.dumps(resposta_api, ensure_ascii=False, indent=2, default=str))
    
    # Teste 5: Verificar estrutura do Jinja2
    print("\n🎯 Teste 5: JavaScript Array (Template Jinja2)")
    
    if produtos:
        js_array = "[\n"
        for i, prod in enumerate(produtos):
            js_array += f"    {{id: {prod['id_prod']}, nome: '{prod['nome_prod']}', valor: {prod['valor']}}}"
            if i < len(produtos) - 1:
                js_array += ",\n"
        js_array += "\n]"
        
        print("   Array JavaScript ficaria assim:")
        print(js_array)
    else:
        print("   ❌ Array vazio - sem produtos para gerar")
    
    # Resultado Final
    print("\n" + "=" * 60)
    if ativos > 0:
        print("✅ TUDO CERTO!")
        print("   • Produtos existem no banco")
        print("   • Template Jinja2 vai popular o array")
        print("   • Dropdown terá opções para selecionar")
        print("\n   Próximo passo: Acesse http://localhost:5000/pedidos")
        print("                 Clique em '+ Adicionar Produto'")
    else:
        print("❌ PROBLEMA DETECTADO!")
        print("   • Nenhum produto cadastrado com ativo=1")
        print("   • Dropdown vai mostrar 'Nenhum produto encontrado'")
        print("\n   Solução:")
        print("   1. Acesse http://localhost:5000/produto")
        print("   2. Clique em 'Cadastrar Novo Produto'")
        print("   3. Preencha nome e valor")
        print("   4. Marque como ATIVO (✓)")
        print("   5. Clique em SALVAR")
        print("   6. Volte e tente novamente")
    print("=" * 60)
    
    cursor.close()
    conexao.close()

except mysql.connector.Error as erro:
    print(f"❌ ERRO DE CONEXÃO: {erro}")
    print("\nVerifique:")
    print("  • MySQL está rodando?")
    print("  • Usuário e senha estão corretos em config.py?")
    print("  • Database '{MYSQL_DB}' existe?")
except Exception as erro:
    print(f"❌ ERRO: {erro}")
    print(f"   Tipo: {type(erro).__name__}")

print("\n✨ Teste finalizado!")
