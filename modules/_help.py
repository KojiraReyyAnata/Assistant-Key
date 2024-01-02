# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

from Ayra.dB._core import HELP, LIST
from Ayra.fns.tools import cmd_regex_replace
from telethon.errors.rpcerrorlist import (BotInlineDisabledError,
                                          BotMethodInvalidError,
                                          BotResponseTimeoutError)
from telethon.tl.custom import Button

from . import HNDLR, LOGS, asst, ayra_cmd, get_string

_main_help_menu = [
    [
	@@ -21,81 +18,24 @@
]


@ayra_cmd(pattern="[hH][eE][lL][pP]( (.*)|$)")
async def _help(ayra):
    plug = ayra.pattern_match.group(1).strip()
    chat = await ayra.get_chat()
    if plug:
        try:
            if plug in HELP["Official"]:
                output = f"**Plugin** - `{plug}`\n"
                for i in HELP["Official"][plug]:
                    output += i
                output += "\n© @Pusingeaak"
                await ayra.eor(output)
            else:
                try:
                    x = get_string("help_11").format(plug)
                    for d in LIST[plug]:
                        x += HNDLR + d
                        x += "\n"
                    x += "\n© @Pusingeaak"
                    await ayra.eor(x)
                except BaseException:
                    file = None
                    compare_strings = []
   for file_name in LIST:
                        compare_strings.append(file_name)
                        value = LIST[file_name]
                        for j in value:
                            j = cmd_regex_replace(j)
                            compare_strings.append(j)
                            if j.strip() == plug:
                                file = file_name
                                break
                    if not file:
                        # the enter command/plugin name is not found
                        text = f"`{plug}` is not a valid plugin!"
                        if best_match := next(
                            (
                                _
                                for _ in compare_strings
                                if plug in _ and not _.startswith("_")
                            ),
                            None,
                        ):
                            text += f"\nDid you mean `{best_match}`?"
                        return await ayra.eor(text)
                    output = f"**Perintah** `{plug}` **ditemukan dalam** - `{file}`\n"
                    if file in HELP["Official"]:
                        for i in HELP["Official"][file]:
                            output += i
                    output += "\n© @Pusingeaak"
                    await ayra.eor(output)
        except BaseException as er:
            LOGS.exception(er)
            await ayra.eor("Error 🤔 occured.")
    else:
        try:
   
