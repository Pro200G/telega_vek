import time

from aiogram import types, Dispatcher
from addit_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove # функция для удаления клавиатуры с экрана

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.reply(f'Привет, {message.from_user.full_name}!', reply_markup=kb_client)
    for i in range(1):
        time.sleep(2)
        await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, Вам что-то понравилось?')

# @dp.message_handler(commands=['Информация'])
async def info_company(message: types.Message):
    await bot.send_message(message.from_user.id, 'Меня зовут Екатерина и я занимаюсь созданием изделий из эпоксидной смолы')

async def client_menu():
    pass

# Если в один из await, в коцне в скобках добавить строку reply_markup=ReplyKeyboardRemove, то клавиатура исчезнет
# при нажатии этой функции

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(info_company, commands=['Информация'])