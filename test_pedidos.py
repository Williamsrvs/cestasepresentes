#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste das funcionalidades de Pedidos e WhatsApp
"""

import requests
import json

print("\n" + "="*70)
print("🧪 TESTE DE FUNCIONALIDADES - SISTEMA DE PEDIDOS")
print("="*70)

BASE_URL = "http://localhost:5000"

# ====== TESTE 1: Verificar rota de pedidos ======
print("\n📝 TESTE 1: Acessar página de pedidos...")
try:
    response = requests.get(f"{BASE_URL}/pedidos")
    if response.status_code == 200:
        print("✅ Página de pedidos carregada com sucesso")
    else:
        print(f"❌ Erro: Status {response.status_code}")
except Exception as e:
    print(f"❌ Erro ao acessar /pedidos: {e}")

# ====== TESTE 2: Simular salvar pedido ======
print("\n💾 TESTE 2: Simular salvamento de pedido...")
try:
    payload = {
        "carrinho": [
            {
                "produtoId": 1,
                "nome": "Produto Teste",
                "quantidade": 2,
                "valor": 50.00,
                "subtotal": 100.00
            }
        ],
        "id_cliente": 1,
        "nome_cliente": "Cliente Teste",
        "telefone_cliente": "(82) 98109-0042"
    }
    
    response = requests.post(
        f"{BASE_URL}/salvar_pedido",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    
    result = response.json()
    print(f"Status: {result.get('status')}")
    print(f"Mensagem: {result.get('mensagem')}")
    
    if result.get('status') == 'sucesso':
        print(f"✅ Pedido salvo! ID: {result.get('id_pedido')}")
        pedido_id = result.get('id_pedido')
    else:
        print(f"⚠️ Resposta: {result}")
        pedido_id = None
        
except Exception as e:
    print(f"❌ Erro ao testar /salvar_pedido: {e}")
    pedido_id = None

# ====== TESTE 3: Testar geração de link WhatsApp ======
print("\n📱 TESTE 3: Testar geração de link WhatsApp...")
try:
    if pedido_id:
        payload = {
            "whatsapp_numero": "5582981090042",
            "mensagem": "*TESTE DE PEDIDO*\n\n👤 Cliente: Cliente Teste\n\n*Total: R$ 100.00*",
            "id_pedido": pedido_id
        }
        
        response = requests.post(
            f"{BASE_URL}/enviar_whatsapp",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        result = response.json()
        print(f"Status: {result.get('status')}")
        
        if result.get('status') == 'sucesso':
            print("✅ Link WhatsApp gerado com sucesso!")
            if result.get('url_whatsapp'):
                print(f"📱 URL: {result.get('url_whatsapp')[:80]}...")
        else:
            print(f"❌ Erro: {result.get('mensagem')}")
    else:
        print("⚠️ Pulando teste (pedido não foi criado)")
        
except Exception as e:
    print(f"❌ Erro ao testar /enviar_whatsapp: {e}")

print("\n" + "="*70)
print("✅ Testes concluídos!")
print("="*70 + "\n")
