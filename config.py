import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6184365480:AAHfps14xl7-zNknrVov6FOZXm37OdG6aI8")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "9774346"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a92aed7d74654a563af4b07efbcd88e9")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001422964183"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "907544310"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgresql://mxyspspz:vc5-Pd2-d_dGr58zPBzowKMsxAaM8_ih@baasu.db.elephantsql.com/mxyspspz")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001857806665"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\ndek Dek Tutor Dek.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "907544310 1670927917").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>Anda Bergabung Ke Channel Terlebih Dahulu Untuk Melihat Video\n\n Silakan Join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", True) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
