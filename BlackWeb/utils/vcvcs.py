from random import randint
from typing import Optional
from contextlib import suppress
from asyncio import sleep

from pyrogram.types import *
from pyrogram import *

from BlackWeb import *
from BlackWeb.modules.ekankth import *
from BlackWeb.helper.misc import *

from pykillerx import *
from pykillerx.helper.call import *
from pykillerx.helper.tools import *
from pykillerx.helper.basic import *
from pykillerx.helper import *
from pykillerx.blacklist import *

async def start_vc(client, message):
    flags = " ".join(message.command[1:])
    ren = await edit_or_reply(message, "`Processing . . .`")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"**Started Group Call\n • **Chat ID** : `{chat_id}`"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • **Title:** `{vctitle}`"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await ren.edit_text(args)
    except Exception as e:
        await ren.edit_text(f"**INFO:** `{e}`")

async def end_vc(client, message):
    """End group call"""
    chat_id = message.chat.id
    if not (
        group_call := (
            await get_group_call(client, message, err_msg=", group call already ended")
        )
    ):
        return
    await client.send(DiscardGroupCall(call=group_call))
    await edit_or_reply(message, f"Ended group call in **Chat ID** : `{chat_id}`")

async def joinvc(client, message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    if message.from_user.id != client.me.id:
        ren = await message.reply("`Otw Naik...`")
    else:
        ren = await message.edit("`Error`")
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.group_call.start(chat_id)
    except Exception as e:
        return await ren.edit(f"**ERROR:** `{e}`")
    await ren.edit_text(f"🤖 **Berhasil Join Ke Obrolan Group**\n└ **Chat ID:** `{chat_id}`")
    await sleep(5)
    await client.group_call.set_is_mute(True)


async def leavevc(client, message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    if message.from_user.id != client.me.id:
        ren = await message.reply("`Turun Dulu...`")
    else:
        ren = await message.edit("`Error`")
    with suppress(ValueError):
        chat_id = int(chat_id)
    try:
        await client.group_call.stop()
    except Exception as e:
        return await edit_or_reply(message, f"**ERROR:** `{e}`")
    msg = "🤖 **Successfully Dismounted from Voice Chat**"
    if chat_id:
        msg += f"\n└ **Chat ID:** `{chat_id}`"
    await ren.edit_text(msg)
Footer
