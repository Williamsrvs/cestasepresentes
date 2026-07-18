#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para verificar se há produtos cadastrados no banco de dados
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

try:
    from app import mysql
    from datetime import datetime
    
    print("=" * 70)
    print("🔍 VERIFICAÇÃO: Produtos no Banco de Dados")
    print("=" * 70)
    print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print()
    
    try:
        conn = mysql.get_connection()
        cur = conn.cursor(dictionary=True)
        
        print("📊 Consultando tabela tbl_prod...")
        print()
        
        # Contar total de produtos
        cur.execute("SELECT COUNT(*) as total FROM tbl_prod")
        total = cur.fetchone()['total']
        print(f"  Total de produtos: {total}")
        
        # Contar produtos ativos
        cur.execute("SELECT COUNT(*) as ativo FROM tbl_prod WHERE ativo = 1")
        ativo = cur.fetchone()['ativo']
        print(f"  Produtos ativos (ativo=1): {ativo}")
        
        # Contar produtos inativos
        cur.execute("SELECT COUNT(*) as inativo FROM tbl_prod WHERE ativo = 0")
        inativo = cur.fetchone()['inativo']
        print(f"  Produtos inativos (ativo=0): {inativo}")
        
        print()
        print("-" * 70)
        print("📋 Primeiros 5 produtos ativos:")
        print("-" * 70)
        
        cur.execute("""
            SELECT id_prod, nome_prod, valor, ativo, created_at 
            FROM tbl_prod 
            WHERE ativo = 1 
            ORDER BY created_at DESC 
            LIMIT 5
        """)
        
        produtos = cur.fetchall()
        
        if not produtos:
            print("❌ AVISO: Nenhum produto encontrado com ativo=1!")
            print()
            print("Solução: Cadastre novos produtos ou ative produtos existentes")
        else:
            for idx, prod in enumerate(produtos, 1):
                print(f"\n  {idx}. {prod['nome_prod']}")
                print(f"     ID: {prod['id_prod']}")
                print(f"     Preço: R$ {prod['valor']:.2f}")
                print(f"     Ativo: {'✅ Sim' if prod['ativo'] == 1 else '❌ Não'}")
        
        print()
        print("=" * 70)
        print("CONCLUSÃO:")
        print("=" * 70)
        
        if ativo > 0:
            print(f"✅ OK! Há {ativo} produto(s) pronto(s) para usar")
            print("   Os produtos devem aparecer no seletor quando clicar em")
            print("   '+ Adicionar Produto'")
        else:
            print("❌ PROBLEMA: Nenhum produto ativo encontrado!")
            print()
            print("Para resolver:")
            print("  1. Acesse http://localhost:5000/produto")
            print("  2. Cadastre novos produtos")
            print("  3. OU ative produtos existentes no gerenciador")
        
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Erro ao conectar ao banco de dados:")
        print(f"   {type(e).__name__}: {str(e)}")
        print()
        print("Verifique:")
        print("  1. Credenciais do banco de dados em config.py")
        print("  2. Servidor MySQL está rodando")
        print("  3. Banco de dados existe")

except ImportError as e:
    print(f"❌ Erro ao importar app:")
    print(f"   {str(e)}")
    print()
    print("Solução:")
    print("  Certifique-se de estar na pasta raiz do projeto")
    print("  E que as dependências estão instaladas")

print()
