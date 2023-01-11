from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Информация')
b2 = KeyboardButton('/Меню')
b3 = KeyboardButton('Поделиться номером', request_contact=True)
b4 = KeyboardButton('Отправить мое местоположение', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) # resize делает кнопки по ширине экрана
# one_time убирает клавиатуру, после использования

kb_client.add(b1) # большая кнопка
kb_client.insert(b2) # добавляет кнопку справа от предыдущей
kb_client.row(b3, b4) # расположение кнопок в одну строку
