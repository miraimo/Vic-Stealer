# import os

# encrypted_data = b"12345678901234567890v105522146985215"


# dind = encrypted_data.rfind(b"v10")# index 20
# print(dind)
# print(encrypted_data[:dind])
# # b"12345678901234567890"

# print(encrypted_data[dind:dind+3]) #radi tjib liya aya haja mn ba3d i dex 20 htal 23
# # b"v10"

# print(encrypted_data[dind+3:])
# # b"5522146985215"
import sqlite3
import hashlib
from Crypto.Cipher import AES

def decrypt_aes_gcm(cipher_data: bytes, iv: bytes, key: bytes, additional_data=None) -> bytes:
    tag: bytes = cipher_data[-16:]
    cipher = AES.new(key, AES.MODE_GCM, iv)
    if additional_data:
        cipher.update(additional_data)
    decrypt_data: bytes = cipher.decrypt_and_verify(cipher_data[:-16], tag)
    return decrypt_data
    
key: bytes = b'\xf45\x80\xf0\xb8\x88\x05\xb3M{\xcd\xd2\x1c\xb6\x0c>\x83\xfc,U\xf9\x89\x9b:\xa0\x9d4\xee\x9c\xf9\x0c\x02'

with sqlite3.connect(r"C:\Users\yoi\AppData\Local\Yandex\YandexBrowser\User Data\Default\Ya Passman Data") as con:
    curse = con.cursor()
    rows = curse.execute(
        "SELECT origin_url, username_element, username_value, password_element, password_value, signon_realm FROM logins")

    for row in rows.fetchall():
        origin_url, username_element, username_value, password_element, password_value, signon_realm = row


        str_to_hash = origin_url + "\x00" + username_element + "\x00" + username_value + "\x00" + password_element + "\x00" + signon_realm
        hash_object = hashlib.sha1(str_to_hash.encode('utf-8'))
        hash_result = hash_object.digest()
        
        iv: bytes = password_value[:12]
        password_valuee = password_value[12:]
        
        print(decrypt_aes_gcm(password_valuee, iv, key, hash_result))
       
