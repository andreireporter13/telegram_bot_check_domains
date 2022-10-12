#
from aiogram import types, Dispatcher
from create_bot import dp
#
#
#
# general function for catching other message
async def any_comment(message: types.Message):

    if '.' in message.text and message.text.split('.')[1] not in ['eu', 'ro', 'com']:
        await message.reply('You are insert domain name with unsuportable extension!')
    else: 
        await message.reply('Please insert /help or /start command and do what you are told.')


def register_handlers_other(dp: Dispatcher): 
    dp.register_message_handler(any_comment)


