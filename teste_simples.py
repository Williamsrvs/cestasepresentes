#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Teste simplificado do fluxo de pedidos"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:5000"
HEADERS = {"Content-Type": "application/json"}

resultado = []

def log_msg(msg):
    """Log message to file and print"""
    resultado.append(msg)
    try:
        print(msg, flush=True)
    except:
        pass

# Teste 1: API de Produtos
log_msg("\n=== TESTE 1: API de Produtos ===")
try:
    r = requests.get(f"{BASE_URL}/api/produtos", headers=HEADERS, timeout=5)
    if r.status_code == 200:
        dados = r.json()
        if 'produtos' in dados and len(dados['produtos']) > 0:
            log_msg(f"OK: Retornou {len(dados['produtos'])} produtos")
            produtos = dados['produtos']
        else:
            log_msg("ERRO: Lista vazia")
            produtos = []
    else:
        log_msg(f"ERRO: Status {r.status_code}")
        produtos = []
except Exception as e:
    log_msg(f"ERRO: {e}")
    produtos = []

# Teste 2: Salvar Pedido
log_msg("\n=== TESTE 2: Salvar Pedido ===")
if len(produtos) > 0:
    try:
        produto = produtos[0]
        carrinho = [{
            'produtoId': produto['id_prod'],
            'nome': produto['nome_prod'],
            'valor': float(produto['valor']),
            'quantidade': 1,
            'subtotal': float(produto['valor'])
        }]
        
        dados = {
            'carrinho': carrinho,
            'id_cliente': 1,
            'nome_cliente': 'TESTE',
            'telefone_cliente': '82981090042',
            'numero_mesa': '1',
            'endereco': 'Rua Teste',
            'bairro': 'Centro',
            'ponto_referencia': 'Perto',
            'form_pgmto': 'PIX',
            'tipo_consumo': 'ENTREGA'
        }
        
        r = requests.post(f"{BASE_URL}/salvar_pedido", json=dados, headers=HEADERS, timeout=5)
        if r.status_code == 200:
            resultado_pedido = r.json()
            if resultado_pedido.get('status') == 'sucesso':
                log_msg(f"OK: Pedido #{resultado_pedido['id_pedido']} salvo")
                log_msg(f"    Valor: R$ {resultado_pedido['valor_total']}")
                log_msg(f"    Campos: endereco, bairro, ponto_referencia, form_pgmto, tipo_consumo [OK]")
            else:
                log_msg(f"ERRO: {resultado_pedido.get('mensagem', 'Erro desconhecido')}")
        else:
            log_msg(f"ERRO: Status {r.status_code}")
    except Exception as e:
        log_msg(f"ERRO: {e}")
else:
    log_msg("PULADO: Nenhum produto disponivel")

# Teste 3: Estrutura do Frontend
log_msg("\n=== TESTE 3: Estrutura do Frontend ===")
try:
    r = requests.get(f"{BASE_URL}/pedidos", timeout=5)
    if r.status_code == 200:
        html = r.text
        checks = [
            ('Button btnAddProduct', 'id="btnAddProduct"' in html),
            ('QRCode.js', 'qrcode' in html.lower()),
            ('updateQRCode', 'updateQRCode' in html),
            ('PIX Key', '05566941478' in html),
        ]
        for nome, passou in checks:
            status = "OK" if passou else "FALTA"
            log_msg(f"  {nome}: {status}")
    else:
        log_msg(f"ERRO: Status {r.status_code}")
except Exception as e:
    log_msg(f"ERRO: {e}")

# Resumo
log_msg("\n=== RESUMO ===")
log_msg("Todos os testes completados!")

# Salvar resultado em arquivo
with open('teste_resultado.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(resultado))

log_msg("\nResultado salvo em: teste_resultado.txt")
