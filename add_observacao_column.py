"""
Script para adicionar a coluna 'observacao' à tabela tbl_detalhes_pedido
Executa apenas se a coluna não existir já
"""

import mysql.connector
from mysql.connector import errorcode
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuração de conexão com o banco
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'u799109175_cestas_present'
}

try:
    conn = mysql.connector.connect(**config)
    cur = conn.cursor()
    
    # Verificar se a coluna já existe
    cur.execute("""
        SELECT COLUMN_NAME 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'tbl_detalhes_pedido' 
        AND COLUMN_NAME = 'observacao'
    """)
    
    if cur.fetchone():
        logging.info("✅ Coluna 'observacao' já existe na tabela tbl_detalhes_pedido")
    else:
        logging.info("❌ Coluna 'observacao' não encontrada. Adicionando...")
        
        # Adicionar a coluna
        cur.execute("""
            ALTER TABLE tbl_detalhes_pedido 
            ADD COLUMN observacao TEXT NULL
        """)
        
        conn.commit()
        logging.info("✅ Coluna 'observacao' adicionada com sucesso!")
    
    cur.close()
    conn.close()
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        logging.error("❌ Erro de autenticação - verifique usuário/senha")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        logging.error("❌ Banco de dados não existe")
    else:
        logging.error(f"❌ Erro: {err}")
except Exception as e:
    logging.error(f"❌ Erro inesperado: {e}")
