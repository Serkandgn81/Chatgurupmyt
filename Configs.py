# Zorunlu gereklidir. Eklemek istediğin bilgileri burda belirt çekinme 😏

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "2930013"))
    API_HASH = os.environ.get("API_HASH", "7cab92dcd979add511b79d693775e17d")
    TOKEN = os.environ.get("TOKEN", "6803669543:AAF3IVN9OQvi0DFESZSX2Nc4W2YGFBO6__c")
