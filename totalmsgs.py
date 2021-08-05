"""
📚 Commands Available -
• `{i}totalmsgs`
    Returns your total msg count in current chat
    
• `{i}totalmsgs [username]/<reply>`
    Returns total msg count of user in current chat
"""

from . import *
from telethon.utils import get_display_name


@ultroid_cmd(pattern="totalmsgs ?(.*)")
async def _(e):
    match = e.pattern_match.group(1)
    if match:
        user = match
    elif e.is_reply:
        user = (await e.get_reply_message()).sender_id
    else:
        user = "me"
    a = await e.client.get_messages(e.chat_id, 0, from_user=user)
    user = await e.client.get_entity(user)
    await eor(e, f"total pesan dari `{get_display_name(user)}` disini = {a.total}")
