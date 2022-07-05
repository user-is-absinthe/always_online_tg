import datetime
import dateutil.tz
import time
import logging

import telethon

from secret_config import TG_API_ID
from secret_config import TG_API_HASH
from secret_config import SESSION_NAME
from secret_config import PATH_TO_LOG

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(PATH_TO_LOG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)

TIME_TO_WAIT = 15  # подождать после запроса {0} секунд
WAKEUP_TIME = 30  # передернуть онлайн раньше выключения на {0} секунд
CRITICAL_WAIT = TIME_TO_WAIT * 10
LOCAL_TIMEZONE = dateutil.tz.tzlocal()

tg_client = telethon.TelegramClient(SESSION_NAME, TG_API_ID, TG_API_HASH)


async def main():
    me_ = await tg_client.get_me()
    return me_


async def set_online():
    result = await tg_client(telethon.functions.account.UpdateStatusRequest(offline=False))
    return result


with tg_client:
    logger.info('Запустились с {0}.'.format(SESSION_NAME))
    try:
        while True:
            logger.info('Старт!')
            me = tg_client.loop.run_until_complete(main())
            if isinstance(me.status, telethon.tl.types.UserStatusOffline):
                logger.info('Был оффлайн, поставили онлайн.')
                online = tg_client.loop.run_until_complete(set_online())
            elif isinstance(me.status, telethon.tl.types.UserStatusOnline):
                logger.info('Был онлайн, вывалиться в оффлайн через + {0} секунд:'.format(TIME_TO_WAIT))
                before_offline = \
                    me.status.expires.astimezone(LOCAL_TIMEZONE).replace(tzinfo=None) \
                    - datetime.datetime.now() \
                    - datetime.timedelta(seconds=WAKEUP_TIME)
                logger.info(before_offline)
                time.sleep(before_offline.total_seconds())
                logger.info('Подождали это время, поставили онлайн.')
                online = tg_client.loop.run_until_complete(set_online())
            else:
                logger.error('Я не знаю, что с этим пользователем не так! Жду {0} секунд.'.format(CRITICAL_WAIT))
                time.sleep(CRITICAL_WAIT)

            logger.info('Ну и просто подождем {0} секунд.'.format(TIME_TO_WAIT))
            time.sleep(TIME_TO_WAIT)
    except KeyboardInterrupt:
        logger.info('Убито с клаивиатуры.')
