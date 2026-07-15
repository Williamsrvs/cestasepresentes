-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 14/07/2026 às 23:43
-- Versão do servidor: 11.8.8-MariaDB-log
-- Versão do PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `u799109175_cestas_present`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `tbl_acomp_pedidos`
--

CREATE TABLE `tbl_acomp_pedidos` (
  `status_pedido` text NOT NULL,
  `qtde_pedidos` bigint(21) NOT NULL,
  `total_pedidos` decimal(54,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tbl_cadastrar_usuario`
--

CREATE TABLE `tbl_cadastrar_usuario` (
  `id_usuario` int(11) NOT NULL,
  `nome_usuario` varchar(100) DEFAULT NULL,
  `senha_usuario` varchar(100) DEFAULT NULL,
  `repetir_senha` varchar(100) DEFAULT NULL,
  `dt_cadastro` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tbl_cliente`
--

CREATE TABLE `tbl_cliente` (
  `id_cliente` int(11) NOT NULL,
  `nome_cliente` varchar(100) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `endereco` text DEFAULT NULL,
  `bairro` varchar(50) DEFAULT NULL,
  `cidade` varchar(50) DEFAULT NULL,
  `uf` varchar(50) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `telefone` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tbl_detalhes_pedido`
--

CREATE TABLE `tbl_detalhes_pedido` (
  `id_detalhe` int(11) NOT NULL,
  `id_pedido` int(11) NOT NULL,
  `id_prod` int(11) NOT NULL,
  `nome_prod` varchar(155) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `quantidade` int(11) NOT NULL,
  `preco_unitario` decimal(10,2) NOT NULL,
  `dt_registro` timestamp NULL DEFAULT current_timestamp(),
  `nome_cliente` varchar(50) NOT NULL,
  `telefone` varchar(50) NOT NULL,
  `valor_total` decimal(10,2) NOT NULL,
  `numero_mesa` int(11) DEFAULT NULL,
  `endereco` text NOT NULL,
  `bairro` text NOT NULL,
  `ponto_referencia` text NOT NULL,
  `form_pgmto` text NOT NULL,
  `tipo_consumo` text NOT NULL,
  `observacao` text NOT NULL,
  `taxa_entrega` int(11) NOT NULL,
  `status_pedido` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tbl_entregadores`
--

CREATE TABLE `tbl_entregadores` (
  `id_entregador` int(11) NOT NULL,
  `nome_entregador` varchar(100) DEFAULT NULL,
  `tipo_entregador` enum('Próprio','Terceirizado') NOT NULL,
  `habilitacao` varchar(50) DEFAULT NULL,
  `tipo_cnh` enum('A','B','C','D','E','AB','ACC') NOT NULL,
  `validade_cnh` date DEFAULT NULL,
  `endereco` varchar(200) DEFAULT NULL,
  `bairro` varchar(50) DEFAULT NULL,
  `cidade` varchar(50) DEFAULT NULL,
  `uf` varchar(50) DEFAULT NULL,
  `telefone` varchar(50) DEFAULT NULL,
  `veiculo` varchar(50) DEFAULT NULL,
  `ano_veiculo` int(11) DEFAULT NULL,
  `cor` varchar(50) DEFAULT NULL,
  `placa` varchar(20) DEFAULT NULL,
  `ativo` tinyint(4) DEFAULT 1,
  `criado_em` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tbl_fale_conosco`
--

CREATE TABLE `tbl_fale_conosco` (
  `id_fconosco` int(11) NOT NULL,
  `nome` varchar(150) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `mensagem` text DEFAULT NULL,
  `dt_reg` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tbl_pedidos`
--

CREATE TABLE `tbl_pedidos` (
  `id_pedido` int(11) NOT NULL,
  `id_prod` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `quantidade` int(11) NOT NULL,
  `dt_registro` timestamp NULL DEFAULT current_timestamp(),
  `valor_total` decimal(10,2) NOT NULL,
  `numero_mesa` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tbl_pedidos_financeiro`
--

CREATE TABLE `tbl_pedidos_financeiro` (
  `id_pedido` int(11) NOT NULL,
  `id_prod` int(11) NOT NULL,
  `nome_prod` varchar(155) NOT NULL,
  `nome_cliente` varchar(50) NOT NULL,
  `telefone` varchar(50) NOT NULL,
  `dt_registro` timestamp NULL DEFAULT current_timestamp(),
  `endereco` text NOT NULL,
  `bairro` text NOT NULL,
  `status_pedido` text NOT NULL,
  `form_pgmto` text NOT NULL,
  `tipo_consumo` text NOT NULL,
  `qtde` decimal(32,0) DEFAULT NULL,
  `valor_total` decimal(32,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tbl_pesquisa_satisfacao`
--

CREATE TABLE `tbl_pesquisa_satisfacao` (
  `id_pesquisa` int(11) NOT NULL,
  `atendimento` varchar(50) DEFAULT NULL,
  `qualidade` varchar(50) DEFAULT NULL,
  `satisfacao` varchar(50) DEFAULT NULL,
  `rapidez` varchar(50) DEFAULT NULL,
  `localizacao` varchar(50) DEFAULT NULL,
  `experiencia` varchar(50) DEFAULT NULL,
  `facilidade` varchar(50) DEFAULT NULL,
  `variedade` varchar(50) DEFAULT NULL,
  `ambiente` varchar(50) DEFAULT NULL,
  `recomendacao` varchar(50) DEFAULT NULL,
  `comentarios` text DEFAULT NULL,
  `data_hora` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tbl_prod`
--

CREATE TABLE `tbl_prod` (
  `id_prod` int(11) NOT NULL,
  `nome_prod` varchar(100) NOT NULL,
  `descricao` text DEFAULT NULL,
  `valor` decimal(10,2) NOT NULL,
  `form_pgmto` varchar(50) DEFAULT NULL,
  `imagem_url` mediumblob DEFAULT NULL,
  `ativo` tinyint(4) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `subgrupo` varchar(50) NOT NULL,
  `status_promocao` varchar(50) NOT NULL,
  `dias_semana` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `vw_pedidos_bairro`
-- (Veja abaixo para a visão atual)
--
CREATE TABLE `vw_pedidos_bairro` (
`id_pedido` int(11)
,`quantidade` int(11)
,`valor_total` decimal(10,2)
,`dt_registro` timestamp
,`id_cliente` int(11)
,`bairro` varchar(50)
,`cidade` varchar(50)
,`uf` varchar(50)
);

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `vw_pedidos_detalhado`
-- (Veja abaixo para a visão atual)
--
CREATE TABLE `vw_pedidos_detalhado` (
`id_pedido` int(11)
,`id_detalhe` int(11)
,`nome_prod` varchar(100)
,`valor_unitario` decimal(10,2)
,`quantidade` int(11)
,`subtotal_item` decimal(10,2)
,`total_pedido` decimal(10,2)
,`nome_cliente` varchar(50)
,`telefone` varchar(50)
,`dt_registro` timestamp
);

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `vw_pedidos_fin`
-- (Veja abaixo para a visão atual)
--
CREATE TABLE `vw_pedidos_fin` (
`id_pedido` int(11)
,`id_prod` int(11)
,`nome_prod` varchar(100)
,`nome_cliente` varchar(50)
,`telefone` varchar(50)
,`dt_registro` timestamp
,`endereco` text
,`bairro` text
,`status_pedido` text
,`form_pgmto` text
,`tipo_consumo` text
,`qtde` decimal(32,0)
,`valor_total` decimal(32,2)
,`tx_entrega` decimal(3,2)
);

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `vw_resumo_pedidos_cliente`
-- (Veja abaixo para a visão atual)
--
CREATE TABLE `vw_resumo_pedidos_cliente` (
`nome_cliente` varchar(50)
,`telefone` varchar(50)
,`total_pedidos` bigint(21)
,`total_itens` bigint(21)
,`quantidade_total` decimal(32,0)
,`valor_total_cliente` decimal(32,2)
,`ultimo_pedido` timestamp
);

-- --------------------------------------------------------

--
-- Estrutura stand-in para view `vw_subgrupo`
-- (Veja abaixo para a visão atual)
--
CREATE TABLE `vw_subgrupo` (
`id_prod` int(11)
,`subgrupo` varchar(50)
,`id_pedido` int(11)
,`total_valor` decimal(32,2)
);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `tbl_cadastrar_usuario`
--
ALTER TABLE `tbl_cadastrar_usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- Índices de tabela `tbl_cliente`
--
ALTER TABLE `tbl_cliente`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Índices de tabela `tbl_detalhes_pedido`
--
ALTER TABLE `tbl_detalhes_pedido`
  ADD PRIMARY KEY (`id_detalhe`),
  ADD KEY `id_pedido` (`id_pedido`),
  ADD KEY `id_prod` (`id_prod`),
  ADD KEY `id_cliente` (`id_cliente`);

--
-- Índices de tabela `tbl_entregadores`
--
ALTER TABLE `tbl_entregadores`
  ADD PRIMARY KEY (`id_entregador`);

--
-- Índices de tabela `tbl_fale_conosco`
--
ALTER TABLE `tbl_fale_conosco`
  ADD PRIMARY KEY (`id_fconosco`);

--
-- Índices de tabela `tbl_pedidos`
--
ALTER TABLE `tbl_pedidos`
  ADD PRIMARY KEY (`id_pedido`);

--
-- Índices de tabela `tbl_pesquisa_satisfacao`
--
ALTER TABLE `tbl_pesquisa_satisfacao`
  ADD PRIMARY KEY (`id_pesquisa`);

--
-- Índices de tabela `tbl_prod`
--
ALTER TABLE `tbl_prod`
  ADD PRIMARY KEY (`id_prod`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `tbl_cadastrar_usuario`
--
ALTER TABLE `tbl_cadastrar_usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tbl_cliente`
--
ALTER TABLE `tbl_cliente`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tbl_detalhes_pedido`
--
ALTER TABLE `tbl_detalhes_pedido`
  MODIFY `id_detalhe` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tbl_entregadores`
--
ALTER TABLE `tbl_entregadores`
  MODIFY `id_entregador` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tbl_fale_conosco`
--
ALTER TABLE `tbl_fale_conosco`
  MODIFY `id_fconosco` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tbl_pedidos`
--
ALTER TABLE `tbl_pedidos`
  MODIFY `id_pedido` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tbl_pesquisa_satisfacao`
--
ALTER TABLE `tbl_pesquisa_satisfacao`
  MODIFY `id_pesquisa` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tbl_prod`
--
ALTER TABLE `tbl_prod`
  MODIFY `id_prod` int(11) NOT NULL AUTO_INCREMENT;

-- --------------------------------------------------------

--
-- Estrutura para view `vw_pedidos_bairro`
--
DROP TABLE IF EXISTS `vw_pedidos_bairro`;

CREATE ALGORITHM=UNDEFINED DEFINER=`u799109175_cestas_present`@`127.0.0.1` SQL SECURITY DEFINER VIEW `vw_pedidos_bairro`  AS SELECT `p`.`id_pedido` AS `id_pedido`, `p`.`quantidade` AS `quantidade`, `p`.`valor_total` AS `valor_total`, `p`.`dt_registro` AS `dt_registro`, `c`.`id_cliente` AS `id_cliente`, `c`.`bairro` AS `bairro`, `c`.`cidade` AS `cidade`, `c`.`uf` AS `uf` FROM (`tbl_pedidos` `p` join `tbl_cliente` `c` on(`p`.`id_pedido` = `c`.`id_cliente`)) ;

-- --------------------------------------------------------

--
-- Estrutura para view `vw_pedidos_detalhado`
--
DROP TABLE IF EXISTS `vw_pedidos_detalhado`;

CREATE ALGORITHM=UNDEFINED DEFINER=`u799109175_cestas_present`@`127.0.0.1` SQL SECURITY DEFINER VIEW `vw_pedidos_detalhado`  AS SELECT `pe`.`id_pedido` AS `id_pedido`, `pe`.`id_detalhe` AS `id_detalhe`, `pr`.`nome_prod` AS `nome_prod`, `pr`.`valor` AS `valor_unitario`, `pe`.`quantidade` AS `quantidade`, `pe`.`valor_total` AS `subtotal_item`, `ped`.`valor_total` AS `total_pedido`, `pe`.`nome_cliente` AS `nome_cliente`, `pe`.`telefone` AS `telefone`, `pe`.`dt_registro` AS `dt_registro` FROM ((`tbl_detalhes_pedido` `pe` join `tbl_prod` `pr` on(`pr`.`id_prod` = `pe`.`id_prod`)) join `tbl_pedidos` `ped` on(`ped`.`id_pedido` = `pe`.`id_pedido`)) ORDER BY `pe`.`dt_registro` DESC ;

-- --------------------------------------------------------

--
-- Estrutura para view `vw_pedidos_fin`
--
DROP TABLE IF EXISTS `vw_pedidos_fin`;

CREATE ALGORITHM=UNDEFINED DEFINER=`u799109175_cestas_present`@`127.0.0.1` SQL SECURITY DEFINER VIEW `vw_pedidos_fin`  AS SELECT `dp`.`id_pedido` AS `id_pedido`, `dp`.`id_prod` AS `id_prod`, `p`.`nome_prod` AS `nome_prod`, `dp`.`nome_cliente` AS `nome_cliente`, `dp`.`telefone` AS `telefone`, `dp`.`dt_registro` AS `dt_registro`, `dp`.`endereco` AS `endereco`, `dp`.`bairro` AS `bairro`, `dp`.`status_pedido` AS `status_pedido`, `dp`.`form_pgmto` AS `form_pgmto`, `dp`.`tipo_consumo` AS `tipo_consumo`, sum(`dp`.`quantidade`) AS `qtde`, sum(`dp`.`valor_total`) AS `valor_total`, CASE WHEN `dp`.`tipo_consumo` = 'Delivery' THEN 6.00 ELSE 0.00 END AS `tx_entrega` FROM ((`tbl_detalhes_pedido` `dp` join `tbl_prod` `p` on(`dp`.`id_prod` = `p`.`id_prod`)) join `tbl_pedidos` `pe` on(`dp`.`id_pedido` = `pe`.`id_pedido`)) GROUP BY `dp`.`id_pedido`, `dp`.`id_prod`, `p`.`nome_prod`, `dp`.`nome_cliente`, `dp`.`telefone`, `dp`.`dt_registro`, `dp`.`endereco`, `dp`.`bairro`, `dp`.`status_pedido`, `dp`.`form_pgmto`, `dp`.`tipo_consumo` ORDER BY `dp`.`dt_registro` DESC ;

-- --------------------------------------------------------

--
-- Estrutura para view `vw_resumo_pedidos_cliente`
--
DROP TABLE IF EXISTS `vw_resumo_pedidos_cliente`;

CREATE ALGORITHM=UNDEFINED DEFINER=`u799109175_cestas_present`@`127.0.0.1` SQL SECURITY DEFINER VIEW `vw_resumo_pedidos_cliente`  AS SELECT `pe`.`nome_cliente` AS `nome_cliente`, `pe`.`telefone` AS `telefone`, count(distinct `pe`.`id_pedido`) AS `total_pedidos`, count(`pe`.`id_detalhe`) AS `total_itens`, sum(`pe`.`quantidade`) AS `quantidade_total`, sum(`pe`.`valor_total`) AS `valor_total_cliente`, max(`pe`.`dt_registro`) AS `ultimo_pedido` FROM `tbl_detalhes_pedido` AS `pe` GROUP BY `pe`.`nome_cliente`, `pe`.`telefone` ORDER BY sum(`pe`.`valor_total`) DESC ;

-- --------------------------------------------------------

--
-- Estrutura para view `vw_subgrupo`
--
DROP TABLE IF EXISTS `vw_subgrupo`;

CREATE ALGORITHM=UNDEFINED DEFINER=`u799109175_cestas_present`@`127.0.0.1` SQL SECURITY DEFINER VIEW `vw_subgrupo`  AS SELECT `pr`.`id_prod` AS `id_prod`, `pr`.`subgrupo` AS `subgrupo`, `pe`.`id_pedido` AS `id_pedido`, sum(`pe`.`valor_total`) AS `total_valor` FROM (`tbl_prod` `pr` join `tbl_pedidos` `pe` on(`pr`.`id_prod` = `pe`.`id_pedido`)) GROUP BY `pr`.`subgrupo` ;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `tbl_detalhes_pedido`
--
ALTER TABLE `tbl_detalhes_pedido`
  ADD CONSTRAINT `tbl_detalhes_pedido_ibfk_1` FOREIGN KEY (`id_pedido`) REFERENCES `tbl_pedidos` (`id_pedido`),
  ADD CONSTRAINT `tbl_detalhes_pedido_ibfk_2` FOREIGN KEY (`id_prod`) REFERENCES `tbl_prod` (`id_prod`),
  ADD CONSTRAINT `tbl_detalhes_pedido_ibfk_3` FOREIGN KEY (`id_cliente`) REFERENCES `tbl_cliente` (`id_cliente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
