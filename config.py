try:
    from logging import getLogger
    from os import environ
    LOGGER = getLogger(__name__)
    from os import getenv
    import sys
    import os
    from dotenv import load_dotenv
    from base64 import b64decode as who
    from partharjun.helper import *
    from partharjun.config import *
    from distutils.util import strtobool as sb
    load_dotenv("config.env", override=True)
except:
    print("not installed partharjun")


API_ID = int(getenv("API_ID", "")) 
API_HASH = getenv("API_HASH")
OWNER_ID = int(getenv("OWNER_ID", ""))
BOT_TOKEN = getenv("BOT_TOKEN")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PACK_NAME = getenv("PACK_NAME", "kang pack")
GCAST_BLACKLIST = {int(x) for x in getenv("GCAST_BLACKLIST", "").split()}

DB_URL = getenv("DATABASE_URL")

_LOG_ID = environ.get("LOG_ID", None)
LOG_ID = int(_LOG_ID) if _LOG_ID and resr(r'^-?\d+$', _LOG_ID) else None
del _LOG_ID

LOG_VERBOSE = sb(environ.get('LOG_VERBOSE', 'False'))

RMBG_API = getenv("RMBG_API")
OPENAI_API = getenv("OPENAI_API")
DEEPAI_API = getenv("DEEPAI_API")

# don't kanger repo this !!!
CHANNEL = "@EkankthHackz"
SUPPORT = "@Ekankth"

BOT_VER = "0.0.0@dev"
BRANCH = getenv("BRANCH", "BlackWeb") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", None)
STRING_SESSION3 = getenv("STRING_SESSION3", None)
STRING_SESSION4 = getenv("STRING_SESSION4", None)
STRING_SESSION5 = getenv("STRING_SESSION5", None)
STRING_SESSION6 = getenv("STRING_SESSION6", None)
STRING_SESSION7 = getenv("STRING_SESSION7", None)
STRING_SESSION8 = getenv("STRING_SESSION8", None)
STRING_SESSION9 = getenv("STRING_SESSION9", None)
STRING_SESSION10 = getenv("STRING_SESSION10", None)