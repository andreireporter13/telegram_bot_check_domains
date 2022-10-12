#
#
#
from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import kb_client
from special_scripts import cr_date, exp_date, domain_register, n_servers

from aiogram.types import ReplyKeyboardRemove



# Help function
async def welcome(message: types.Message): 
    await message.answer('Hello. This bot can give you any information about domains with this extensions: .ro, .com, .eu. Press "/start" to begin')


# Start function
async def general_start_command(message: types.Message):
    await message.answer('Write domain for check. Domain must have extension .ro, .com, .eu')


# Save domain name
async def choose_domain_data(message: types.Message):
    await message.answer('Choose needed data for your domain (.com, .ro, eu)', reply_markup=kb_client) # keyboard here

    # catch domain_name
    global dom_ans 
    dom_ans = message.text


# Creation date function
async def domain_creation_date(message: types.Message):
    await message.reply(cr_date(dom_ans))


# Expiration date function
async def domain_expiration_date(message: types.Message):
    await message.reply(exp_date(dom_ans))


# Updated date function 
async def domain_updated_date(message: types.Message):
    await message.reply(domain_register(dom_ans))


# Name Servers function 
async def domain_name_servers_data(message: types.Message):
    await message.reply(n_servers(dom_ans))


async def exit_func(message: types.Message):
    await message.answer('Menu is closed. If you want start verify domain, insert /start command!', reply_markup=ReplyKeyboardRemove())


# handlers
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(welcome, commands=['help', 'Help', 'HELP'])
    dp.register_message_handler(general_start_command, commands=['start', 'Start', 'START'])
    dp.register_message_handler(choose_domain_data, regexp='[\w\.\/]+.(com|ro|eu)$')
    dp.register_message_handler(domain_creation_date, commands=['Creation_date'])
    dp.register_message_handler(domain_expiration_date, commands=['Expiration_date'])
    dp.register_message_handler(domain_updated_date, commands=['Registrar'])
    dp.register_message_handler(domain_name_servers_data, commands=['Name_servers'])
    dp.register_message_handler(exit_func, commands=['Exit'])