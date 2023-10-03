# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
✘ **Bantuan Untuk Broadcast**

๏ **Perintah:** `gcast`
◉ **Keterangan:** Kirim pesan ke semua obrolan grup.

๏ **Perintah:** `gucast`
◉ **Keterangan:** Kirim pesan ke semua pengguna pribadi.

๏ **Perintah:** `addbl`
◉ **Keterangan:** Tambahkan grup ke dalam anti gcast.

๏ **Perintah:** `delbl`
◉ **Keterangan:** Hapus grup dari daftar anti gcast.

๏ **Perintah:** `blchat`
◉ **Keterangan:** Melihat daftar anti gcast.
"""
import asyncio

from Ayra.dB import DEVS
from Ayra.dB.gcast_blacklist_db import add_gblacklist, list_bl, rem_gblacklist
from Ayra.fns.tools import create_tl_btn, format_btn, get_msg_button
from telethon.errors.rpcerrorlist import FloodWaitError

from . import *
from ._inline import something


@ayra_cmd(pattern="[gG][c][a][s][t]( (.*)|$)", fullsudo=True)
async def gcast(event):
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await eor(
            event, ('**Kiw Jomblo..`"
        )
    kk = await event.eor("`LagiNgirimBacotanAlaymu")
    er = 0
    done = 0
    err = ""
    chat_blacklist = udB.get_key("GBLACKLISTS") or []
    chat_blacklist.append(-1001608847572)  (-1001905557194)
    udB.set_key("GBLACKLISTS", chat_blacklist)
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            
            if chat not in chat_blacklist and chat not in NOSPAM_CHAT:
                try:
                    await event.client.send_message(chat, msg)
                    done += 1
                except FloodWaitError as fw:
                    await asyncio.sleep(fw.seconds + 10)
                    try:
                        await event.client.send_message(
                                chat, msg)
                        done += 1
                    except Exception as rr:
                        err += f"• {rr}\n"
                        er += 1
                except BaseException as h:
                    err += f"• {str(h)}" + "\n"
                    er += 1
    await kk.edit(f"** Selingkuhan Lo ada {done} Di Kamar, Di Ghosting {er} Asuw.**")


@ayra_cmd(pattern="[gG][u][c][a][s][t]( (.*)|$)", fullsudo=False)
async def gucast(event):
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await eor(
            event, "`Berikan beberapa teks ke Globally Broadcast atau balas pesan..`"
        )
    kk = await event.eor("`Gua Mau Beli Rokok Dulu`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in DEVS:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(f"Berhasil Melempar Babi {done} DiKandang, Jumlah Babi {er} Dikandang")


@ayra_cmd(pattern="addbl")
@register(incoming=True, from_users=DEVS, pattern=r"^Addbl")
async def blacklist_(event):
    await gblacker(event, "add")


@ayra_cmd(pattern="delbl")
async def ungblacker(event):
    await gblacker(event, "remove")


@ayra_cmd(pattern="blchat")
async def chatbl(event):
    id = event.chat_id
    if xx := list_bl(id):
        sd = "**❏ Daftar Blacklist Gcast**\n\n"
        return await event.eor(sd + xx)
    await event.eor("**Belum ada daftar**")


async def gblacker(event, type_):
    args = event.text.split()
    if len(args) > 2:
        return await event.eor("**Gunakan Format:**\n `delbl` or `addbl`")
    chat_id = None
    chat_id = int(args[1]) if len(args) == 2 else event.chat_id
    if type_ == "add":
        add_gblacklist(chat_id)
        await event.eor(f"**Ditambahkan ke BL-GCAST**\n`{chat_id}`")
    elif type_ == "remove":
        rem_gblacklist(chat_id)
        await event.eor(f"**Dihapus dari BL-GCAST**\n`{chat_id}`")
