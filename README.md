# 🛍️ Catálogo Digital | Sistema de Gerenciamento de Pedidos

Um sistema web moderno e intuitivo para gerenciamento de pedidos com integração WhatsApp, QR Code PIX e relatórios avançados.

---

## ✨ Recursos Principais

- Gestão de clientes e produtos  
- Carrinho de compras interativo  
- Pagamentos (Dinheiro, PIX, Cartão)  
- Integração com WhatsApp  
- Relatórios avançados (CSV/Excel)  
- Controle de usuários e permissões  
- Pesquisa de satisfação  

---

## 🚀 Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/Williamsrvs/Visibility_System.git
cd "Catálogo Digital"

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instale dependências
pip install -r requirements.txt

# Configure variáveis de ambiente
cp .env.example .env
nano .env   # edite com suas credenciais seguras

# Configure banco de dados
python setup_db.py
python create_views.py

# Inicie servidor
python app.py
# cestasepresentes
