import req_bot


@req_bot.dp.message_handler(commands=['start'])
async def start_handler(message: req_bot.types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    req_bot.logging.info(f'{user_id=} {user_full_name=}, {req_bot.time.asctime()}')
    await message.answer(f'Привет, {user_full_name}! Ты запустил бота помощника по управлению твоими подписками!')


@req_bot.dp.message_handler(commands=['about'])
async def about_handler(message: req_bot.types.Message):
    user_first_name = message.from_user.first_name
    await message.reply(f'Это чат-бот, который поможет тебе, {user_first_name}, следить за своими подписками.')
    await message.answer(
        f'Зачем это нужно? Все просто, сейчас существует большая проблема с управлением своих подписок. Часто мы '
        f'забываем о том, что мы оформляли и в неожиданный момент у нас происходят списания средств за то, '
        f'чем мы не пользуемся.')
    await message.answer(
        f'С помощью этого бота ты можешь добавлять свои текущие подписки в список, а бот будет напоминать тебе о '
        f'скором списании средств по добавленной подписке.')


if __name__ == '__main__':
    req_bot.executor.start_polling(req_bot.dp, skip_updates=True, on_startup=req_bot.on_startup)
