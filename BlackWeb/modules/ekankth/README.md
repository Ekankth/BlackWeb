## How to make a module
- try example use `test.py`
```python
import asyncio
from pyrogram import Client as ren
from pyrogram.types import *
from pyrogram import Client
from BlackWeb.helper.misc import *
from BlackWeb.helper.cmd import *
from arjunarthx.help import *
from arjunarthx.helper.basic import *
from arjunarthx.helper import *


@ren.on_message(filters.command("test", cmd) & filters.me)
async def test(client: Client, message: Message):
    await client.send_message(message.chat.id, "Hello World")

add_command_help(
    "test",
    [
        ["test", "Hello World"],
    ],
)
```
