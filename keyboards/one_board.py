from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def onekeyboard(name, placeholder):
    kb = [[KeyboardButton(text=name)]]
    keyboard1 = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder=placeholder
    )
    return keyboard1
