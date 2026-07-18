#!/usr/bin/env python3
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))
from routes import app

with app.app_context():
    with app.test_client() as c:
        payload = {
            'carrinho': [
                {'produtoId': 20, 'quantidade': 1, 'valor': 32.99, 'subtotal': 32.99}
            ],
            'nome_cliente': 'Cliente Teste',
            'telefone_cliente': '11999990000',
            'numero_mesa': None,
            'endereco': 'Rua Teste, 123',
            'bairro': 'Centro',
            'ponto_referencia': 'Perto do X',
            'form_pgmto': 'Dinheiro',
            'tipo_consumo': 'Delivery'
        }
        rv = c.post('/salvar_pedido', data=json.dumps(payload), content_type='application/json')
        print('STATUS', rv.status_code)
        try:
            print(rv.get_json())
        except Exception:
            print(rv.data.decode())
