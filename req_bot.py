import time
import logging

from api_token import TOKEN_BOT_NOTIFY
from aiogram import Bot, Dispatcher, executor, types

TOKEN = TOKEN_BOT_NOTIFY

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

async def on_startup(_):
    print(f'Бот вышел в онлайн в {time.asctime()}')