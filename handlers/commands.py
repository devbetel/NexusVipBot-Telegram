from aiogram.filters import CommandStart, Command
from aiogram import Router
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

from config.settings import dp
import requests
from dotenv import load_dotenv
import os
from aiogram.handlers import CallbackQueryHandler
import mercadopago
load_dotenv()

#Cache do usuario


router = Router()

@router.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer(f"Olá, {message.from_user.full_name}! Eu sou o NexusVipBot um bot de assinaturas. Use /help para ver os comandos disponíveis. 🚀")


 # Cria o teclado inline com os botões

    
@router.message(Command("vip"))
async def vip_command(message: Message) -> None:
    #Cria os botões inline para os planos
    button1= InlineKeyboardButton(text="Básico", callback_data="basic_plan_button")
    button2= InlineKeyboardButton(text="Premium", callback_data="premium_plan_button")
    
    # Cria o teclado inline e adiciona os botões
    keyboard_inline= InlineKeyboardMarkup(inline_keyboard=[[button1, button2]])
    
    # Envia a mensagem com os planos e o teclado inline
    await message.reply("""
                        "
📌 Planos VIP (Demonstração):  
- BÁSICO: Acesso a conteúdos exclusivos (R$0,00).  
- PREMIUM: Grupo privado + suporte (R$0,00).  
[🔹 Selecione um plano para simular pagamento] 
""", reply_markup=keyboard_inline)
 
sdk= mercadopago.SDK(os.getenv("ACESS_TOKEN_MERCADOPAGO"))

async def create_payment_link(user_id: int, plan: str, price: float):
    preference_data = {
        "items": [
            {
                "title": f"Assinatura {plan}",
                "quantity": 1,
                "unit_price": float(price),  # Garanta que é float
                "currency_id": "BRL",
            }
        ],
        "payer": {
            "email": "test_user_{user_id}@testuser.com"  # Email único por usuário
        },
        "back_urls": {
            "success": "https://seusite.com/success",
            "failure": "https://seusite.com/failure",
            "pending": "https://seusite.com/pending"
        },
        "auto_return": "approved",
        "statement_descriptor": "NEXUSVIP",
        "external_reference": f"user_{user_id}_plan_{plan.lower()}",
    }

    try:
        preference_response = sdk.preference().create(preference_data)
        if 'response' in preference_response and 'sandbox_init_point' in preference_response['response']:
            return preference_response['response']['sandbox_init_point']
        else:
            print("Resposta completa da API:", preference_response)
            return None
    except Exception as e:
        print("Erro na API:", e)
        return None


   

@router.callback_query(lambda c: c.data in ["basic_plan_button", "premium_plan_button"])
async def handle_plan_buttons(callback: CallbackQuery):
    user = callback.from_user
    plan = "Básico" if callback.data == "basic_plan_button" else "Premium"
    price = 0.01  # Valor simulado
    
    payment_url = await create_payment_link(user.id, plan, price)
    
    if not payment_url:
        await callback.message.answer("❌ Temporariamente não podemos processar pagamentos. Tente novamente mais tarde.")
        return
    
    payment_button = InlineKeyboardButton(
        text="🔹 Pagar Agora (Simulação)",
        url=payment_url
    )
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[payment_button]])
    
    await callback.message.answer(
        f"💳 Você selecionou o plano {plan}.\n"
        "Clique no botão abaixo para simular o pagamento:",
        reply_markup=keyboard
    )
    await callback.answer()

@router.message(Command("acesso_vip"))
async def acesso_vip_command(message: Message) -> None:
      # Mensagem de resposta + link fictício
    resposta = (
        "🎉 **Acesso VIP Liberado!**\n\n"
        "Aqui está seu link exclusivo (demonstração):\n"
        "🔗 https://exemplo.com/vip-demo\n\n"
        "*Este é um teste para portfólio. Nenhum pagamento real foi processado.*"
    )

    # Teclado inline com um botão (opcional)
    teclado = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="👉 Acessar Conteúdo VIP", url="https://exemplo.com/vip-demo")],
            [InlineKeyboardButton(text="🗑️ Encerrar Sessão", callback_data="fim_demo")]
        ]
    )

    await message.answer(resposta, parse_mode="Markdown", reply_markup=teclado)
@router.message(Command("portfolio"))
async def portfolio_command(message: Message) -> None:

    # Mensagem de resposta + link fictício
    resposta = (
        "🌟 **Portfólio de Demonstração**\n\n"
        "Confira nosso portfólio de bots e serviços:\n"
        "🔗 https://lucasbeteldev.com.br\n\n"
        "*Este é um teste para portfólio. Nenhum pagamento real foi processado.*"
    )

    # Teclado inline com um botão (opcional)
    teclado = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="👉 Ver Portfólio", url="https://lucasbeteldev.com.br")],
            [InlineKeyboardButton(text="🗑️ Encerrar Sessão", callback_data="fim_demo")]
        ]
    )

    await message.answer(resposta, parse_mode="Markdown", reply_markup=teclado)
# Callback para encerrar a sessão VIP
@dp.callback_query(lambda c: c.data == "fim_demo")
async def encerrar_sessao(callback: types.CallbackQuery):
    await callback.message.edit_text("✅ Sessão VIP encerrada. Use /vip para recomeçar.")

@router.message(Command("help"))
async def help_command(message: Message) -> None:
    await message.answer("""
Comandos disponíveis:
/start - Inicia o bot e mostra uma mensagem de boas-vindas.
/vip - Exibe os planos VIP disponíveis e permite simular um pagamento.
/acesso_vip - Acesso direto aos planos VIP.
/help - Mostra esta mensagem de ajuda.
/portfolio - Exibe o portfólio de demonstração do bot.
""")
    