from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(
    token=os.getenv("BOT_TELEGRAM_TOKEN"),
    default= DefaultBotProperties(parse_mode= ParseMode.HTML))

dp= Dispatcher()