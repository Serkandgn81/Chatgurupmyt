from telethon import TelegramClient
import logging
from Configs import *

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

bot = TelegramClient('Meyit47', api_id=Configs.APP_ID, api_hash=Configs.API_HASH)
Meyit47 = bot.start(bot_token=Configs.TOKEN)
