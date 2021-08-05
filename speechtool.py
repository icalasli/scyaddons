"""
📚 Commands Available -

• {i}tts LanguageCode <balas ke pesan>
• {i}tts LangaugeCode | text to speak

"""


import asyncio
import os
import subprocess
from datetime import datetime

from gtts import gTTS

from . import *


@ultroid_cmd(
    pattern="tts ?(.*)",
)
async def _(event):
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await eor(event, "invalid syntax, module dihentikan.")
        return
    text = text.strip()
    lan = lan.strip()
    if not os.path.isdir("downloads/"):
        os.makedirs("downloads/")
    required_file_name = "downloads/voice.ogg"
    try:
        tts = gTTS(text, lang=lan)
        tts.save(required_file_name)
        command_to_execute = [
            "ffmpeg",
            "-i",
            required_file_name,
            "-map",
            "0:a",
            "-codec:a",
            "libopus",
            "-b:a",
            "100k",
            "-vbr",
            "on",
            required_file_name + ".opus",
        ]
        try:
            subprocess.check_output(command_to_execute, stderr=subprocess.STDOUT)
        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:
            await eor(event, str(exc))
        else:
            os.remove(required_file_name)
            required_file_name = required_file_name + ".opus"
        end = datetime.now()
        ms = (end - start).seconds
        await event.reply(
            file=required_file_name,
       )
        os.remove(required_file_name)
        await eod(event, "memproses {} ({}) dalam {} detik!".format(text[0:97], lan, ms))
    except Exception as e:
        await eor(event, str(e))
