from config import RMBG_API
from pyrogram.types import *
from pyrogram import *
from base64 import b64decode as hack
from BlackWeb import *
from BlackWeb.utils import *
from partharjun.helper.basic import *
from partharjun.helper.tools import *
import os
import requests
import shutil

async def rmbg_background(c, m):
    api_key = RMBG_API
    photo_id = m.reply_to_message.photo.file_id
    temp_file = await c.download_media(photo_id)
    if not api_key:
       return await m.edit("**RMBG_API: missing**")

    endpoint = "https://api.remove.bg/v1.0/removebg"
    payload = {"size": "auto"}

    if api_key:
       with open(temp_file, "rb") as image_file:
          response = requests.post(endpoint, data=payload, headers={"X-Api-Key": api_key}, files={"image_file": image_file}, stream=True)

    with open("output.png", "wb") as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    await m.reply_document("output.png")
    try:
       clear_file = "ran.webp"
       clear_file2 = "output.png"
       (await shell_exec("cp *.png ran.webp"))[0]
       await c.send_sticker(m.chat.id, "ran.webp")
       os.remove(clear_file)
       os.remove(clear_file2)
    except BaseException:
        pass


async def photo_as_sticker(c, m):
    try:
       goblok_lu = get_arg(m)
       ran = m.reply_to_message
       if not ran and not goblok_lu: 
          return await m.edit("**Please Reply [image/background]**")

       if goblok_lu.startswith("-p"):
          file_name = "downloads/ran.webp"
          upload = await ran.download()
          (await shell_exec("cd downloads && cp *.jpg ran.webp"))[0]
          await c.send_sticker(m.chat.id, file_name)
          os.remove(file_name)
          os.remove(upload)

       if goblok_lu.startswith("-r"):
          file_name = "downloads/ran.webp"
          upload = await ran.download()
          (await shell_exec("cd downloads && cp *.png ran.webp"))[0]
          await c.send_sticker(m.chat.id, file_name)
          os.remove(file_name)
          os.remove(upload)

       if goblok_lu.startswith("-m"):
          file_name = "downloads/ran.jpg"
          upload = await ran.download()
          (await shell_exec("cd downloads && cp *.webp ran.jpg"))[0]
          await c.send_photo(m.chat.id, file_name)
          os.remove(file_name)
          os.remove(upload)

          # copyright by https://t.me/xtsea
          # credits : https://t.me/xtsea

       if goblok_lu.startswith("--profile anime"):
             as_ai = await m.reply_text("`Prossing......`")
             animebot = hack("QW5pbWVBSUFscGhhQm90").decode("utf-8")
             bot = animebot
             user_id = ran.from_user.id
             user = await c.get_users(user_id)
             asend = await c.download_media(user.photo.big_file_id)
             await asyncio.sleep(5)
             delete_as_photo = await c.send_photo(bot, photo=asend)
             await asyncio.sleep(15)
             async for randydev in c.search_messages(bot, limit=1):
                 if randydev.photo:
                    downloader_as_photo = await c.download_media(randydev)
                    await as_ai.edit("`Successfully sent image`")
                    await c.send_photo(m.chat.id, downloader_as_photo)
                    await delete_as_photo.delete()
                    await randydev.delete()
                    os.remove(downloader_as_photo)
                    os.remove(asend)            

       if goblok_lu.startswith("-anime"):
          as_ai = await m.reply_text("`Prossing......`")
          animebot = hack("QW5pbWVBSUFscGhhQm90").decode("utf-8")
          bot = animebot
          if not ran or not ran.photo: 
             await as_ai.edit("**Please reply to a photo to anime**")
             return 
          photo_id = ran.photo.file_id
          delete_as_photo = await c.send_photo(bot, photo=photo_id)
          await asyncio.sleep(15)
          async for randydev in c.search_messages(bot, limit=1):
              if randydev.photo:
                 downloader_as_photo = await c.download_media(randydev)
                 await as_ai.edit("`Successfully sent image`")
                 await c.send_photo(m.chat.id, downloader_as_photo)
                 await delete_as_photo.delete()
                 await randydev.delete()
                 os.remove(downloader_as_photo)
              else:
                  await pro.edit("**ERROR ANIME**")
          await c.delete_messages(bot, 3)      

    except BaseException:
        pass
