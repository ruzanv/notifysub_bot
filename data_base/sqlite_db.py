import sqlite3 as sql
from keyboards.client_kb import kb_client


async def sql_start(client_id):
    global base, cur
    base = sql.connect('notify_bot.db')
    cur = base.cursor()
    if base:
        print(f'DB connected OK for client: {client_id}')
    base.execute(f'CREATE TABLE IF NOT EXISTS list_sub{client_id}(name TEXT, date INTEGER, selct INTEGER)')
    base.commit()


async def sql_add_cmnd(state, client_id):
    async with state.proxy() as data:
        cur.execute(f'INSERT INTO list_sub{client_id} VALUES(?, ?, ?)', tuple(data.values()))
        base.commit()


async def view_list_sql(message, client_id):
    try:
        answer_list = ''
        for ret in cur.execute(f'SELECT rowid, name, date, selct FROM list_sub{client_id}').fetchall():
            answer_list += (f'{ret[0]}. Подписка {ret[1]}, оформлена {ret[2]} на {ret[3] // (60 * 60 * 24)} дней\n')
        await message.answer(f'{answer_list}', reply_markup=kb_client)
    except:
        await message.answer('В ваш список еще ничего не добавлено!')


async def delete_value(message):
        cur.execute(f'DELETE FROM list_sub{message.from_user.id} WHERE rowid={int(message.text)}')
        base.commit()

