#
#
#
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


# here define our keyboards
cr_date = KeyboardButton('/Creation_date')
ex_date = KeyboardButton('/Expiration_date')
update_date = KeyboardButton('/Registrar')
name_server = KeyboardButton('/Name_servers')
exit_button = KeyboardButton('/Exit')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(cr_date).insert(ex_date).add(update_date).insert(name_server).add(exit_button)