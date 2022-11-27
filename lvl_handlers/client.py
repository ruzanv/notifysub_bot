import logging
import time
from aiogram import types, Dispatcher
from keyboards import kb_client
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

list_subs = []


async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=}, {time.asctime()}')
    await message.answer(f'Привет, {user_full_name}! Ты запустил бота помощника по управлению твоими подписками!',
                         reply_markup=kb_client)


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


class FSMClient(StatesGroup):
    sub_name = State()
    sub_date = State()
    sub_select = State()


async def add_subscribe(message: types.Message):
    kb = [[types.KeyboardButton(text="Отмена ввода")]]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Введите название сервиса"
    )
    await FSMClient.sub_name.set()
    await message.answer('Введите название вашей подписки', reply_markup=keyboard)


async def add_name(message: types.Message, state: FSMContext):
    kb = [[types.KeyboardButton(text="Отмена ввода")]]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Введите дату оформления"
    )
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMClient.next()
    await message.reply('Введите дату оформления подписки в формате ДД.ММ', reply_markup=keyboard)


async def add_date(message: types.Message, state: FSMContext):
    kb = [[types.KeyboardButton(text="Отмена ввода")]]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Введите переодичность подписки"
    )
    async with state.proxy() as data:
        data['date'] = message.text
    await FSMClient.next()
    await message.reply('С какой периодичностью была оформлена подписка? Введите значение в днях', reply_markup=keyboard)


async def add_select(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['select'] = ((int(message.text)) * 60 * 60 * 24)
    async with state.proxy() as data:
        await message.reply(f'Подписка была добавлена в список {str(data)}', reply_markup=kb_client)
    await state.finish()


async def cancel_add(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
    await message.reply('Добавление в список было отменено.', reply_markup=kb_client)

async def donate(message: types.Message):
    await message.answer('Если вы хотите поддержать проект и помочь в его развитии, '
                         'вы можете это сделать по текущему номеру карты:')
    await message.answer('5536 9139 6627 5485')



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(about_handler, Text(equals='О боте'))
    dp.register_message_handler(add_subscribe, Text(equals='Добавить подписку в список'), state=None)
    dp.register_message_handler(cancel_add, Text(equals='Отмена ввода'), state='*')
    dp.register_message_handler(add_name, state=FSMClient.sub_name)
    dp.register_message_handler(cancel_add, Text(equals='Отмена ввода'), state='*')
    dp.register_message_handler(add_date, state=FSMClient.sub_date)
    dp.register_message_handler(cancel_add, Text(equals='Отмена ввода'), state='*')
    dp.register_message_handler(add_select, state=FSMClient.sub_select)
    dp.register_message_handler(donate, Text(equals='Поддержка проекта'))
