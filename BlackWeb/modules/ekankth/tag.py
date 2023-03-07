"""
COPYRIGHT 2020 - 2023 : https://github.com/TeamKillerX/BlackWeb
CREDITS DEVELOPER BY : @XTSEA
"""

from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren

from BlackWeb.helper.cmd import *
from BlackWeb.helper.misc import *

from arjunarthx import *
from arjunarthx.helper import *
from arjunarthx.helper.basic import *
from arjunarthx.helper.hacking import *
from arjunarthx.help import *

@ren.on_message(filters.command("tagm", cmd) & filters.me)
async def tagm(client: Client, message: Message):
    tag = get_arg(message)
    lol = message.reply_to_message
    if not tag and not lol:
       return await message.edit("**Please Reply**")
    if tag:
       try:
          await lol.reply_text(f"<a href=tg://user?id={lol.from_user.id}>{tag}</a>")
          await message.delete()
       except Exception as e:
           return await message.edit(f"**ERROR** `{e}`")
