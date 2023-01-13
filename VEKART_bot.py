from aiogram import Bot, Dispatcher, executor
from addit_bot import dp

async def on_startup(_):
    print('Бот в онлайне, все ОК!')

from handlers import admin, client, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handler_other(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

