import asyncio
from telethon import TelegramClient, events

from secret_config import SESSION_NAME
from secret_config import TG_API_ID as api_id
from secret_config import TG_API_HASH as api_hash

import logging
logging.basicConfig(level=logging.DEBUG)

# with TelegramClient(SESSION_NAME, api_id, api_hash) as client:
#     client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))


async def main():
    client = TelegramClient(SESSION_NAME, api_id, api_hash)
    await client.start()

asyncio.run(main())
