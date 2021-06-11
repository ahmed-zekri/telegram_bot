import os
import random
import shutil
import time
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

from telethon import TelegramClient
from win32api import GetSystemMetrics

from variables import api_id_test, api_hash_test
from variables import groups, get_base_path


def launch_campaign():
    client = TelegramClient('session_name', api_id_test, api_hash_test)
    client.start()
    message = telegram_message.get('1.0', 'end-1c')
    for group in groups:
        info.config(text=f"Extracting all members for group {group}")
        window.update()
        time.sleep(random.randint(1, 5))
        participants = client.get_participants(group, aggressive=True)
        usernames = [f"@{participant.username}" for participant in participants if participant.username is not None]
        info.config(text=f"Extracted {len(usernames)} members for group {group}")
        for username in usernames:
            info.config(text=f"Sending message to username {username}")
            window.update()
            client.send_message(username, message.replcae("{username}", username))
            time.sleep(random.randint(1, 5))


def copy_session_in_executable():
    if os.path.exists("session_name.session"):
        path = get_base_path()
        if path is not None:
            filename = os.path.join(path, "session_name.session")
            shutil.copy(filename, os.path.abspath("session_name.session"))


if __name__ == '__main__':
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
    # Info label
    info = tk.Label(text="", fg='#0000CD')

    button = tk.Button(text="Launch campaigns", command=launch_campaign)

    telegram_message_label.pack()
    telegram_message.pack()
    info.pack()
    button.pack()

    window.mainloop()
