"""
📚 Commands Available -

• `{i}autoname`
   `mulai autoname.`.

• `{i}stopname`
   `hentikan autoname.`

• `{i}autobio`
   `mulai autobio.`

• `{i}stopbio`
   `hentikan autobio.`
"""

from . import *
import random
from telethon.tl.functions.account import UpdateProfileRequest


@ultroid_cmd(pattern="(auto|stop)name$")
async def autoname_(event):
    match = event.pattern_match.group(1)
    if match == "stop":
      udB.delete("AUTONAME")
      await eor(event, "`autoname telah dihentikan !`")
      return
    udB.set("AUTONAME", "True")
    await eod(event, "`memulai autoname`")
    while True:
        getn = udB.get("AUTONAME")
        if not getn:
            return
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"🕒{HM} ⚡{OWNER_NAME}⚡ {DM} 🗓️"
        await event.client(
                UpdateProfileRequest( 
                    first_name=name
                )
            )
        await asyncio.sleep(1111)


@ultroid_cmd(pattern="(auto|stop)bio$")
async def autoname_(event):
    match = event.pattern_match.group(1)
    if match == "stop":
      udB.delete("AUTOBIO")
      await eor(event, "`autobio telah dihentikan !`")
      return
    udB.set("AUTOBIO", "True")
    await eod(event, "`memulai autobio`")
    BIOS = ["sedang sibuk !",
            "caper bet lu tolol",
            "ape liat liat bio gua?, naksir yah?..",
            "hai beban ortu, apa kabar 👋🏻"
            "cie nge stalking, xixixi",
            "ga terima pm, pc segala macam, gua sibuk !"]
    while True:
        getn = udB.get("AUTOBIO")
        if not getn:
            return
        BIOMSG = random.choice(BIOS)
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"📅{DM} | {BIOMSG} | ⌚️{HM}"
        await event.client(
                UpdateProfileRequest( 
                    about=name,
                )
            )
        await asyncio.sleep(1111)
