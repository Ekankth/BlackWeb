import asyncio

from prettytable import *
from pyrogram import *
from pyrogram import Client as ren
from pyrogram import Client
from pyrogram.types import Message

from BlackWeb import app, CMD_HELP
from BlackWeb.helper.cmd import *
from BlackWeb.utils import *

from arjunarthx.helper.hacking import *
from arjunarthx.helper.utility import *
from arjunarthx.helper import *
from arjunarthx.blacklist import *
from arjunarthx.help import *

@ren.on_message(filters.command(["help", "helpme"], cmd) & filters.me)
async def module_help_cmd(client: Client, message: Message):
    await module_help(client, message)

@ren.on_message(filters.command(["plugins"], cmd) & filters.me)
async def module_helper_cmd(client: Client, message: Message):
    await module_helper(client, message)
