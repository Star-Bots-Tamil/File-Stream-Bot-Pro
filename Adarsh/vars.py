# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '11973721'))
    API_HASH = str(getenv('API_HASH', '5264bf4663e9159565603522f58d3c18'))
    BOT_TOKEN = str(getenv('BOT_TOKEN','5990559544:AAHUhUFy54tDKGubpU_dMSpSGTRthmgImAw'))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001871766752'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', 'starstreamer.hop.sh'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1391556668").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    PORT = int(environ.get("PORT", 8080))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', '@TG_Karthik'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME', 'file-stream-bot-pro'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'starstreamer.hop.sh')) if not ON_HEROKU or getenv('FQDN', '16.171.19.76:8080') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL', True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Star_Bots_Tamil'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001296894100")).split())) 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001821439025"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
    KEEP_ALIVE = str(environ.get("KEEP_ALIVE", "1").lower()) in  ("1", "true", "t", "yes", "y")
    DEBUG = str(environ.get("DEBUG", "0").lower()) in ("1", "true", "t", "yes", "y")
    USE_SESSION_FILE = str(environ.get("USE_SESSION_FILE", "0").lower()) in ("1", "true", "t", "yes", "y")
