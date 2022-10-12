#
#
# import token
from config_data import config 
# 
# import libraries
from aiogram import Bot
from aiogram import Dispatcher
#


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)