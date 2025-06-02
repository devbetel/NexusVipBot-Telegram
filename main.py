from config.settings import dp, bot
import logging
from aiohttp import web
import os
from utils.middleware import LoggingMiddleware
from dotenv import load_dotenv
from handlers import commands
import asyncio

load_dotenv()


#configuração básica de logging
logging.basicConfig(level=logging.DEBUG)
logging= logging.getLogger(__name__)
dp.message.middleware(LoggingMiddleware())

#inclui os routers
dp.include_router(commands.router)


async def main():
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    print("Iniciando o bot...")
    
    asyncio.run(main())
    print("Bot iniciado com sucesso!")