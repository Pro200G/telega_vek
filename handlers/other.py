from aiogram import types, Dispatcher
from addit_bot import dp
import json, string

# @dp.message_handler()
async def cenz_fuck(message: types.Message):
    if{i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()

def register_handler_other(dp: Dispatcher):
    dp.register_message_handler(cenz_fuck, )
