# MIT License

# Copyright (c) 2022 Zenitsu Prjkt™

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram import __version__ as pyrover
from telegram import __version__ as telever
from telethon import __version__ as tlhver

from elaina import telethn as tbot
from elaina.events import register

PHOTO = "https://telegra.ph/file/7482398e772bd21a1f2bb.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Elaina Robot.** \n\n"
    TEXT += "💠 **I'm Working Properly** \n\n"
    TEXT += "💠 **My Master : [Zenitsu Prjkt](https://t.me/ZenitsuPrjkt)** \n\n"
    TEXT += f"💠 **Library Version :** `{telever}` \n\n"
    TEXT += f"💠 **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"💠 **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += "**Thanks For Adding Me Here ❤️**"
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT)
