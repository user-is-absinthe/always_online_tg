from telethon.sync import TelegramClient
from telethon import functions

from secret_config import TG_API_ID
from secret_config import TG_API_HASH
from secret_config import SESSION_NAME


with TelegramClient(SESSION_NAME, TG_API_ID, TG_API_HASH) as client:
    result = client(functions.account.UpdateStatusRequest(
        offline=False
    ))
    print(result)
