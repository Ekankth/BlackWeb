from pyrogram import *
from pyrogram.types import *
from BlackWeb import *
import requests


async def export_string(client, message):
    string = await client.export_session_string()
    await client.send_message("me", string)
    await message.reply_text("Successfully you check saved messages")
