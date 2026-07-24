import os
import sys
from dotenv import load_dotenv
import mysql.connector

# Carregar variáveis de ambiente
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

try:
    # Conectar usando variáveis de ambiente
    conn = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', ''),
        database=os.getenv('MYSQL_DB', 'catalogo_digital'),
        port=int(os.getenv('MYSQL_PORT', 3306))
    )
    cursor = conn.cursor()

    print("="*60)
    print("✅ CONEXÃO BEM-SUCEDIDA!")
    print("="*60)
    print(f"🖥️  Host: {os.getenv('MYSQL_HOST')}")
    print(f"👤 Usuário: {os.getenv('MYSQL_USER')}")
    print(f"🗄️  Database: {os.getenv('MYSQL_DB')}")
    print("="*60)
    
    conn.close()
except mysql.connector.Error as e:
    print("="*60)
    print("❌ ERRO DE CONEXÃO!")
    print("="*60)
    print(f"Erro: {e}")
    print(f"\nVerifique:")
    print(f"  • Host: {os.getenv('MYSQL_HOST')} (acessível?)")
    print(f"  • Usuário: {os.getenv('MYSQL_USER')}")
    print(f"  • Banco: {os.getenv('MYSQL_DB')}")
    print(f"  • Porta: {os.getenv('MYSQL_PORT')}")
    print("="*60)
    sys.exit(1)
except Exception as e:
    print("="*60)
    print("❌ ERRO INESPERADO!")
    print("="*60)
    print(f"Erro: {e}")
    print("="*60)
    sys.exit(1)
