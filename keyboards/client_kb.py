from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

About = '/about'

kb1 = KeyboardButton('О боте')
kb2 = KeyboardButton('Добавить подписку в список')
kb3 = KeyboardButton('Посмотреть список подписок')
kb4 = KeyboardButton('Удалить подписку из списка')
kb5 = KeyboardButton('Поддержка проекта')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(kb1).add(kb3).row(kb2, kb4).add(kb5)
