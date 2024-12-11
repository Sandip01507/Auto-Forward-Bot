import logging
logger = logging.getLogger(__name__)
from pyrogram import filters
from bot import channelforward

@channelforward.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message):
    await message.reply(
        text="**Hi there! I am a channel auto forward bot. I can forward only new messages from one channel to another channel.**",
        disable_web_page_preview=True,
        quote=True
    )