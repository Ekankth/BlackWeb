from io import BytesIO
from pyrogram import *
from pyrogram.types import *
from BlackWeb import *
from BlackWeb.utils import *
from BlackWeb.modules.ekankth.carbon import make_carbon

async def neofetch(client, message):
    chat_id = message.chat.id
    noob = await message.reply_text("`Prossing.....`")
    try:
        neofetch = (await shell_exec("neofetch --stdout"))[0]
        carbon = await make_carbon(neofetch)
        await noob.edit("`Uloading....`")
        await client.send_photo(chat_id, carbon, caption=f"Carbonised by {client.me.mention}")
        await noob.delete()
    except Exception:
        pass

async def sysinfo(c, m):
    chat_id = m.chat.id
    pro = await m.reply_text("`Prossing....`")
    try:
        sysinfo = (await shell_exec("neofetch | sed 's/\x1B\\[[0-9;\\?]*[a-zA-Z]//g'"))[0]
        carbon = await make_carbon(sysinfo)
        await c.send_photo(chat_id, carbon, caption=f"Carbonised by {c.me.mention}")
        await pro.delete()
    except Exception:
        pass
