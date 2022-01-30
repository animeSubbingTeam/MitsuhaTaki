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

import html
import aiohttp
from typing import Optional, List

import elaina.modules.helper_funcs.git_api as api
import elaina.modules.sql.github_sql as sql

from pyrogram import filters
from elaina import pbot, BOT_USERNAME
from elaina.utils.errors import capture_err
from elaina.modules.sql.clear_cmd_sql import get_clearcmd
from elaina import dispatcher, OWNER_ID, EVENT_LOGS
from elaina.modules.helper_funcs.filters import CustomFilters
from elaina.modules.helper_funcs.chat_status import user_admin
from elaina.modules.helper_funcs.misc import delete
from elaina.modules.disable import DisableAbleCommandHandler

from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    RegexHandler,
    run_async,
)

from telegram import (
    Message,
    Chat,
    Update,
    Bot,
    User,
    ParseMode,
    InlineKeyboardMarkup,
    MAX_MESSAGE_LENGTH,
)


def getphh(index):
    recentRelease = api.getReleaseData(api.getData("phhusson/treble_experimentations"), index)
    if recentRelease is None:
        return "The specified release could not be found"
    author = api.getAuthor(recentRelease)
    authorUrl = api.getAuthorUrl(recentRelease)
    name = api.getReleaseName(recentRelease)
    assets = api.getAssets(recentRelease)
    releaseName = api.getReleaseName(recentRelease)
    message = "<b>Author:</b> <a href='{}'>{}</a>\n".format(authorUrl, author)
    message += "<b>Release Name:</b> <code>"+releaseName+"</code>\n\n"
    message += "<b>Assets:</b>\n"
    for asset in assets:
        fileName = api.getReleaseFileName(asset)
        if fileName in ("manifest.xml", "patches.zip"):
            continue
        fileURL = api.getReleaseFileURL(asset)
        assetFile = "• <a href='{}'>{}</a>".format(fileURL, fileName)
        sizeB = ((api.getSize(asset))/1024)/1024
        size = "{0:.2f}".format(sizeB)
        message += assetFile + "\n"
        message += "    <code>Size: "  + size + " MB</code>\n"
    return message


@pbot.on_message(filters.command(["github", "git", f"git@{BOT_USERNAME}"]))
@capture_err
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/git Username")
        return
    username = message.text.split(None, 1)[1]
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result["html_url"]
                name = result["name"]
                company = result["company"]
                bio = result["bio"]
                created_at = result["created_at"]
                avatar_url = result["avatar_url"]
                blog = result["blog"]
                location = result["location"]
                repositories = result["public_repos"]
                followers = result["followers"]
                following = result["following"]
                caption = f"""**Info Of {name}**
**Username:** `{username}`
**Bio:** `{bio}`
**Profile Link:** [Here]({url})
**Company:** `{company}`
**Created On:** `{created_at}`
**Repositories:** `{repositories}`
**Blog:** `{blog}`
**Location:** `{location}`
**Followers:** `{followers}`
**Following:** `{following}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=caption)


__mod_name__ = "GitHub"
