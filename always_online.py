import asyncio
import datetime
import dateutil.tz
import time

import telethon

from secret_config import TG_API_ID
from secret_config import TG_API_HASH
from secret_config import SESSION_NAME

TIME_TO_WAIT = 15
WAKEUP_TIME = 30
LOCAL_TIMEZONE = dateutil.tz.tzlocal()

tg_client = telethon.TelegramClient(SESSION_NAME, TG_API_ID, TG_API_HASH)


async def main():
    me_ = await tg_client.get_me()
    return me_


async def set_online(client):
    result = client(telethon.functions.account.UpdateStatusRequest(offline=False))
    return result


with tg_client:
    while True:
        me = tg_client.loop.run_until_complete(main())
        if isinstance(me.status, telethon.tl.types.UserStatusOffline):
            # пользователь оффлайн, дергаем его в онлайн сейчас
            print(me.status.was_online.strftime('%H:%M:%S %d-%m-%Y'))
            # set_online(client=tg_client)
            asyncio.run(set_online(client=tg_client))
            # if set_online(client=tg_client):
            #     print(
            #         'Я был оффлайн, стал онлайн до {0}.'.format(
            #             me.status.was_online.astimezone(LOCAL_TIMEZONE).strftime('%H:%M:%S %d-%m-%Y')
            #         ))
            # else:
            #     print('Я хотел стать онлайн, но не прокатило.')

        elif isinstance(me.status, telethon.tl.types.UserStatusOnline):
            # пользователь онлайн, но перейдет в оффлайн через время
            print(me.status.expires.strftime('%H:%M:%S %d-%m-%Y'))
            # time_to_offline_utc = me.status.expires
            # time_to_offline = time_to_offline_utc.astimezone(LOCAL_TIMEZONE)
            before_offline = \
                datetime.datetime.now() - me.status.expires.astimezone(LOCAL_TIMEZONE).replace(tzinfo=None)
            print('Вывалиться в оффлайн через:')
            print(before_offline)
            # - datetime.timedelta(seconds=30)
            # time.sleep(before_offline - datetime.timedelta(seconds=WAKEUP_TIME))
        else:
            print('Я не знаю, что с этим пользователем не так!')

        time.sleep(TIME_TO_WAIT)
        break
