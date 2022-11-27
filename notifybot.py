from time import asctime
from aiogram import executor
from create_bot import dp


async def on_startup(_):
    print(f'Бот вышел в онлайн в {asctime()}')

from lvl_handlers import client, admin

client.register_handlers_client(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
