import sys
from os import environ, execle, remove
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren
from pyrogram import Client
from BlackWeb.helper.cmd import *
from BlackWeb import *
from BlackWeb.helper.misc import *

from partharjun.helper.basic import *
from partharjun import *
from partharjun.helper import *
from partharjun.help import *

@Client.on_message(filters.command("restart", cmd) & filters.user(1191668125))
async def restart_bot(_, message: Message):
    try:
        msg = await edit_or_reply(message, "`Restarting bot...`")
        LOGGER("BlackWeb").info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER("BlackWeb").info(f"{err}")
        return
    await msg.edit_text("✅ Bot has restarted !\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "BlackWeb"]
        execle(sys.executable, *args, environ)



add_command_help(
    "system",
    [
        ["restart", "to restart userbot."],
    ],
)
