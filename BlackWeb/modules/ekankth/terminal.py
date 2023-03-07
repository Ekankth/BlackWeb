from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren

from BlackWeb.helper.cmd import *
from BlackWeb.helper.misc import *

from arjunarthx import *
from arjunarthx.helper.basic import *
from arjunarthx.helper.hacking import *
from arjunarthx.helper import *
from arjunarthx.help import *

# like this utroid using terminal file upload
# credits @xtsea // please do not remove credits

@ren.on_message(filters.command("ul", cmd) & filters.me)
async def terminal(client: Client, message: Message):
    file = get_arg(message)
    vcs = await message.reply_text("**please wait a moment for the file to upload....**")
    await asyncio.sleep(2)
    await vcs.edit("**Uploaded successfully...**")
    if file:
        try:
           await client.send_document(message.chat.id, file)
        except Exception as e:
            return await vcs.edit(f"**ERROR** `{e}`") 

add_command_help(
    "terminal",
    [
        [f"ul [exec]", "using terminal/shell example: `.ul file/to/path/name.py`"],
    ],
)
