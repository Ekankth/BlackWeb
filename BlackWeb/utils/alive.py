import os
from os import getenv
import asyncio
import asyncio as tai
from datetime import datetime as dt
from platform import python_version
from pyrogram import __version__, filters, Client
from pyrogram import Client as ren
from pyrogram.types import *
from pyrogram import *
from config import *
from pytgcalls import __version__ as tg

# --------- BlackWeb ---------------------------------------

from BlackWeb import *
from BlackWeb.modules.bot.inline import get_readable_time

# --------- pykillerx Library ---------------------------------------

from pykillerx.helper.hacking import *
from pykillerx.helper import *
from pykillerx import __version__ as killerx
from pykillerx.extra import *

# --------- alive Command ---------------------------------------

alive_logo = ALIVE_PIC or "https://ibb.co/306MBpx"

async def alive(client, message):
    user = await client.get_users("me")
    if ALIVE_TEXT:
       txt = ALIVE_TEXT
    else:
        txt = (
        f"** 〄 𝓑𝓵𝓪𝓬𝓴 𝓦𝓮𝓫 〄**\n\n"
        f"❏ **full_name**: `{user.first_name}`\n"
        f"├•  **premium**: `{user.is_premium}`\n"
        f"├• **dc_id**: `{user.dc_id}`\n"
        f"├• **ᴠᴇʀsɪᴏɴ**: `{BOT_VER}`\n"
        f"├• **ᴘʏᴋɪʟʟᴇʀx**: `{killerx}` [`{where_hosted()}`]\n"
        f"├• **ᴜᴘᴛɪᴍᴇ**: `{str(dt.now() - START_TIME).split('.')[0]}`\n"
        f"├• **ᴘʏᴛʜᴏɴ**: `{python_version()}`\n"
        f"├• **ᴘʏʀᴏɢʀᴀᴍ**: `{__version__}`\n"
        f"└• **ᴍᴏᴅᴜʟᴇs**: `{len(CMD_HELP)}`\n"

    )
    xx = await message.reply_text("☠️")
    try:
       await message.delete()
    except:
       pass
    send = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    xd = (f"{txt}")
    try:
        await tai.gather(
            xx.delete(),
            send(
                message.chat.id,
                caption=xd,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await xx.edit(xd, disable_web_page_preview=True)

async def repo(bot, message):
    await message.edit("⚡")
    await asyncio.sleep(1)
    await message.edit("Fetching Source Code.....")
    await asyncio.sleep(1)
    await message.edit(f"[Here is repo]({REPO_URL})", disable_web_page_preview=True)

async def creator(bot, message):
    await message.edit(f"Developer By [BOT](https://t.me/ekankth)")

async def uptime(bot, message):
    now = dt.now()
    current_uptime = now - START_TIME
    await message.edit(f"Uptime ⚡\n" f"```{str(current_uptime).split('.')[0]}```")

async def get_id(bot, message):
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message

        if rep.audio:
            file_id = f"**File ID**: `{rep.audio.file_id}`"
            file_id += "**File Type**: `audio`"

        elif rep.document:
            file_id = f"**File ID**: `{rep.document.file_id}`"
            file_id += f"**File Type**: `{rep.document.mime_type}`"

        elif rep.photo:
            file_id = f"**File ID**: `{rep.photo.file_id}`"
            file_id += "**File Type**: `photo`"

        elif rep.sticker:
            file_id = f"**Sicker ID**: `{rep.sticker.file_id}`\n"
            if rep.sticker.set_name and rep.sticker.emoji:
                file_id += f"**Sticker Set**: `{rep.sticker.set_name}`\n"
                file_id += f"**Sticker Emoji**: `{rep.sticker.emoji}`\n"
                if rep.sticker.is_animated:
                    file_id += f"**Animated Sticker**: `{rep.sticker.is_animated}`\n"
                else:
                    file_id += "**Animated Sticker**: `False`\n"
            else:
                file_id += "**Sticker Set**: __None__\n"
                file_id += "**Sticker Emoji**: __None__"

        elif rep.video:
            file_id = f"**File ID**: `{rep.video.file_id}`\n"
            file_id += "**File Type**: `video`"

        elif rep.animation:
            file_id = f"**File ID**: `{rep.animation.file_id}`\n"
            file_id += "**File Type**: `GIF`"

        elif rep.voice:
            file_id = f"**File ID**: `{rep.voice.file_id}`\n"
            file_id += "**File Type**: `Voice Note`"

        elif rep.video_note:
            file_id = f"**File ID**: `{rep.animation.file_id}`\n"
            file_id += "**File Type**: `Video Note`"

        elif rep.location:
            file_id = "**Location**:\n"
            file_id += f"**longitude**: `{rep.location.longitude}`\n"
            file_id += f"**latitude**: `{rep.location.latitude}`"

        elif rep.venue:
            file_id = "**Location**:\n"
            file_id += f"**longitude**: `{rep.venue.location.longitude}`\n"
            file_id += f"**latitude**: `{rep.venue.location.latitude}`\n\n"
            file_id += "**Address**:\n"
            file_id += f"**title**: `{rep.venue.title}`\n"
            file_id += f"**detailed**: `{rep.venue.address}`\n\n"

        elif rep.from_user:
            user_id = rep.from_user.id

    if user_id:
        if rep.forward_from:
            user_detail = (
                f"**Forwarded User ID**: `{message.reply_to_message.forward_from.id}`\n"
            )
        else:
            user_detail = f"**User ID**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**Message ID**: `{message.reply_to_message.id}`"
        await message.edit(user_detail)
    elif file_id:
        if rep.forward_from:
            user_detail = (
                f"**Forwarded User ID**: `{message.reply_to_message.forward_from.id}`\n"
            )
        else:
            user_detail = f"**User ID**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**Message ID**: `{message.reply_to_message.id}`\n\n"
        user_detail += file_id
        await message.edit(user_detail)

    else:
        await message.edit(f"**Chat ID**: `{message.chat.id}`")
