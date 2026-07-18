# 🧪 CHECKLIST DE TESTES - FLUXO DE PEDIDOS

**Instruções:** Siga cada passo e marque com ✅ quando completar

---

## 📋 TESTE 1: Botão "Adicionar Produto"

### Pré-requisitos
- [ ] Abrir página de pedidos: `http://seu-app/pedidos`
- [ ] Abrir DevTools (F12)
- [ ] Ir para aba **Console**

### Testes
- [ ] Procure pela mensagem: **"✅ Sistema inicializado com sucesso!"**
- [ ] Se não vir, verifique se há erro logo acima
- [ ] Clique no botão **"+ Adicionar Produto"**
- [ ] Esperado: Um novo campo de produto aparece na lista

### Validação
- [ ] Console mostra: **"✅ Botão encontrado: <button...>"**
- [ ] Console mostra: **"✅ Event listener registrado com sucesso"**
- [ ] Novo campo aparece ao clicar no botão

**Resultado:** [ ] ✅ PASSOU  [ ] ❌ FALHOU

Se falhou, copie o erro do console e compartilhe.

---

## 🛒 TESTE 2: Adicionar Produtos ao Carrinho

### Procedimento
- [ ] Com a página aberta, clique em "+ Adicionar Produto"
- [ ] No novo campo, clique no dropdown de produtos
- [ ] Selecione: **"Coxinha de Frango com Catupiry"** (R$ 4,00)
- [ ] Defina quantidade: **2**
- [ ] Clique em "+ Adicionar ao Carrinho"
- [ ] Verifique se o produto aparece no painel direito
- [ ] Repita para adicionar outro produto diferente

### Validação
- [ ] Pelo menos 2 produtos diferentes no carrinho
- [ ] Quantidade está correta
- [ ] Valor unitário está exibindo
- [ ] Subtotal está calculando corretamente (qtd × preço)

**Resultado:** [ ] ✅ PASSOU  [ ] ❌ FALHOU

---

## 📱 TESTE 3: QR Code PIX

### Procedimento
- [ ] Com produtos no carrinho, olhe para o **painel direito** (área de resumo)
- [ ] Procure pela seção **"💳 QR Code PIX"**
- [ ] Verifique se um **QR Code visual** apareceu
- [ ] Verifique se o **valor total está correto**

### Validação
- [ ] QR Code é uma imagem quadrada em preto e branco
- [ ] Está visível e nítido
- [ ] O valor mostrado é a soma de todos os produtos

### Teste Dinâmico
- [ ] Adicione outro produto ao carrinho
- [ ] O QR Code deve **atualizar automaticamente**
- [ ] O valor deve aumentar
- [ ] Remova um produto
- [ ] O QR Code deve atualizar novamente para valor menor

**Resultado:** [ ] ✅ PASSOU  [ ] ❌ FALHOU

Se não aparecer, verifique no console se há erro relacionado a "QRCode".

---

## 📋 TESTE 4: Preenchimento do Formulário

### Dados de Teste
```
Cliente:              JOÃO SILVA
Telefone:             (82) 98109-0042
Endereço:             Rua das Flores, 123
Bairro:               Ponta Verde
Ponto de Referência:  Perto do Banco Bradesco
Número da Mesa:       5
Forma de Pagamento:   PIX
Tipo de Consumo:      ENTREGA
```

### Procedimento
- [ ] Clique no dropdown de **Cliente** e selecione um cliente
- [ ] Ou crie um novo cliente se necessário
- [ ] Preencha **Telefone** (deve auto-preencher se cliente existir)
- [ ] Preencha **Endereço**
- [ ] Preencha **Bairro**
- [ ] Preencha **Ponto de Referência**
- [ ] Defina **Número da Mesa** (opcional)
- [ ] Selecione **Forma de Pagamento**
- [ ] Selecione **Tipo de Consumo**

### Validação
- [ ] Todos os campos preenchidos corretamente
- [ ] Telefone está formatado com parênteses e hífen
- [ ] Nenhum campo obrigatório está vazio

**Resultado:** [ ] ✅ PASSOU  [ ] ❌ FALHOU

---

## 🖨️ TESTE 5: Imprimir Pedido (Salvamento no Banco)

### Procedimento
1. [ ] Com formulário preenchido e produtos no carrinho
2. [ ] Clique no botão **"🖨️ Imprimir Pedido"**
3. [ ] Verifique a resposta:
   - [ ] Um alerta deve aparecer: **"✅ Pedido #XX Salvo com Sucesso!"**
4. [ ] Uma janela de impressão deve abrir
5. [ ] Clique em **"Cancelar"** ou feche a janela
6. [ ] Verifique se o carrinho foi **limpo** (agora vazio)

### Validação no Banco de Dados

Abra seu gerenciador MySQL e execute:

```sql
SELECT * FROM tbl_detalhes_pedido 
WHERE id_pedido = (SELECT MAX(id_pedido) FROM tbl_detalhes_pedido)
ORDER BY id_pedido DESC LIMIT 1;
```

Verifique se os seguintes campos estão **preenchidos**:
- [ ] `endereco` - Endereço do cliente
- [ ] `bairro` - Bairro do cliente
- [ ] `ponto_referencia` - Ponto de referência
- [ ] `form_pgmto` - Forma de pagamento (PIX)
- [ ] `tipo_consumo` - Tipo de consumo (ENTREGA)

**Resultado:** [ ] ✅ PASSOU  [ ] ❌ FALHOU

Se falhou, verifique:
- Console para erros JavaScript
- Status HTTP da requisição (Network tab)
- Se a rota `/salvar_pedido` está respondendo

---

## 📱 TESTE 6: Enviar via WhatsApp

### Procedimento
1. [ ] **Limpe o carrinho** ou atualize a página
2. [ ] Adicione novamente produtos (pelo menos 1)
3. [ ] Preencha o formulário com os dados do cliente
4. [ ] Clique no botão **"📱 Enviar via WhatsApp"**

### Esperado
- [ ] Alerta apareça: **"✅ Pedido #XX Salvo!"**
- [ ] Uma aba do WhatsApp abre automaticamente
- [ ] A mensagem contém:
  - [ ] ID do pedido real (ex: #56, não #0 ou undefined)
  - [ ] Nome do cliente
  - [ ] Endereço
  - [ ] Bairro
  - [ ] Produtos e quantidades
  - [ ] Valor total
  - [ ] Forma de pagamento

### Validação no Banco

Execute a mesma query acima e verifique se um novo pedido foi criado.

**Resultado:** [ ] ✅ PASSOU  [ ] ❌ FALHOU

---

## 🎯 TESTE 7: Fluxo Completo (Sem Erros)

### Procedimento
1. [ ] Atualize a página (F5)
2. [ ] Clique "+ Adicionar Produto" 5 vezes
3. [ ] Adicione diferentes produtos ao carrinho
4. [ ] Preencha formulário completamente
5. [ ] Clique "Imprimir Pedido"
6. [ ] Feche a janela de impressão
7. [ ] Atualize novamente (F5)
8. [ ] Repita com "Enviar via WhatsApp"

### Validação
- [ ] Nenhum erro no console (F12)
- [ ] Nenhum alerta de erro
- [ ] Cada pedido foi salvo com sucesso
- [ ] Pedidos aparecem no banco de dados

**Resultado:** [ ] ✅ PASSOU  [ ] ❌ FALHOU

---

## 📊 RESUMO FINAL

### Testes Completados
- [ ] Teste 1: Botão Adicionar Produto
- [ ] Teste 2: Adicionar Produtos ao Carrinho
- [ ] Teste 3: QR Code PIX
- [ ] Teste 4: Preenchimento do Formulário
- [ ] Teste 5: Imprimir Pedido
- [ ] Teste 6: Enviar via WhatsApp
- [ ] Teste 7: Fluxo Completo

### Resultado Geral
- [ ] ✅ **TUDO PASSOU** - Sistema está pronto para produção!
- [ ] ⚠️ **ALGUNS FALHOS** - Veja detalhes abaixo
- [ ] ❌ **CRÍTICO** - Precisar de suporte

### Se Houver Falhas

Para cada teste que falhou, forneça:

1. **Número do teste:** (ex: Teste 3)
2. **Descrição do problema:** (ex: QR Code não aparece)
3. **Screenshot:** (se possível)
4. **Erro do console:** (F12 > Console, copie o erro exato)
5. **Passos para reproduzir:** (detalhe exatamente o que fez)

---

**Última atualização:** 2024-01-10  
**Versão:** 1.0  
**Status:** ✅ Pronto para testes
