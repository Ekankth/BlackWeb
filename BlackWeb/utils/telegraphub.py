import asyncio
from telegraph import Telegraph, exceptions, upload_file
from pyrogram.types import *
from pyrogram import *
from BlackWeb import *
from pykillerx.helper.basic import *
from pykillerx.helper.hacking import *
from pykillerx import *
from pykillerx.helper import *


telegraph = Telegraph()
r = telegraph.create_account(short_name="DarkWeb-Userbot")
auth_url = r["auth_url"]

async def telegraph_upload(client, message):
    ren = await edit_or_reply(message, "`Processing . . .`")
    if not message.reply_to_message:
        await ren.edit(
            "**Please reply to the message, to get the link from the telegraph**"
        )
        return
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            pe_ler = await convert_to_image(message, client)
        else:
            pe_ler = await message.reply_to_message.download()
        try:
            media_url = upload_file(pe_ler)
        except exceptions.TelegraphException as exc:
            await ren.edit(f"**ERROR:** `{exc}`")
            os.remove(pe_ler)
            return
        done = (
            f"**Successfully uploaded to** [Telegraph](https://telegra.ph/{media_url[0]})"
        )
        await ren.edit(done)
        os.remove(pe_ler)
    elif message.reply_to_message.text:
        page_title = get_text(message) if get_text(message) else client.me.first_name
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            await ren.edit(f"**ERROR:** `{exc}`")
            return
        tele = f"**Successfully uploaded to** [Telegraph](https://telegra.ph/{response['path']})"
        await ren.edit(tele)
