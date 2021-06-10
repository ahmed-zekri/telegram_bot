import asyncio

from telethon import TelegramClient, events, sync
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types import ChannelParticipantsSearch

if __name__ == '__main__':
    # These example values won't work. You must get your own api_id and
    # api_hash from https://my.telegram.org, under API Development.
    api_id = 4014948
    api_hash = 'c2774cd88072d9bf329442f1eefa6612'

    client = TelegramClient('session_name', api_id, api_hash)
    client.start()

    # print(client.get_me().stringify())

    # client.send_message('@captseagull', 'Hello! Talking to you from a bot ')
    all_participants = []
    participants = client.get_participants("@Farmingroom", aggressive=True)
    print(participants)

    # client.send_file('username', '/home/myself/Pictures/holidays.jpg')

    # client.download_profile_photo('me')
    # messages = client.get_messages('username')
    # messages[0].download_media()


@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.respond('Hey!')
