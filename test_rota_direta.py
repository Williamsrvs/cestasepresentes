#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste direto da rota sem precisar de servidor HTTP
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from routes import app
from jinja2 import Template

print("="*60)
print("🔍 TESTE DIRETO DA ROTA /pedidos_cliente")
print("="*60)

# Usar contexto de aplicação Flask
with app.app_context():
    # Simular requisição GET
    with app.test_client() as client:
        print("\n🌐 Fazendo requisição GET para /pedidos_cliente...\n")
        
        response = client.get('/pedidos_cliente')
        
        print(f"✅ Status: {response.status_code}")
        print(f"✅ Content-Type: {response.content_type}")
        
        # Verificar se os dados estão lá
        html_content = response.get_data(as_text=True)
        
        # Procurar pelo array de produtos
        if 'produtosDisponiveis' in html_content:
            print("\n✅ Array 'produtosDisponiveis' encontrado!")
            
            # Extrair o trecho relevante
            inicio = html_content.find('let produtosDisponiveis = [')
            if inicio > 0:
                fim = html_content.find('];', inicio) + 2
                trecho = html_content[inicio:fim]
                
                # Mostrar o primeiro 500 caracteres
                print("\n📄 Conteúdo JavaScript (primeiros 500 chars):")
                print(trecho[:500])
                print("...")
                
                # Contar quantos produtos
                import re
                produtos = re.findall(r'{\s*id:', trecho)
                print(f"\n✅ Número de produtos encontrados: {len(produtos)}")
        else:
            print("\n❌ Array 'produtosDisponiveis' NÃO encontrado!")
            print("\n⚠️ Verificando se há 'id_prod'...")
            if 'id_prod' in html_content:
                print("✅ Encontrado 'id_prod' na resposta")
            else:
                print("❌ Nenhum 'id_prod' encontrado")

print("\n" + "="*60)
