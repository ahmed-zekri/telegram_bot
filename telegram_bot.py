import argparse
import os
import random
import re
import shutil
import sys
import time
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import socks
# TODO             DO NOT REMOVE sync !!!!!!!
from telethon import TelegramClient, events, sync, hints
from win32api import GetSystemMetrics

from variables import groups, get_base_path, configurable_text, api_id, api_hash, proxies

account_index = 0
proxy_index = 0


# Determine if application is a script file or frozen exe
def check_app_is_exe():
    return getattr(sys, 'frozen', False)


def copy_data_files_to_executable_dir(filename):
    if os.path.exists(filename):
        path = get_base_path()
        if path == '':
            return
        filename = os.path.join(path, filename)

        shutil.copy(filename, os.path.abspath(filename))
    else:
        session_id = re.findall('.(\d)', filename)
        if len(session_id) == 1:
            print(f'Login for account {session_id[0]}')
            c = TelegramClient(f'session_name.{session_id[0]}', api_id[int(session_id[0])],
                               api_hash[int(session_id[0])])
            c.start()
            c.disconnect()
            time.sleep(1)
            copy_data_files_to_executable_dir(f'session_name.{session_id[0]}.session')


def rotate_proxy():
    global proxy_index

    proxy_index = random.randint(0, len(proxies) - 1)
    proxy = dict(proxy_type=socks.HTTP, addr=re.findall("@([\d.]+):", proxies[proxy_index])[0],
                 port=int(re.findall(":([\d]+)", proxies[proxy_index])[0]),
                 username=re.findall("/([\w\d]+)", proxies[proxy_index])[0],
                 password=re.findall(":([\w\d]+)@", proxies[proxy_index])[0])
    client.set_proxy(proxy)


def check_username_received(username):
    with open(file='sent_users', mode='r') as file:
        usernames = file.read().split('\n')
    return username in usernames


def launch_campaign():
    global proxy_index
    global account_index
    global client
    if gui:
        button["state"] = "disabled"
        message = telegram_message.get('1.0', 'end-1c')
    else:
        message = configurable_text
    for group in groups:
        if gui:
            info.config(text=f"Extracting all members for group {group}")
            window.update()
        else:
            print(f"Extracting all members for group {group}")

        time.sleep(random.randint(1, 5))

        try:
            participants = client.get_participants(group, aggressive=False)

        except:
            time.sleep(3)
            if gui:
                info.config(text=f"Couldn't extract members for group {group}, skipping,")
                window.update()
            else:
                print(f"Couldn't extract members for group {group}, skipping,")
            continue
        while type(participants) != hints.TotalList:
            if gui:
                info.config(text="Invalid response retrying")
                window.update()
            else:
                print("Invalid response retrying")

            participants = client.get_participants(group, aggressive=False)
            time.sleep(random.randint(1, 5))

        usernames = [f"@{participant.username}" for participant in participants if participant.username is not None]
        if gui:
            info.config(text=f"Extracted {len(usernames)} members for group {group}")
            window.update()
        else:
            print(f"Extracted {len(usernames)} members for group {group}")

        time.sleep(random.randint(1, 5))
        random.shuffle(usernames)
        for username in usernames:
            if check_username_received(username):
                if gui:
                    info.config(text=f"{username} already received the message")
                    window.update()
                else:
                    print(f"{username} already received the message")
                continue

            if gui:
                info.config(text=f"Sending message to username {username}" + (
                    f" using proxy {proxies[proxy_index]} " if use_proxy else ""))
                window.update()
            else:
                print(f"Sending message to username {username}" + (
                    f" using proxy {proxies[proxy_index]} " if use_proxy else ""))

            attempts = 0
            while True:
                try:
                    attempts += 1
                    if use_proxy:
                        rotate_proxy()
                    client.send_message(username, message.replace("{username}", username))

                    with open(file="sent_users", mode="a+") as file:
                        file.write(f"{username}\n")
                    break
                except Exception as e:
                    if attempts >= message_send_attempts:
                        if gui:
                            info.config(text=f"Error : {e},Reached max number of attempts, proceeding to next user")
                            window.update()
                        else:
                            print(f"Error : {e},Reached max number of attempts, proceeding to next user")

                        break

                    proxy_index = random.randint(0, len(proxies) - 1)
                    account_index += 1
                    if account_index > len(api_id) - 1:
                        account_index = 0
                    client.disconnect()

                    client = TelegramClient(f'session_name.{account_index}', api_id[account_index],
                                            api_hash[account_index])

                    if gui:
                        info.config(
                            text=f"Couldn't send message {e}, Switching to account {account_index}" + (
                                f" with proxy {proxies[proxy_index]}" if use_proxy else "") + f", attempts remaining :{message_send_attempts - attempts}")
                        window.update()
                    else:
                        print(
                            f"Couldn't send message {e}, Switching to account {account_index}" + (
                                f" with proxy {proxies[proxy_index]}" if use_proxy else "") + f", attempts remaining :{message_send_attempts - attempts}")

                    client.start()
                    sleeping_time = random.randint(60, 120)
                    if gui:
                        info.config(text=f"Sleeping for {sleeping_time} seconds")
                        window.update()
                    else:
                        print(f"Sleeping for {sleeping_time} seconds")

                    time.sleep(sleeping_time)

    if gui:
        button["state"] = "normal"
    else:
        launch_campaign()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Telegram bot to launch campaigns")
    parser.add_argument("-ng", '--no-gui', default=True, help='Disable gui', action='store_false')
    parser.add_argument("-p", '--use-proxy', default=False, help='Use proxies', action='store_true')
    parser.add_argument("-m", '--message-attempts', type=int, default=20,
                        help='Maximum attempts allowed to send a message')
    args = parser.parse_args()
    gui = args.no_gui
    use_proxy = args.use_proxy
    message_send_attempts = args.message_attempts

    for _ in range(len(api_id)):
        copy_data_files_to_executable_dir(f"session_name.{_}.session")
    copy_data_files_to_executable_dir("sent_users")

    client = TelegramClient(f'session_name.{account_index}', api_id[account_index], api_hash[account_index])
    client.start()
    random.shuffle(groups)

    if not gui:
        launch_campaign()
        sys.exit()
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
