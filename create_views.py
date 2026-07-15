#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para criar as VIEWs de relatório de pedidos
"""

import mysql.connector
from mysql.connector import Error

db_config = {
    'host': 'auth-db1937.hstgr.io',
    'user': 'u799109175_cestas_present',
    'password': 'Q1k2v1y5@2025',  
    'database': 'u799109175_cestas_present',  
    'port': 3306
}

def executar_sql(cursor, sql, descricao):
    """Executa um comando SQL e mostra o resultado"""
    try:
        for comando in sql.split(';'):
            cmd = comando.strip()
            if cmd:
                cursor.execute(cmd)
        print(f"✅ {descricao}")
        return True
    except Error as e:
        print(f"❌ {descricao}: {e}")
        return False

def main():
    print("=" * 70)
    print("🔧 Criando VIEWs de Relatório de Pedidos")
    print("=" * 70)
    
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()
        
        print("\n📊 Conectado ao banco de dados com sucesso!\n")
        
        # VIEW 1: vw_pedidos_fin
        sql1 = """
        CREATE OR REPLACE VIEW u799109175_cestas_present.vw_pedidos_fin AS
        SELECT
            pe.id_pedido,
            pr.nome_prod,
            pr.valor AS valor_unitario,
            pe.quantidade,
            pe.valor_total,
            pe.nome_cliente,
            pe.telefone,
            pe.dt_registro
        FROM u799109175_cestas_present.tbl_detalhes_pedido pe
        INNER JOIN u799109175_cestas_present.tbl_prod pr 
            ON pr.id_prod = pe.id_prod
        ORDER BY pe.dt_registro DESC
        """
        executar_sql(cursor, sql1, "VIEW vw_pedidos_fin criada")
        
        # VIEW 2: vw_resumo_pedidos_cliente
        sql2 = """
        CREATE OR REPLACE VIEW u799109175_cestas_present.vw_resumo_pedidos_cliente AS
        SELECT
            pe.nome_cliente,
            pe.telefone,
            COUNT(DISTINCT pe.id_pedido) AS total_pedidos,
            COUNT(pe.id_detalhe) AS total_itens,
            SUM(pe.quantidade) AS quantidade_total,
            SUM(pe.valor_total) AS valor_total_cliente,
            MAX(pe.dt_registro) AS ultimo_pedido
        FROM u799109175_cestas_present.tbl_detalhes_pedido pe
        GROUP BY pe.nome_cliente, pe.telefone
        ORDER BY SUM(pe.valor_total) DESC
        """
        executar_sql(cursor, sql2, "VIEW vw_resumo_pedidos_cliente criada")
        
        # VIEW 3: vw_pedidos_detalhado
        sql3 = """
        CREATE OR REPLACE VIEW u799109175_cestas_present.vw_pedidos_detalhado AS
        SELECT
            pe.id_pedido,
            pe.id_detalhe,
            pr.nome_prod,
            pr.valor AS valor_unitario,
            pe.quantidade,
            pe.valor_total AS subtotal_item,
            ped.valor_total AS total_pedido,
            pe.nome_cliente,
            pe.telefone,
            pe.dt_registro,
            ped.status_pedido
        FROM u799109175_cestas_present.tbl_detalhes_pedido pe
        INNER JOIN u799109175_cestas_present.tbl_prod pr 
            ON pr.id_prod = pe.id_prod
        INNER JOIN u799109175_cestas_present.tbl_pedidos ped
            ON ped.id_pedido = pe.id_pedido
        ORDER BY pe.dt_registro DESC
        """
        executar_sql(cursor, sql3, "VIEW vw_pedidos_detalhado criada")
        
        conexao.commit()
        
        print("\n" + "=" * 70)
        print("✅ Todas as VIEWs foram criadas com sucesso!")
        print("=" * 70)
        print("\n📋 VIEWs disponíveis:")
        print("   1️⃣  vw_pedidos_fin - Listagem de pedidos com detalhes")
        print("   2️⃣  vw_resumo_pedidos_cliente - Totais por cliente")
        print("   3️⃣  vw_pedidos_detalhado - Pedidos com informações completas")
        print("\n💡 Exemplos de consulta:")
        print("   SELECT * FROM vw_pedidos_fin;")
        print("   SELECT * FROM vw_resumo_pedidos_cliente;")
        print("   SELECT * FROM vw_pedidos_detalhado;")
        
        cursor.close()
        conexao.close()
        
    except Error as e:
        print(f"❌ Erro ao conectar ao banco: {e}")

if __name__ == '__main__':
    main()
