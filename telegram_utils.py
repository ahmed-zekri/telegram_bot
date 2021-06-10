from telethon import TelegramClient


class TeleGramUtils:
    def __init__(self, **kwargs):
        self.app_id = kwargs.get("app_id", "4014948")
        self.api_hash = kwargs.get("api_hash", "c2774cd88072d9bf329442f1eefa6612")
        self.client = TelegramClient('session_name', self.app_id, self.api_hash)

        self.client.start()
