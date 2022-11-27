import logging
import time
from aiogram import types, Dispatcher

list_subs = []


async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=}, {time.asctime()}')
    await message.answer(f'Привет, {user_full_name}! Ты запустил бота помощника по управлению твоими подписками!')


async def about_handler(message: types.Message):
    user_first_name = message.from_user.first_name
    await message.reply(f'Это чат-бот, который поможет тебе, {user_first_name}, следить за своими подписками.')
    await message.answer(
        f'Зачем это нужно? Все просто, сейчас существует большая проблема с управлением своих подписок. Часто мы '
        f'забываем о том, что мы оформляли и в неожиданный момент у нас происходят списания средств за то, '
        f'чем мы не пользуемся.')
    await message.answer(
        f'С помощью этого бота ты можешь добавлять свои текущие подписки в список, а бот будет напоминать тебе о '
        f'скором списании средств по добавленной подписке.')


async def add_handler(message: types.Message):
    pass


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(about_handler, commands=['about'])
    dp.register_message_handler(add_handler, commands=['add'])
