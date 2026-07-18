# 🚀 GUIA DE USO - Sistema de Pedidos Corrigido

## ✅ O que foi corrigido?

### 1. **Botão de Adicionar Produto - FUNCIONANDO**
   - ✅ Clique agora funciona perfeitamente
   - ✅ Permite adicionar múltiplos produtos

### 2. **QR Code PIX - IMPLEMENTADO**
   - ✅ Aparece automaticamente ao adicionar produtos
   - ✅ Mostra valor total com QR Code
   - ✅ Campo de cópia e cola para PIX manual

### 3. **Campos do Cliente - TODOS FUNCIONANDO**
   - ✅ Endereço
   - ✅ Bairro
   - ✅ Ponto de Referência (ID corrigido)
   - ✅ Forma de Pagamento
   - ✅ Tipo de Consumo

---

## 📖 PASSO A PASSO DE USO

### 🏪 Para o Lojista/Operador

#### **CONFIGURAÇÃO INICIAL (fazer uma vez)**
1. Abra `app/templates/pedidos.html`
2. Procure por (linha ~1065):
   ```javascript
   const CHAVE_PIX = '00000000000000000000000';
   const NOME_BENEFICIARIO = 'NOME DO LOJISTA';
   ```
3. Altere para seus dados:
   ```javascript
   const CHAVE_PIX = '82987654321'; // Seu CPF
   const NOME_BENEFICIARIO = 'LANCHONETE DELICIA'; // Seu nome
   ```

#### **USAR O SISTEMA**
1. **Selecione o Cliente**
   - Clique em "Selecione um cliente..."
   - Escolha ou crie novo cliente

2. **Preencha os Dados do Cliente**
   - Endereço: [digite o endereço completo]
   - Bairro: [escolha o bairro]
   - Ponto de Referência: [ex: próximo à padaria]
   - Forma de Pagamento: [Dinheiro/Pix/Cartão]
   - Tipo de Consumo: [No Local/Delivery/Retirada]
   - Telefone: [será preenchido automaticamente do cliente]

3. **Adicione Produtos**
   - Clique em "+ Adicionar Produto"
   - Selecione o produto no dropdown
   - Digite a quantidade
   - O preço será preenchido automaticamente
   - Clique em "Adicionar ao Pedido"

4. **Veja o Resumo**
   - No painel direito aparecerá:
     - Valor Total
     - **QR Code PIX** (escaneável)
     - Chave PIX para cópia e cola

5. **Enviar ao Cliente**
   - **Opção A:** Clique em "📱 Enviar via WhatsApp"
     - Abre o WhatsApp com a mensagem completa
     - Mostra QR Code para pagamento
   
   - **Opção B:** Clique em "🖨️ Imprimir Pedido"
     - Abre a janela de impressão
     - Salva no banco de dados

---

## 🎯 EXEMPLO PRÁTICO

### Cenário: Cliente quer pedir 2 hambúrgueres + 1 refrigerante

```
1. Selecione o cliente: João Silva

2. Preencha os dados:
   - Endereço: Rua das Flores, 123
   - Bairro: Centro
   - Ponto de Referência: Perto do banco
   - Forma de Pagamento: PIX
   - Tipo de Consumo: Delivery
   - Telefone: (85) 98765-4321

3. Clique em "+ Adicionar Produto"
   - Selecione: Hambúrguer Caseiro
   - Quantidade: 2
   - Clique "Adicionar ao Pedido"

4. Clique em "+ Adicionar Produto" novamente
   - Selecione: Refrigerante 2L
   - Quantidade: 1
   - Clique "Adicionar ao Pedido"

5. Veja no painel direito:
   - Valor Total: R$ 45,00
   - QR Code: [código gerado]

6. Clique em "📱 Enviar via WhatsApp"
   - WhatsApp abre automaticamente
   - Mensagem mostra:
     * Nome do cliente
     * Endereço
     * Produtos (com quantidades)
     * Valor total
     * Instruções para PIX

7. Cliente escaneia o QR Code e paga!
```

---

## 📱 O QUE O CLIENTE VÊ NO WhatsApp

```
*NOVO PEDIDO #12345*

👤 *Cliente:* João Silva
📱 *Telefone:* (85) 98765-4321
🏠 *Endereço:* Rua das Flores, 123
🏘️ *Bairro:* Centro
🗺️ *Ponto de Referência:* Perto do banco
💳 *Forma de Pagamento:* PIX
🍽️ *Tipo de Consumo:* Delivery

*📋 Itens do Pedido:*
1. Hambúrguer Caseiro
   └ Qtd: 2 x R$ 18,00
   └ Subtotal: R$ 36,00

2. Refrigerante 2L
   └ Qtd: 1 x R$ 9,00
   └ Subtotal: R$ 9,00

*💰 TOTAL: R$ 45,00*

_Pedido gerado via Catálogo Digital_
```

---

## 🔴 DÚVIDAS FREQUENTES

### "O QR Code apareceu mas não funciona"
**Solução:**
- Verifique se a chave PIX está corretamente configurada
- Aguarde o carregamento completo (pode levar 2-3 segundos)

### "O WhatsApp não abre"
**Solução:**
- Verifique se o WhatsApp está instalado no computador
- Se não estiver, copie a mensagem manualmente

### "Aparecem 2 botões 'Adicionar Produto'"
**Solução:**
- Atualize o navegador (Ctrl + F5 ou Cmd + Shift + R)

### "Não consigo imprimir o pedido"
**Solução:**
- Verifique se tem uma impressora configurada
- Tente imprimir como PDF

### "Campo de Ponto de Referência não aparece"
**Solução:**
- Atualize o navegador (Ctrl + F5)
- Limpe o cache do navegador

---

## 💡 DICAS ÚTEIS

### ✅ Ative a Cópia e Cola do PIX
- Campo de chave PIX ao lado do QR Code
- Clique para copiar automaticamente
- Cole na transferência manual

### ✅ Use Nomes Descritivos
- Exemplo: "Hambúrguer Caseiro com Queijo e Bacon" (em vez de só "Hambúrguer")

### ✅ Sempre Confirme o Cliente
- Verifique se o endereço está correto antes de enviar
- Confira o telefone do cliente

### ✅ Economize Papel
- Imprima apenas se necessário
- Considere usar QR Code no WhatsApp

---

## 🔧 CONFIGURAÇÕES IMPORTANTES

### Localização das Configurações:
**Arquivo:** `app/templates/pedidos.html`

### 1. Chave PIX (linha ~1065)
```javascript
const CHAVE_PIX = '82987654321';
const NOME_BENEFICIARIO = 'LANCHONETE DELICIA';
```

### 2. Número WhatsApp do Lojista (linha ~812)
```javascript
const WHATSAPP_LOJISTA = '5582981090042'; // Seu número
```

---

## 📞 CONTATO

Para dúvidas ou problemas, consulte:
- [CONFIGURACAO_PIX.md](CONFIGURACAO_PIX.md) - Configuração detalhada
- [CORRECOES_PEDIDOS_v2.md](CORRECOES_PEDIDOS_v2.md) - Relatório técnico

---

**Versão:** 2.0  
**Data:** 10 de janeiro de 2026  
**Status:** ✅ PRONTO PARA USO

🎉 **Aproveite o novo sistema de pedidos!**
