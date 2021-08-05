"""
📚 **makes fancy gif from your words!**
📚 `{i}t2g <some_text>`
    `mengubah teks menjadi gif`
"""

import emoji
import re, os
import random
from telethon.utils import get_input_document

from . import *

chat = "text2gifBot"

def remove_emoji(string):
    return emoji.get_emoji_regexp().sub(u'', string)


@ultroid_cmd(pattern="t2g ?(.*)")
async def t2g(e):
    eris = await eor(e, "`...`")
    input_args = e.pattern_match.group(1) 
    if not input_args:
        input_args = "mohon berikan teks juga."
    args = remove_emoji(input_args)
    try:
        t2g = await e.client.inline_query(chat, args)
        doc = t2g[random.randrange(0, len(t2g) -1)]
        try:
            file = await doc.download_media()
            done = await e.client.send_file(
            e.chat_id,
            file = file,
            reply_to=e.reply_to_msg_id
            )
            os.remove(file)
        except AttributeError:
            # for files, without write Method
            done = await doc.click(
                e.chat_id,
                reply_to=e.reply_to_msg_id)
        await eris.delete()
    except Exception as fn:
        return await eod(eris, f"**ERROR** : `{fn}`")
    await cleargif(done)


async def cleargif(gif_):
    try:
        await ultroid(
            functions.messages.SaveGifRequest(
                id=get_input_document(gif_),
                unsave=True,
            )
        )
    except Exception as E:
        LOGS.info(E)
