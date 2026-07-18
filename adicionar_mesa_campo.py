#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para adicionar o campo 'numero_mesa' à tabela 'tbl_pedidos'
Execute este script uma vez para atualizar a estrutura do banco de dados
"""

import mysql.connector as mysql_conn
from config import db_config
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def adicionar_campo_mesa():
    try:
        conn = mysql_conn.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database'],
            port=db_config['port']
        )
        cur = conn.cursor()
        
        # Verificar se o campo já existe
        cur.execute("""
            SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_NAME = 'tbl_pedidos' AND COLUMN_NAME = 'numero_mesa'
        """)
        
        if cur.fetchone():
            logging.info("✅ Campo 'numero_mesa' já existe na tabela 'tbl_pedidos'")
        else:
            # Adicionar o campo
            cur.execute("""
                ALTER TABLE tbl_pedidos 
                ADD COLUMN numero_mesa INT DEFAULT NULL
            """)
            conn.commit()
            logging.info("✅ Campo 'numero_mesa' adicionado com sucesso à tabela 'tbl_pedidos'")
        
        # Também adicionar à tabela de detalhes se necessário
        cur.execute("""
            SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_NAME = 'tbl_detalhes_pedido' AND COLUMN_NAME = 'numero_mesa'
        """)
        
        if cur.fetchone():
            logging.info("✅ Campo 'numero_mesa' já existe na tabela 'tbl_detalhes_pedido'")
        else:
            cur.execute("""
                ALTER TABLE tbl_detalhes_pedido 
                ADD COLUMN numero_mesa INT DEFAULT NULL
            """)
            conn.commit()
            logging.info("✅ Campo 'numero_mesa' adicionado com sucesso à tabela 'tbl_detalhes_pedido'")
        
        cur.close()
        conn.close()
        logging.info("✅ Migração concluída com sucesso!")
        
    except mysql_conn.Error as e:
        logging.error(f"❌ Erro ao conectar ao MySQL: {e}")
    except Exception as e:
        logging.error(f"❌ Erro durante a migração: {e}")

if __name__ == '__main__':
    adicionar_campo_mesa()
