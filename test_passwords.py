#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testador de Senhas Comuns - MySQL
Tenta conectar com as senhas mais comuns
"""

import mysql.connector
import sys

print("\n" + "="*70)
print("🔐 TESTANDO SENHAS COMUNS PARA MySQL")
print("="*70)

host = "localhost"
user = "root"
database = "catalogo_digital"
port = 3306

# Senhas mais comuns
senhas_comuns = [
    "",                      # Vazia (padrão MySQL)
    "root",                  # Comum
    "password",              # Comum
    "123456",                # Comum
    "admin",                 # Comum
    "mysql",                 # Comum
]

print(f"\n🔍 Testando com host={host}, user={user}...\n")

for i, senha in enumerate(senhas_comuns, 1):
    label = "(VAZIA)" if not senha else f"'{senha}'"
    print(f"{i}. Tentando senha {label}...", end=" ")
    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=senha,
            database=database,
            port=port,
            autocommit=False,
            connection_timeout=3
        )
        
        print("✅ FUNCIONOU!")
        print(f"\n{'='*70}")
        print(f"✨ SENHA CORRETA ENCONTRADA: {label}")
        print(f"{'='*70}")
        print(f"\n📝 Atualize seu .env com:")
        print(f"MYSQL_PASSWORD={senha}")
        print(f"\n{'='*70}\n")
        
        conn.close()
        sys.exit(0)
        
    except mysql.connector.Error as e:
        print("❌")
    except Exception as e:
        print("❌")

print(f"\n{'='*70}")
print("❌ Nenhuma senha comum funcionou!")
print(f"{'='*70}")
print(f"""
Próximas ações:

1. Se instalou MySQL e configurou uma senha personalizada:
   • Digite a senha que você configurou no .env

2. Se esqueceu a senha:
   • Windows: Reinicie MySQL sem senha
   • Linux/Mac: Reinicie em modo seguro

3. Se está usando XAMPP/WAMP/MAMP:
   • Verifique as credenciais padrão da aplicação

4. Abra o arquivo .env e edite:
   MYSQL_PASSWORD=sua_senha_aqui

5. Depois teste:
   python diagnostic_db.py
   
{'='*70}
""")
sys.exit(1)
