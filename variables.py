import sys

# Protocol can be socks5 , http,https....
proxies = ['protocol://ip:username@password:password', 'protocol://ip:username@password:password',
           'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
           'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
           'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
           'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
           'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
           'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
           'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
           'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
           'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
           'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
           'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
           'protocol://ip:username@password:password', 'protocol://ip:username@password:password',
           'protocol://ip:username@password:password']
groups = ['@Group1', '@Group2', '@Group3']

api_id = ['api_id1', 'api_id2', 'api_id3']
api_hash = ['api_hash1', 'api_hash_2', 'api_hash3']


def get_base_path():
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        return sys._MEIPASS

    except Exception:
        return ''


configurable_text = "Hey {username} This is our campaign message"
