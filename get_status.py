# import asyncio
# import time

import telethon

# from telethon import TelegramClient
# from telethon import functions
# from telethon import errors

from secret_config import TG_API_ID
from secret_config import TG_API_HASH
from secret_config import SESSION_NAME

tg_client = telethon.TelegramClient(SESSION_NAME, TG_API_ID, TG_API_HASH)

TIME_TO_WAIT = 15


async def main():
    # Getting information about yourself
    me = await tg_client.get_me()
    #
    # # "me" is a user object. You can pretty-print
    # # any Telegram object with the "stringify" method:
    print(me.stringify())
    #
    # # When you print something, you see a representation of it.
    # # You can access all attributes of Telegram objects with
    # # the dot operator. For example, to get the username:
    username = me.username
    print(username)
    print(me.phone)
    # result = tg_client(telethon.functions.account.UpdateStatusRequest(
    #     offline=False
    # ))
    # print(result)


with tg_client:
    tg_client.loop.run_until_complete(main())

    # result = tg_client(telethon.functions.account.UpdateStatusRequest(
    #     offline=False
    # ))
    # print(result)
