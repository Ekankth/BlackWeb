

from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren
from BlackWeb.helper.cmd import *
from arjunarthx.help import *
import asyncio

@ren.on_message(filters.command("copy", cmd) & filters.me)
async def copy_message(c: Client, m: Message):
    command_args = m.command[1:]
    if len(command_args) != 1:
        await m.reply_text("Please provide a link to the message you want to copy.")
        return
    link = m.text.split(" ", 1)[1]
    try:
        if link:
           check_copy = "kangcopybot"
           await c.send_message(check_copy, link)
           await asyncio.sleep(5)
           async for ran in c.get_chat_history(check_copy, limit=1):
               await ran.copy(m.chat.id)
    except Exception as e:
        await m.reply_text(f"Error {e}")
        return
