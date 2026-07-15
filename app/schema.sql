CREATE TABLE IF NOT EXISTS tbl_prod (
    id_prod INT NOT null AUTO_INCREMENT PRIMARY KEY,
    nome_prod VARCHAR(100) NOT NULL,
    descricao TEXT,
    subgrupo varchar(50),
    status_promocao VARCHAR(50),
    valor DECIMAL(10,2) NOT NULL,
    form_pgmto VARCHAR(50),
    imagem_url longblob,
    ativo TINYINT DEFAULT 1,    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tbl_cliente(
    id_cliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_cliente VARCHAR(100),
    telefone VARCHAR(50),
    email VARCHAR(50),
    endereco TEXT,
    bairro VARCHAR(50),
    cidade VARCHAR(50),
    uf VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS tbl_cadastrar_usuario(
    id_usuario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_usuario VARCHAR(100),
    senha_usuario VARCHAR(100)
    repetir_senha VARCHAR(100)
    dt_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tbl_pesquisa_satisfacao (
                    id_pesquisa INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    atendimento VARCHAR(50),
                    qualidade VARCHAR(50),
                    satisfacao VARCHAR(50),
                    rapidez VARCHAR(50),
                    localizacao VARCHAR(50),
                    experiencia VARCHAR(50),
                    facilidade VARCHAR(50),
                    variedade VARCHAR(50),
                    ambiente VARCHAR(50),
                    recomendacao VARCHAR(50),
                    comentarios TEXT,
                    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );

CREATE TABLE u799109175_cestas_present.tbl_fale_conosco(
    id_fconosco INT AUTO_INCREMENT NOT null PRIMARY KEY,
    nome varchar(150),
    email varchar(150),
    mensagem text,
    dt_reg TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            );

GRANT ALL PRIVILEGES ON u799109175_dbflask_menu.* TO 'u799109175_dbflask_menu'@'%' IDENTIFIED BY 'Q1k2v1y5@2025';
FLUSH PRIVILEGES;


CREATE TABLE u799109175_cestas_present.tbl_pedidos (
    id_pedido INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_prod INT NOT NULL,
    valor_total DECIMAL(10,2),
    numero_mesa text,
    quantidade INT,
    dt_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valor_total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES tbl_cliente(id_cliente)
);


# Criar uma tabela relacionada entre a cliente e produto para detalhes do pedido

CREATE TABLE u799109175_cestas_present.tbl_detalhes_pedido (
    id_detalhe INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_prod INT NOT NULL,
    id_cliente INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    dt_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    nome_cliente VARCHAR(100),
    numero_mesa INT null,
    telefone VARCHAR(100),
    endereco TEXT,
    bairro VARCHAR(50),
    ponto_referencia TEXT,
    form_pgmto enum('dinheiro', 'cartao', 'pix') NOT NULL,
    tipo_consumo enum('No Local', 'Retira', 'Delivery') NOT NULL,
    observacao TEXT,

    FOREIGN KEY (id_pedido) REFERENCES tbl_pedidos(id_pedido),
    FOREIGN KEY (id_prod) REFERENCES tbl_prod(id_prod),
    FOREIGN KEY (id_cliente) REFERENCES tbl_cliente(id_cliente)
);

-- ============================================
-- VIEWs para Relatório de Pedidos
-- ============================================

CREATE OR REPLACE VIEW u799109175_cestas_present.vw_pedidos_fin AS
SELECT
    dp.id_pedido,
    dp.id_prod,
    dp.nome_prod AS nome_produto,

    dp.nome_cliente,
    dp.telefone,
    dp.dt_registro,
    dp.endereco,
    dp.bairro,

    dp.status_pedido,

    dp.form_pgmto,
    dp.tipo_consumo,

    SUM(dp.quantidade) AS qtde,
    SUM(dp.valor_total) AS valor_total

FROM u799109175_cestas_present.tbl_detalhes_pedido dp

JOIN u799109175_cestas_present.tbl_prod p
    ON dp.id_prod = p.id_prod

JOIN u799109175_cestas_present.tbl_pedidos pe
    ON dp.id_pedido = pe.id_pedido

GROUP BY
    dp.id_pedido,
    dp.id_prod,
    p.nome_prod,
    dp.nome_cliente,s
    dp.telefone,
    dp.dt_registro,
    dp.endereco,
    dp.bairro,
    dp.status_pedido,
    dp.form_pgmto,
    dp.tipo_consumo

ORDER BY dp.dt_registro DESC;

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
    FROM u799109175_cestas_present.tbl_detalhes_pedido pe
INNER JOIN u799109175_cestas_present.tbl_prod pr 
    ON pr.id_prod = pe.id_prod
INNER JOIN u799109175_cestas_present.tbl_pedidos ped
    ON ped.id_pedido = pe.id_pedido
ORDER BY pe.dt_registro DESC;

CREATE VIEW u799109175_cestas_present.vw_subgrupo AS 
SELECT
    pr.id_prod,
    pr.subgrupo,
    pe.id_pedido,
    SUM(pe.valor_total) AS total_valor
FROM u799109175_cestas_present.tbl_prod pr
INNER JOIN u799109175_cestas_present.tbl_pedidos pe
    ON pr.id_prod = pe.id_pedido
GROUP BY
        pr.subgrupo;

CREATE VIEW u799109175_cestas_present.vw_pedidos_bairro AS
SELECT
pe.id_pedido,
SUM(quantidade) as total_qtde,
sum(valor_total) AS total_valor,
pe.dt_registro,
cl.id_cliente,
cl.bairro,
cl.cidade,
cl.uf
FROM u799109175_cestas_present.tbl_detalhes_pedido pe
JOIN u799109175_cestas_present.tbl_cliente cl
ON pe.id_pedido = cl.id_cliente
GROUP BY
bairro;

CREATE TABLE IF NOT EXISTS tbl_entregadores(
    id_entregador INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_entregador VARCHAR(100),
    tipo_entregador enum('Próprio', 'Terceirizado') NOT NULL,
    habilitacao VARCHAR(50),
    tipo_cnh enum('A', 'B', 'C', 'D', 'E', 'AB','ACC') NOT NULL,
    validade_cnh DATE,
    endereco VARCHAR(200),
    bairro VARCHAR(50),
    cidade VARCHAR(50),
    uf VARCHAR(50),
    telefone VARCHAR(50),
    veiculo VARCHAR(50),
    ano_veiculo INT,
    cor VARCHAR(50),
    placa VARCHAR(20),
    ativo TINYINT DEFAULT 1,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE u799109175_cestas_present.tbl_pedidos_financeiro AS
SELECT
    dp.id_pedido,
    dp.id_prod,
    dp.nome_prod AS nome_produto,

    dp.nome_cliente,
    dp.telefone,
    dp.dt_registro,
    dp.endereco,
    dp.bairro,

    dp.status_pedido,

    dp.form_pgmto,
    dp.tipo_consumo,

    SUM(dp.quantidade) AS qtde,
    SUM(dp.valor_total) AS valor_total

FROM u799109175_cestas_present.tbl_detalhes_pedido dp

JOIN u799109175_cestas_present.tbl_prod p
    ON dp.id_prod = p.id_prod

JOIN u799109175_cestas_present.tbl_pedidos pe
    ON dp.id_pedido = pe.id_pedido

GROUP BY
    dp.id_pedido,
    dp.id_prod,
    dp.nome_prod,
    dp.nome_cliente,
    dp.telefone,
    dp.dt_registro,
    dp.endereco,
    dp.bairro,
    dp.status_pedido,
    dp.form_pgmto,
    dp.tipo_consumo

ORDER BY dp.dt_registro DESC;

CREATE TABLE IF NOT EXISTS u799109175_cestas_present.tbl_acomp_pedidos AS
SELECT
    pe.status_pedido,
    COUNT(*) AS qtde_pedidos,
    SUM(pe.valor_total) AS total_pedidos
FROM u799109175_cestas_present.tbl_pedidos_financeiro pe
GROUP BY pe.status_pedido;