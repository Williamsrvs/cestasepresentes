#!/usr/bin/env python3
"""
Script para testar as rotas /salvar_pedido e /enviar_whatsapp
"""

import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_salvar_pedido():
    """Testa a rota /salvar_pedido"""
    print("\n" + "="*60)
    print("🧪 TESTE 1: POST /salvar_pedido")
    print("="*60)
    
    payload = {
        "carrinho": [
            {
                "produtoId": 1,
                "nome": "Testando Produto",
                "quantidade": 2,
                "valor": 15.50,
                "subtotal": 31.00
            }
        ],
        "nome_cliente": "João Teste",
        "email_cliente": "joao@teste.com",
        "telefone_cliente": "(82) 98109-0042",
        "numero_mesa": None,
        "endereco": "Rua Teste, 123",
        "bairro": "Centro",
        "cidade": "Maceió",
        "uf": "AL",
        "ponto_referencia": "Perto da padaria",
        "form_pgmto": "Pix",
        "tipo_consumo": "Delivery",
        "observacao": "Sem cebola",
        "taxa_entrega": 6.00
    }
    
    try:
        response = requests.post(f"{BASE_URL}/salvar_pedido", json=payload)
        print(f"Status: {response.status_code}")
        print(f"Resposta: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        
        if response.status_code == 200:
            return response.json().get('id_pedido')
        else:
            print("❌ Erro ao salvar pedido")
            return None
            
    except Exception as e:
        print(f"❌ Erro ao conectar: {e}")
        return None

def test_enviar_whatsapp():
    """Testa a rota /enviar_whatsapp"""
    print("\n" + "="*60)
    print("🧪 TESTE 2: POST /enviar_whatsapp")
    print("="*60)
    
    payload = {
        "whatsapp_numero": "5582981090042",
        "mensagem": "*NOVO PEDIDO #123*\n\n👤 Cliente: João Teste\n📱 Telefone: (82) 98109-0042\n\n1. Testando Produto x2 - R$ 31,00\n\n💰 Subtotal: R$ 31,00\n🚚 Taxa Entrega: R$ 6,00\n💰 TOTAL: R$ 37,00"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/enviar_whatsapp", json=payload)
        print(f"Status: {response.status_code}")
        result = response.json()
        print(f"Resposta: {json.dumps(result, indent=2, ensure_ascii=False)}")
        
        if response.status_code == 200 and result.get('url_whatsapp'):
            print(f"\n✅ URL gerada com sucesso:")
            print(f"   {result['url_whatsapp'][:100]}...")
            return True
        else:
            print("❌ Erro ao gerar link WhatsApp")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao conectar: {e}")
        return False

if __name__ == "__main__":
    print("\n🚀 Iniciando testes das rotas...")
    print(f"Base URL: {BASE_URL}")
    
    # Teste 1: Salvar pedido
    id_pedido = test_salvar_pedido()
    
    # Teste 2: Enviar WhatsApp
    test_enviar_whatsapp()
    
    print("\n" + "="*60)
    print("✅ Testes concluídos!")
    print("="*60)
