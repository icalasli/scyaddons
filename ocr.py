"""
📚 Commands Available -

• `{i}ocr <language code><balas ke foto>`
    mengenali teks dari gambar.

"""


import requests as r
from telegraph import upload_file as uf

from . import *

TE = f"API tidak ditemukan, dapatkan dari ocr.space dan set\n\ncommand `{HNDLR}setredis OCR_API your-api-key`"


@ultroid_cmd(pattern="ocr ?(.*)")
async def ocrify(ult):
    if not ult.is_reply:
        return await eor(ult, "`balas ke foto...`")
    msg = await eor(ult, "`memproses...`")
    OAPI = udB.get("OCR_API")
    if not OAPI:
        return await msg.edit(TE)
    pat = ult.pattern_match.group(1)
    repm = await ult.get_reply_message()
    if not (repm.media and repm.media.photo):
        return await msg.edit("`bukan foto...`")
    dl = await repm.download_media()
    if pat:
        atr = f"&language={pat}&"
    else:
        atr = "&"
    tt = uf(dl)
    li = "https://telegra.ph" + tt[0]
    gr = r.get(
        f"https://api.ocr.space/parse/imageurl?apikey={OAPI}{atr}url={li}"
    ).json()
    trt = gr["ParsedResults"][0]["ParsedText"]
    await msg.edit(f"**🎉 OCR PORTAL\n\nRESULTS ~ ** `{trt}`")
