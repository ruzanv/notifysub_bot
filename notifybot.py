import os
import time
import logging

from api_token import TOKEN_BOT_NOTIFY
from aiogram import Bot, Dispatcher, executor, types

TOKEN = TOKEN_BOT_NOTIFY

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=}, {time.asctime()}')
    await message.answer(f'Привет, {user_full_name}! Ты запустил бота помощника по управлению твоими подписками!')

@dp.message_handler(commands=['about'])
async def about_handler(message: types.Message):
    user_first_name = message.from_user.first_name
    await message.reply(f'Это чат-бот, который поможет тебе, {user_first_name}, следить за своими подписками.')
    await message.answer(f'Зачем это нужно? Все просто, сейчас существует большая проблема с управлением своих подписок. Часто мы забываем о том, что мы оформляли и в неожиданный момент у нас происходят списания средств за то, чем мы не пользуемся.')
    await message.answer(f'С помощью этого бота ты можешь добавлять свои текущие подписки в список, а бот будет напоминать тебе о скором списании средств по добавленной подписке.')

if __name__ == '__main__':
    executor.start_polling(dp)