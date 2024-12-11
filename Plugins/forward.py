import logging
logger = logging.getLogger(__name__)

from pyrogram import filters
from bot import channelforward
from config import Config 

@channelforward.on_message(filters.channel)
async def channel_01(client, message):
   try:
      for id in Config.CHANNEL:
         from_channel, to_channel = id.split(":")
         if message.chat.id == int(from_channel):
            # func = message.copy if False else message.forward
            await message.copy(int(to_channel))
            print("Forwarded message", from_channel, "to", to_channel)
   except Exception as e:
      logger.exception(e)