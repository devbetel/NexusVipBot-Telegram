# NexusVIPBot - Bot de Assinaturas VIP (Demo)  

🤖 **Sobre o Projeto**:  
Bot educativo para portfólio que simula um sistema de assinaturas VIP no Telegram, com:  
- Integração com **Mercado Pago Sandbox** (pagamentos fictícios).  
- Automação de respostas e comandos via `aiogram`.  
- Webhooks para deploy em cloud (Render/Heroku).  

🔧 **Tecnologias**:  
`Python` `aiogram` `Mercado Pago API` `Render`  

🚀 **Objetivo**:  
Demonstrar habilidades em:  
- Bots Telegram com automação profissional.  
- Integração de APIs de pagamento.  
- Deploy de serviços em cloud.  

📌 **Aviso**:  
Este é um projeto **100% educativo**. Nenhum pagamento real é processado.  .

![Demo Preview](https://img.shields.io/badge/Status-Demo_Project-blue) 
![Python](https://img.shields.io/badge/Python-3.10%2B-yellowgreen)

---

## 🔥 Funcionalidades
- Fluxo completo de "assinatura VIP" (simulado).
- Integração com **Mercado Pago Sandbox** (pagamentos fictícios).
- Comandos intuitivos (`/vip`, `/acesso_vip`, etc).
- Painel de interação com botões inline.

---

## 🛠️ Como Usar (Localmente)

### Pré-requisitos
- Python 3.10+
- Conta no [Mercado Pago Developers](https://www.mercadopago.com.br/developers)
- Token do Bot do Telegram ([@BotFather](https://t.me/BotFather))

### Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/NexusVIPBot.git
   cd NexusVIPBot
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente (`.env`):
   ```env
   TELEGRAM_BOT_TOKEN=seu_token_aqui
   ACESS_TOKEN_MERCADOPAGO=seu_access_token_mp
   ```

4. Execute o bot:
   ```bash
   python main.py
   ```

---

## 📋 Comandos do Bot
| Comando       | Descrição                          |
|---------------|-----------------------------------|
| `/start`      | Mensagem de boas-vindas.          |
| `/vip`        | Mostra planos de assinatura.      |
| `/acesso_vip` | Simula acesso pós-pagamento.      |
| `/portfolio`  | Link para o portfólio.            |
| `/help`       | Lista todos os comandos.          |

---


## 📌 Personalização
- Substitua `https://exemplo.com/vip-demo` no código por um link real do seu portfólio.
- Altere os textos em `messages.py` (se separar em arquivo).

---


## 👨‍💻 Autor
[Lucas L. Betel](https://github.com/seu-usuario)  
[Meu Portfólio](https://lucasbeteldev.com.br)  

```