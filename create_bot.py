from api_token import TOKEN_BOT_NOTIFY
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage

bot = Bot(token=TOKEN_BOT_NOTIFY)
dp = Dispatcher(bot=bot, storage=storage())
