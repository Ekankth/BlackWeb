"""
Project [BlackWeb](https://github.com/TeamKillerX/BlackWeb) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# COPYRIGHT https://github.com/TeamKillerX/BlackWeb
# CREATE CODING BY https://t.me/xtsea

import os
import asyncio
import cv2
import numpy as np
import requests
from io import BytesIO
from PIL import Image
from pyrogram import Client as ren
from pyrogram.types import *
from pyrogram import *
from BlackWeb.helper.cmd import *
from BlackWeb.helper.misc import *
from partharjun import *
from partharjun.helper import *
from partharjun.helper.basic import *
from partharjun.help import *
from config import DEEPAI_API


@ren.on_message(filters.command("facedetect", cmd) & filters.me)
async def face_detect(c: Client, m: Message):
    pro = await m.reply_text("`Whacking face detect.......`")
    await asyncio.sleep(5)
    if not m.reply_to_message or not m.reply_to_message.photo:
        await pro.edit("Please reply to a photo to detect faces.")
        return

    file_id = m.reply_to_message.photo.file_id
    file_path = await c.download_media(file_id)
    img = cv2.imread(file_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imwrite("output.jpg", img)
    await pro.edit("`Successfully sent image`")
    await m.reply_photo("output.jpg", caption="Here are the detected faces.")
    try:
        cleared = "output.jpg"
        os.remove(cleared)
    except BaseException:
        pass

@ren.on_message(filters.command("pcil", cmd) & filters.me)
async def generate_sketch(c: Client, m: Message):
    if m.reply_to_message.photo:
        file_id = m.reply_to_message.photo
        photo_path = await c.download_media(file_id)
    
        img = cv2.imread(photo_path)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        inverted_img = 255 - gray_img
        blurred_img = cv2.GaussianBlur(inverted_img, (21, 21), 0)
        pencil_sketch = cv2.divide(gray_img, blurred_img, scale=80)
        sketch_path = "pencil_sketch.jpg"
        cv2.imwrite(sketch_path, pencil_sketch)

        await m.reply_photo(photo=sketch_path, caption="Here's your pencil sketch!")
        os.remove(photo_path)
        os.remove(sketch_path)



@ren.on_message(filters.command(["toonify", "cartoon"], cmd) & filters.me)
async def toonify_handler(c: Client, m: Message):
    pro = await m.reply_text("`Whacking face cartoon.......`")
    await asyncio.sleep(5)
    if not m.reply_to_message or not m.reply_to_message.photo:
        await pro.edit("Please reply to a photo to convert to cartoon or comic style.")
        return
    
    file_id = m.reply_to_message.photo.file_id
    file_path = await c.download_media(file_id)
   
    with open(file_path, 'rb') as f:
        response = requests.post(
            "https://api.deepai.org/api/toonify",
            files={'image': f},
            headers={'api-key': DEEPAI_API}
        )
    result = response.json()
    if 'output_url' in result:
        await pro.edit("`Successfully sent image`")
        await c.send_photo(m.chat.id, result['output_url'])
    else:
        await pro.edit("Failed to toonify the image.")

add_command_help(
    "face",
    [
        [f"cartoon [reply to image]", "to cartoon image using the deepai api."],
        [f"toonify [reply to image]", "to toonify image using the deepai api."],
        [f"facedetect [reply to image]", "to check face detect."],
    ],
)
