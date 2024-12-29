import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from RadhaMusic import LOGGER, app, userbot
from RadhaMusic.core.call import AMBOTOP
from RadhaMusic.misc import sudo
from RadhaMusic.plugins import ALL_MODULES
from RadhaMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("RadhaMusic.plugins" + all_module)
    LOGGER("RadhaMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await AMBOTOP.start()
    try:
        await AMBOTOP.stream_call("https://files.catbox.moe/r58ihg.mp4")
    except NoActiveGroupCall:
        LOGGER("RadhaMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await AMBOTOP.decorators()
    LOGGER("RadhaMusic").info(
        " Radha Music Start Hoga ab"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("RadhaMusic").info("Stopping Radha Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
