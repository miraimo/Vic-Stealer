import ctypes

BLACKLIST: list[str] = [
    "ru-ru",  # Russia
    "be-by",  # Belarus
    "kk-kz",  # Kazakhstan
    "ky-kg",  # Kyrgyzstan
    "tg-tj",  # Tajikistan
    "uz-uz",# Uzbekistan
]

def anti_cis() -> None:
    try:
        kernel32 = ctypes.windll.kernel32 
        lang_id: int = kernel32.GetUserDefaultUILanguage()
        buf = ctypes.create_unicode_buffer(85)
        kernel32.LCIDToLocaleName(lang_id, buf, 85, 0)
    except Exception as err:
        print(err)
        
    if buf.value.lower() in BLACKLIST:
        ctypes.windll.kernel32.ExitProcess(0)