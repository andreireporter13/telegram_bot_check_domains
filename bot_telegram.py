# New telegram bot with Aiogram for my Portofolio
#
############################################################################
#
#
# Author: Andrei C. Cojocaru
# Linkedin: https://www.linkedin.com/in/andrei-cojocaru-985932204/
# Facebook: https://www.facebook.com/webautomation.romania
# Tiktok: https://www.tiktok.com/@n0hacker_reporter13
# Twitter: https://twitter.com/andrei_reporter
# Youtube: https://www.youtube.com/channel/UCgx_Y9OHi5KPVzLJo9setxw/featured
# GitHub: https://github.com/andreireporter13
# Website: https://webautomation.ro/
# 
# 
############################################################################
#

# import libraries
from aiogram import executor
from create_bot import dp
# 
from handlers import client, other


# start bot message
async def on_startup(_):
    print('Bot is online!')


client.register_handlers_client(dp)
other.register_handlers_other(dp)


# poolling function
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

