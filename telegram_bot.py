import os
import random
import shutil
import sys
import time

from telethon import TelegramClient, events, sync
from variables import groups, get_base_path

if __name__ == '__main__':
    if os.path.exists("session_name.session"):
        path = get_base_path()
        if path is not None:
            filename = os.path.join(path, "session_name.session")
            shutil.copy(filename, os.path.abspath("session_name.session"))
    api_id = 4014948
    api_hash = 'c2774cd88072d9bf329442f1eefa6612'

    client = TelegramClient('session_name', api_id, api_hash)
    client.start()

    for group in groups:
        print(f"Extracting all members for group {group}")
        time.sleep(random.randint(1, 5))
        participants = client.get_participants(group, aggressive=True)
        usernames = [f"@{participant.username}" for participant in participants if participant.username is not None]
        print(f"Extracted {len(usernames)} members for group {group}")
        for username in usernames:
            print(f"Sending message to username {username}")
            client.send_message(username, 'Hello!')
            time.sleep(random.randint(1, 5))


@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.respond('Hey!')
