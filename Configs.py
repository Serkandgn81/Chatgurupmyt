# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "28121536"))
    API_HASH = os.environ.get("API_HASH", "57d552d05f2a76244291d9eb330294c2")
    TOKEN = os.environ.get("TOKEN", "7282714112:AAFPB0W1s2Ej8W9MZlBRNWmEsMNluLbltxc")
