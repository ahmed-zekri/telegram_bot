import random
import time

from telethon import TelegramClient, events, sync
from variables import groups

if __name__ == '__main__':

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
