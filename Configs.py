# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "24864975"))
    API_HASH = os.environ.get("API_HASH", "73251b7458f360ace1c92adaf8d8ac16")
    TOKEN = os.environ.get("TOKEN", "5831429115:AAHlW32O2W-rBQbdtLauZnUy_B1aowHL10Y")
