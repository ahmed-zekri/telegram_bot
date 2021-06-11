import os
import random
import shutil
import sys
import time
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

from telethon import TelegramClient, events, sync, hints
from win32api import GetSystemMetrics

from variables import groups, get_base_path, configurable_text


def copy_session_in_executable():
    if os.path.exists("session_name.session"):
        path = get_base_path()
        if path is not None:
            filename = os.path.join(path, "session_name.session")
            shutil.copy(filename, os.path.abspath("session_name.session"))


def launch_campaign():
    button["state"] = "disabled"
    message = telegram_message.get('1.0', 'end-1c')
    for group in groups:
        info.config(text=f"Extracting all members for group {group}")
        window.update()
        time.sleep(random.randint(1, 5))
        participants = client.get_participants(group, aggressive=False)
        while type(participants) != hints.TotalList:
            info.config(text="Invalid response retrying")
            window.update()
            participants = client.get_participants(group, aggressive=False)
            time.sleep(random.randint(1, 5))

        usernames = [f"@{participant.username}" for participant in participants if participant.username is not None]
        info.config(text=f"Extracted {len(usernames)} members for group {group}")
        window.update()
        time.sleep(random.randint(1, 5))
        random.shuffle(usernames)
        for username in usernames:
            info.config(text=f"Sending message to username {username}")
            window.update()
            try:
                client.send_message(username, message.replace("{username}", username))
            except Exception as e:
                info.config(text=f"Error : {e}")
                window.update()
            time.sleep(random.randint(1, 5))
    button["state"] = "normal"


if __name__ == '__main__':
    api_id = 4014948
    api_hash = 'c2774cd88072d9bf329442f1eefa6612'

    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
    random.shuffle(groups)

    copy_session_in_executable()
    # UI building
    window = tk.Tk()
    screen_width = GetSystemMetrics(0)
    screen_height = GetSystemMetrics(1)
    window.geometry(f"{int(screen_width / 2)}x{int(screen_height / 1.8)}")
    window.winfo_toplevel().title("Telegram bot")
    # usernames label
    telegram_message_label = tk.Label(
        text="Enter the message you want to send, you can "
             "use placeholder like this {username} to put the username to every user receiving your message")
    # message input
    telegram_message = ScrolledText(wrap=tk.WORD)
    telegram_message.place(width=int(screen_width / 2), height=int(screen_height / 2))
    telegram_message.insert('1.0', configurable_text)
    # Info label
    info = tk.Label(text="", fg='#0000CD')

    button = tk.Button(text="Launch campaign", command=launch_campaign)

    telegram_message_label.pack()
    telegram_message.pack()
    info.pack()
    button.pack()

    window.mainloop()


@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.respond('Hey!')
