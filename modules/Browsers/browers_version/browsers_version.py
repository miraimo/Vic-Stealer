import os
import win32api


def get_file_version(exe_path: str) -> str | None:
    if not exe_path or not os.path.isfile(exe_path):
        return None

    try:
        info = win32api.GetFileVersionInfo(exe_path, "\\")
        ms = info["FileVersionMS"]
        ls = info["FileVersionLS"]

        return f"{ms >> 16}.{ms & 0xffff}.{ls >> 16}.{ls & 0xffff}"

    except Exception:
        return None


def all_browsers_version(folder: str)-> None:

    APPDATA = os.getenv("APPDATA")
    LOCALAPPDATA = os.getenv("LOCALAPPDATA")
    PROGRAMFILES = os.getenv("PROGRAMFILES")
    PROGRAMFILES_X86 = os.getenv("PROGRAMFILES(X86)")

    browsers = {

        "opera": {
            "path_data": os.path.join(
                APPDATA, "Opera Software", "Opera Stable"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "Programs",
                "Opera",
                "opera.exe"
            ),
            "key_name": "Opera Stable"
        },

        "opera-gx": {
            "path_data": os.path.join(
                LOCALAPPDATA,
                "Opera Software",
                "Opera GX Stable"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "Programs",
                "Opera GX",
                "opera.exe"
            ),
            "key_name": "Opera GX Stable"
        },

        "amigo": {
            "path_data": os.path.join(
                APPDATA,
                "Amigo",
                "User Data"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "Amigo",
                "Application",
                "amigo.exe"
            ),
            "key_name": "Amigo Browserkey1"
        },

        "torch": {
            "path_data": os.path.join(
                APPDATA,
                "Torch",
                "User Data"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "Torch",
                "Application",
                "torch.exe"
            ),
            "key_name": "Torch Media Inc.key1"
        },

        "kometa": {
            "path_data": os.path.join(
                APPDATA,
                "Kometa",
                "User Data"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "Kometa",
                "Application",
                "kometa.exe"
            ),
            "key_name": "Kometa Browserkey1"
        },

        "orbitum": {
            "path_data": os.path.join(
                APPDATA,
                "Orbitum",
                "User Data"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "Orbitum",
                "Application",
                "orbitum.exe"
            ),
            "key_name": "Orbitum Browserkey1"
        },

        "cent-browser": {
            "path_data": os.path.join(
                APPDATA,
                "CentBrowser",
                "User Data"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "CentBrowser",
                "Application",
                "chrome.exe"
            ),
            "key_name": "Cent Studio Browserkey1"
        },

        "7star": {
            "path_data": os.path.join(
                APPDATA,
                "7Star",
                "7Star",
                "User Data"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "7Star",
                "Application",
                "7star.exe"
            ),
            "key_name": "7Star Browserkey1"
        },

        "sputnik": {
            "path_data": os.path.join(
                APPDATA,
                "Sputnik",
                "Sputnik",
                "User Data"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "Sputnik",
                "Application",
                "sputnik.exe"
            ),
            "key_name": "Sputnik Browserkey1"
        },

        "vivaldi": {
            "path_data": os.path.join(
                LOCALAPPDATA,
                "Vivaldi",
                "User Data"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "Vivaldi",
                "Application",
                "vivaldi.exe"
            ),
            "key_name": "Vivaldi Technologieskey1"
        },

        "google-chrome-sxs": {
            "path_data": os.path.join(
                LOCALAPPDATA,
                "Google",
                "Chrome SxS",
                "User Data"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "Google",
                "Chrome SxS",
                "Application",
                "chrome.exe"
            ),
            "key_name": "Google Chrome SxSkey1"
        },

        "google-chrome": {
            "path_data": os.path.join(
                LOCALAPPDATA,
                "Google",
                "Chrome",
                "User Data"
            ),
            "exe_path": os.path.join(
                PROGRAMFILES,
                "Google",
                "Chrome",
                "Application",
                "chrome.exe"
            ),
            "key_name": "Google Chromekey1"
        },

        "epic-privacy-browser": {
            "path_data": os.path.join(
                LOCALAPPDATA,
                "Epic Privacy Browser",
                "User Data"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "Epic Privacy Browser",
                "Application",
                "epic.exe"
            ),
            "key_name": "Epic Softwarekey1"
        },

        "microsoft-edge": {
            "path_data": os.path.join(
                LOCALAPPDATA,
                "Microsoft",
                "Edge",
                "User Data"
            ),
            "exe_path": os.path.join(
                PROGRAMFILES_X86,
                "Microsoft",
                "Edge",
                "Application",
                "msedge.exe"
            ),
            "key_name": "Microsoft Edge"
        },

        "uran": {
            "path_data": os.path.join(
                LOCALAPPDATA,
                "uCozMedia",
                "Uran",
                "User Data"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "uCozMedia",
                "Uran",
                "Application",
                "uran.exe"
            ),
            "key_name": "uCoz Media Urankey1"
        },

        "brave": {
            "path_data": os.path.join(
                LOCALAPPDATA,
                "BraveSoftware",
                "Brave-Browser",
                "User Data"
            ),
            "exe_path": os.path.join(
                PROGRAMFILES,
                "BraveSoftware",
                "Brave-Browser",
                "Application",
                "brave.exe"
            ),
            "key_name": "Brave Softwarekey1"
        },

        "iridium": {
            "path_data": os.path.join(
                LOCALAPPDATA,
                "Iridium",
                "User Data"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "Iridium",
                "Application",
                "iridium.exe"
            ),
            "key_name": "Iridium Browserkey1"
        },

        "yandex": {
            "path_data": os.path.join(
                LOCALAPPDATA,
                "Yandex",
                "YandexBrowser",
                "User Data"
            ),
            "exe_path": os.path.join(
                LOCALAPPDATA,
                "Yandex",
                "YandexBrowser",
                "Application",
                "browser.exe"
            ),
            "key_name": None
        }
    }

    # Add version for each browser
    for browser in browsers.values():
        browser["version"] = get_file_version(
            browser["exe_path"]
        )

    for name, browser in browsers.items():
        with open(os.path.join(folder, "browsers_version.txt"), 'a', encoding='utf-8') as f:
            if browser["version"]:
                f.write(
                    f"{name:<25} >>> {browser['version']}\n"
                )