# Foobar

Telegram bot is a Python bot build using telethon library This bot allows for sending a specific message to many users
of specific groups.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Telethon.

```bash
pip install Telethon
```

## Usage

Open variables.py and fill the array proxies with your proxies if you have, Then, enter the app_id and the api_hash of
every telegram account that will be used. For more information on how to get those please
visit https://my.telegram.org/auth?to=apps
and proceed to fill the given forms, you'll obtain your api_id and api_hash. Finally, fill the groups array with the
names of your target groups that you want to send message to their members

```bash
Telegram bot to launch campaigns

optional arguments:
  -h, --help            show this help message and exit
  -ng, --no-gui         Disable gui
  -p, --use-proxy       Use proxies (specified in variables.py)
  -ma MESSAGE_ATTEMPTS, --message-attempts MESSAGE_ATTEMPTS
                        Maximum attempts allowed to send a message
  -n ACCOUNT_NUMBERS, --account_numbers ACCOUNT_NUMBERS
                        Accounts used to send the messages (Accounts specified in variables.py by their api_id and api_hash)
  -w MESSAGE_WAIT, --message_wait MESSAGE_WAIT
                        Time to wait between each sent message
  -cm CAMPAIGN_MESSAGE, --campaign_message CAMPAIGN_MESSAGE
                        Text to be sent in the campaign, can only be run on no
                        gui mode (Message can also be specified in variables.py)

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
 