from api_token import TOKEN_BOT_NOTIFY
from aiogram import Bot, Dispatcher

bot = Bot(token=TOKEN_BOT_NOTIFY)
dp = Dispatcher(bot=bot)
