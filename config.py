from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "c7e952440251e33bb5cce566b29f7254")
      API_ID = int(getenv("API_ID", 18029060))      
      BOT_TOKEN = getenv("BOT_TOKEN", "7592982888:AAEfg-bVArXtC07OwjOKQX4ipPqV9TTtE2Y")
      CHANNEL = list(x for x in getenv("CHANNEL", "-1001815869253:-1002317285080").replace("\n", " ").split(' '))
