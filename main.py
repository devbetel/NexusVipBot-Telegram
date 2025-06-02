from config.settings import dp, bot
import logging
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
import os
from utils.middleware import LoggingMiddleware
from dotenv import load_dotenv
from handlers import commands
import asyncio

load_dotenv()

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
dp.message.middleware(LoggingMiddleware())

# Inclui os routers
dp.include_router(commands.router)

# Configurações do Webhook (para produção)
WEBHOOK_PATH = "/webhook"
WEBHOOK_HOST = os.getenv("RENDER_EXTERNAL_HOSTNAME")  # Ou outra variável de host
WEBHOOK_URL = f"https://{WEBHOOK_HOST}{WEBHOOK_PATH}" if WEBHOOK_HOST else None

async def on_startup(bot):
    """Configura webhook se estiver em produção"""
    if WEBHOOK_URL:
        logger.info(f"Configurando webhook em: {WEBHOOK_URL}")
        await bot.delete_webhook()
        await bot.set_webhook(WEBHOOK_URL)
    else:
        logger.info("Modo: Polling (desenvolvimento local)")

async def start_webhook():
    """Inicia o servidor webhook"""
    app = web.Application()
    app.on_startup.append(lambda app: on_startup(bot))
    
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    
    return app

async def start_polling():
    """Inicia o bot em modo polling (local)"""
    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Iniciando o bot...")
    
    if WEBHOOK_HOST:
        # Modo produção (webhook)
        app = asyncio.run(start_webhook())
        web.run_app(
            app,
            host="0.0.0.0",
            port=int(os.getenv("PORT", "10000"))
        )
    else:
        # Modo desenvolvimento (polling)
        asyncio.run(start_polling())
    
    print("Bot iniciado com sucesso!")