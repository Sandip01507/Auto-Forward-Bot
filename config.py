from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "abcd")
      API_ID = int(getenv("API_ID", 1234))      
      BOT_TOKEN = getenv("BOT_TOKEN", "1234:abcd")
      CHANNEL = list(x for x in getenv("CHANNEL", "-100123:-100456").replace("\n", " ").split(' '))
