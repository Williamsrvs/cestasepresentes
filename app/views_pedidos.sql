-- ============================================
-- VIEW: vw_pedidos_fin
-- Relatório resumido de pedidos por cliente
-- ============================================

CREATE OR REPLACE VIEW u799109175_cestas_present.vw_pedidos_fin AS
SELECT
    pe.id_pedido,
    pe.nome_cliente,
    pe.telefone,
    pe.dt_registro,
    pe.status_pedido,
    pe.endereco,
    pe.bairo,
    pe.form_pgmto,
	pe.tipo_consumo,
    SUM(pe.valor_total) AS valor_total
FROM u799109175_cestas_present.tbl_detalhes_pedido pe
GROUP BY
    pe.id_pedido,
    pe.nome_cliente,
    pe.telefone,
    pe.dt_registro,
    pe.status_pedido
ORDER BY pe.dt_registro DESC;

-- ============================================
-- VIEW: vw_resumo_pedidos_cliente
-- Totalizando pedidos por cliente
-- ============================================

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
ORDER BY SUM(pe.valor_total) DESC;

-- ============================================
-- VIEW: vw_pedidos_detalhado
-- Detalhamento completo de cada pedido
-- ============================================

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
ORDER BY pe.dt_registro DESC;
