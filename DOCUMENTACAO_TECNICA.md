# 🔧 DOCUMENTAÇÃO TÉCNICA - Sistema de Pedidos v2.0

## 📋 Visão Geral

O sistema de pedidos foi corrigido e melhorado com as seguintes funcionalidades:
1. **Botão de Adicionar Produto** - FUNCIONANDO
2. **Gerador de QR Code PIX** - IMPLEMENTADO
3. **Integração com Novos Campos** - MELHORADA

---

## 🏗️ Arquitetura

### Frontend (HTML/CSS/JavaScript)
- **Arquivo:** `app/templates/pedidos.html`
- **Framework:** Vanilla JavaScript (sem dependências de framework)
- **Dependências externas:**
  - `https://cdn.jsdelivr.net/npm/qrcode@1.4.4/build/qrcode.min.js` (QR Code)
  - Google Fonts: Inter

### Backend (Requerido)
- **Endpoints utilizados:**
  - `POST /salvar_pedido` - Salvar pedido no banco de dados
  - `POST /enviar_whatsapp` - Gerar link wa.me para WhatsApp

---

## 📊 Fluxo de Dados

```
┌─────────────────────────────────────────────────────────────┐
│                   TELA DE PEDIDOS                            │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  1. Seleção de Cliente                                      │
│     └─ Carrega telefone automaticamente                     │
│     └─ Carrega dados do banco de dados                      │
│                                                               │
│  2. Preenchimento de Informações                            │
│     ├─ Endereço                                             │
│     ├─ Bairro                                               │
│     ├─ Ponto de Referência                                  │
│     ├─ Forma de Pagamento                                   │
│     ├─ Tipo de Consumo                                      │
│     └─ Telefone (auto-formatado)                            │
│                                                               │
│  3. Seleção de Produtos                                     │
│     └─ Carrega lista de produtos (templates Jinja2)         │
│     └─ Detecta preço automaticamente                        │
│     └─ Calcula subtotal                                     │
│                                                               │
│  4. Carrinho de Compras (em JavaScript)                     │
│     ├─ Mantém lista de produtos adicionados                 │
│     ├─ Atualiza totais em tempo real                        │
│     └─ Gera QR Code PIX dinamicamente                       │
│                                                               │
│  5. Ações do Usuário                                         │
│     ├─ Enviar via WhatsApp                                  │
│     │   └─ Chama POST /enviar_whatsapp                      │
│     │   └─ Abre link wa.me                                  │
│     └─ Imprimir Pedido                                      │
│         └─ Chama POST /salvar_pedido                        │
│         └─ Abre janela de impressão                         │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔌 Endpoints de API

### 1. POST /salvar_pedido

**Descrição:** Salva o pedido no banco de dados

**Payload (JSON):**
```json
{
  "carrinho": [
    {
      "id": 1234567890,
      "produtoId": 5,
      "nome": "Hambúrguer Caseiro",
      "valor": 18.00,
      "quantidade": 2,
      "subtotal": 36.00
    }
  ],
  "id_cliente": "123",
  "nome_cliente": "João Silva",
  "telefone_cliente": "(85) 98765-4321",
  "numero_mesa": "5"
}
```

**Resposta (sucesso):**
```json
{
  "status": "sucesso",
  "id_pedido": 12345,
  "mensagem": "Pedido salvo com sucesso",
  "valor_total": 45.00
}
```

**Resposta (erro):**
```json
{
  "status": "erro",
  "mensagem": "Erro ao salvar pedido"
}
```

### 2. POST /enviar_whatsapp

**Descrição:** Gera link wa.me para envio via WhatsApp

**Payload (JSON):**
```json
{
  "whatsapp_numero": "5582981090042",
  "mensagem": "*NOVO PEDIDO #12345*\n\n👤 *Cliente:* João Silva\n..."
}
```

**Resposta (sucesso):**
```json
{
  "status": "sucesso",
  "url_whatsapp": "https://wa.me/5582981090042?text=...",
  "mensagem": "Link gerado com sucesso"
}
```

**Resposta (erro):**
```json
{
  "status": "erro",
  "mensagem": "Erro ao gerar link"
}
```

---

## 🎯 Variáveis JavaScript Globais

### Configuração (editável)
```javascript
// Linha ~1065 - Configure estes valores:
const CHAVE_PIX = '00000000000000000000000';      // Sua chave PIX
const NOME_BENEFICIARIO = 'NOME DO LOJISTA';      // Seu nome/razão social

// Linha ~812 - Configure o número do lojista:
const WHATSAPP_LOJISTA = '5582981090042';         // Seu número WhatsApp
```

### Estado da Aplicação
```javascript
let carrinho = [];              // Array com produtos selecionados
let productCounter = 0;         // Contador de campos de produto
```

---

## 🔄 Fluxo de Processos

### 1. Adicionar Produto

```javascript
// Usuário clica no botão
btnAddProduct.addEventListener('click', addProductField)

// Função cria novo campo
function addProductField() {
  // Cria elemento HTML novo
  // Adiciona event listeners
  // Exibe na tela
}

// Usuário seleciona produto
selectElement.addEventListener('change', updatePrice)

// Preço é preenchido automaticamente
function updatePrice(selectElement) {
  // Obtém preço do atributo data-price
  // Atualiza field readonly
}

// Usuário clica "Adicionar ao Pedido"
button.addEventListener('click', addToCart)

// Produto é adicionado ao array carrinho
function addToCart(button) {
  // Valida dados
  // Adiciona ou atualiza carrinho
  // Atualiza interface
}
```

### 2. Atualizar Carrinho

```javascript
function updateCartDisplay() {
  // Calcula totais
  // Atualiza painel direito
  // Chama updateQRCode()
}

function updateQRCode(valor) {
  // Verifica se valor > 0
  // Se sim: Gera novo QR Code
  // Se não: Oculta container
}
```

### 3. Enviar via WhatsApp

```javascript
whatsappBtn.addEventListener('click', async function(e) {
  // 1. Valida dados do cliente
  const customerInfo = validateCustomerInfo()
  
  // 2. Salva pedido no banco
  const saveResponse = await fetch('/salvar_pedido', {...})
  
  // 3. Monta mensagem formatada
  // Inclui todos os campos:
  // - Cliente, Telefone, Endereço, Bairro
  // - Ponto de Referência, Forma de Pagamento
  // - Tipo de Consumo, Produtos, Total
  
  // 4. Gera link wa.me
  const whatsappResponse = await fetch('/enviar_whatsapp', {...})
  
  // 5. Abre em nova aba
  window.open(whatsappResult.url_whatsapp, '_blank')
})
```

### 4. Imprimir Pedido

```javascript
printBtn.addEventListener('click', async function () {
  // 1. Salva pedido no banco
  const response = await fetch('/salvar_pedido', {...})
  
  // 2. Gera HTML de impressão
  const printWindow = window.open('', '_blank', '...')
  printWindow.document.write(html)
  
  // 3. Abre diálogo de impressão
  printWindow.print()
  
  // 4. Após imprimir, recarrega página
  printWindow.onafterprint = () => {
    window.location.href = '/pedidos'
  }
})
```

---

## 🎯 Detecção de Produtos (Template Jinja2)

O arquivo utiliza variáveis Jinja2 para carregar dados do backend:

```html
<!-- Carrega dropdown de clientes -->
{% for cliente in clientes %}
  <option value="{{ cliente['id_cliente'] }}" data-phone="{{ cliente['telefone'] }}">
    {{ cliente['nome_cliente'] }}
  </option>
{% endfor %}

<!-- Carrega array de produtos em JavaScript -->
{% for produto in produtos %}
  { 
    id: {{ produto['id_prod'] }}, 
    nome: "{{ produto['nome_prod'] }}", 
    valor: {{ produto['valor'] }} 
  }
{% endfor %}
```

**Esperado do backend:**
- `clientes`: Lista com campos `id_cliente`, `nome_cliente`, `telefone`
- `produtos`: Lista com campos `id_prod`, `nome_prod`, `valor`

---

## 🔐 Validações Frontend

### Validação de Cliente
```javascript
function validateCustomerInfo() {
  // Verifica se cliente foi selecionado
  // Verifica se telefone foi digitado
  // Remove formatação do telefone
  // Retorna objeto com dados validados
}
```

### Validação de Produto
```javascript
function addToCart(button) {
  // Verifica se produto foi selecionado
  // Verifica se quantidade é > 0
  // Verifica se valor é > 0
  // Impede adição se validação falhar
}
```

---

## 📋 Campos Capturados

### Informações do Cliente
| Campo | ID HTML | Tipo | Obrigatório | Fonte |
|-------|---------|------|-------------|-------|
| Cliente | `customerSelect` | select | Sim | Banco de Dados |
| Endereço | `customerAddress` | text | Não | Entrada Manual |
| Bairro | `customerBairro` | text | Não | Entrada Manual |
| Ponto Ref. | `customerReferencia` | text | Não | Entrada Manual |
| Form. Pag. | `form_pgmto` | select | Sim | Entrada Manual |
| Tipo Consumo | `tipo_consumo` | select | Sim | Entrada Manual |
| Telefone | `customerPhone` | tel | Sim | Auto-preenchido |
| Nº Mesa | `tableNumber` | number | Não | Entrada Manual |

### Informações do Produto
| Campo | ID Class | Tipo | Obrigatório |
|-------|----------|------|-------------|
| Produto | `product-select` | select | Sim |
| Quantidade | `qty-input` | number | Sim |
| Valor Unit. | `price-input` | number | Não (preenchido) |
| Subtotal | `subtotal-display` | text | Não (calculado) |

---

## 🎨 Estilos CSS Principais

### Componentes Principais
- `.header` - Cabeçalho com título
- `.main-container` - Container principal (flex 2 colunas)
- `.left-panel` - Painel esquerdo (seleção de produtos)
- `.right-panel` - Painel direito (resumo e QR Code)
- `.product-item` - Item de produto individual
- `.qrcodeContainer` - Container do QR Code PIX
- `.btn-add-product` - Botão de adicionar produto
- `.btn-checkout` - Botões de ação

### Responsividade
- Em telas < 1024px: Layout muda para coluna única
- Painéis se ajustam automaticamente
- QR Code mantém tamanho e visibilidade

---

## 🔍 Debug/Troubleshooting

### Console JavaScript
Para verificar o estado atual:
```javascript
// No console do navegador (F12):
console.log(carrinho);           // Ver carrinho atual
console.log(CHAVE_PIX);          // Ver chave PIX configurada
console.log(produtosDisponiveis); // Ver produtos carregados
```

### Erros Comuns
1. **"Cannot read property 'getElementById'"**
   - Pode haver HTML com ID faltando
   - Verifique IDs dos elementos

2. **"QR Code não aparece"**
   - Verifique se `CHAVE_PIX` está configurada
   - Verifique se valor do carrinho > 0

3. **"WhatsApp não abre"**
   - Verifique se `WHATSAPP_LOJISTA` está configurado
   - Tente em outro navegador

---

## 📦 Dependências

### Bibliotecas Externas
```html
<!-- QR Code Generator -->
<script src="https://cdn.jsdelivr.net/npm/qrcode@1.4.4/build/qrcode.min.js"></script>

<!-- Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
```

### Compatibilidade
- **Navegadores suportados:**
  - Chrome/Edge 90+
  - Firefox 88+
  - Safari 14+
  - Opera 76+

- **JavaScript versão:** ES6+ (suporta async/await, spread operator, etc.)

---

## 📝 Notas de Desenvolvimento

### Possíveis Melhorias Futuras
1. Adicionar validação de CPF/CNPJ para forma de pagamento
2. Integrar com API real do PIX (DICT)
3. Adicionar autenticação de usuário
4. Implementar histórico de pedidos
5. Adicionar opcionalidade de desconto/taxa
6. Notificação em tempo real do pedido

### Código Limpo
- Sem dependências desnecessárias
- Nomenclatura clara e consistente
- Comentários em pontos críticos
- Tratamento de erros adequado

---

**Documentação:** DOCUMENTACAO_TECNICA.md  
**Versão:** 1.0  
**Data:** 10 de janeiro de 2026  
**Manutenção:** Consulte este documento ao fazer alterações

---

## ✅ Checklist de Implementação Backend

Se você está implementando o backend, verifique:

- [ ] Endpoint `/salvar_pedido` implementado
- [ ] Endpoint `/enviar_whatsapp` implementado
- [ ] Banco de dados com tabelas `pedidos` e `itens_pedido`
- [ ] Validação de dados no backend
- [ ] Logging de pedidos
- [ ] Tratamento de erros apropriado
- [ ] CORS habilitado se necessário
- [ ] Rate limiting implementado

---

**Fim da Documentação Técnica**
