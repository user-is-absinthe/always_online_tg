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
    me_ = await tg_client.get_me()
    # print(isinstance(me.status, telethon.functions.account.UserStatusOnline()))
    # print(me.status)
    # print('Is User offline?', isinstance(me_.status, telethon.tl.types.UserStatusOffline))
    # print('Is User online?', isinstance(me_.status, telethon.tl.types.UserStatusOnline))
    if isinstance(me_.status, telethon.tl.types.UserStatusOffline):
        print('Сейчас оффлайн. В последний раз был онлайн:')
        print(me_.status.was_online.strftime('%H:%M:%S %d-%m-%Y'))
    elif isinstance(me_.status, telethon.tl.types.UserStatusOnline):
        print('Сейчас онлайн. Вывалиться в оффлайн:')
        print(me_.status.expires.strftime('%H:%M:%S %d-%m-%Y'))
    else:
        print('Я не знаю, что с этим пользователем не так!')
    # print(me.stringify())
    return me_


with tg_client:
    me = tg_client.loop.run_until_complete(main())
