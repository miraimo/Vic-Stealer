from typing import Any

class Login:
    def __init__(self, browser_name:  str, url: str, username: str, password: str, profile) -> None:
        self.profile = profile
        self.browser_name = browser_name
        self.url = url
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return f'\nBrowser Name: {self.browser_name} \n {self.profile} )\nurl: {self.url}\nusername: {self.username}\npassword: {self.password}\n'

class Cookies:
    def __init__(self, host_key: str, name:  str, path: str, cookies_value: bytes, expires_utc: str) -> None:
        self.host_key = host_key
        self.name = name
        self.path = path
        self.cookies_value = cookies_value
        self.expires_utc = expires_utc
        
    def to_list_(self) -> list[str]:
        return [self.host_key, "FALSE" if self.expires_utc == 0 else "TRUE", self.path, "FALSE" if self.host_key.startswith(".") else "TRUE", self.expires_utc, self.name, self.cookies_value[32:].decode()]

class AutoFill:
    def __init__(self, name: str, value: str, browser_name: str):
        self.name = name
        self.value = value
        self.browser_name = browser_name

    def __str__(self) -> str:
        return f"Browser Name{self.browser_name}\n\nName: {self.name}\nValue: {self.value}\n\n{'*'*12}\n\n"

class Credits:
    def __init__(self, name_on_card: Any, expiration_month: Any, expiration_year: Any, card_number_encrypted: Any, date_modified: Any) -> None:
        self.name_on_card = name_on_card
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
        self.card_number_encrypted = card_number_encrypted
        self.date_modified = date_modified

    def __str__(self) -> str:
        return f'\nName: {self.name_on_card}\nMonth : {self.expiration_month}\nYear: {self.expiration_year}\nCard Number:{self.card_number_encrypted.decode()}\nDate: {self.date_modified}\n{"-"*24}'

class Downloads:
    def __init__(self, tab_url: str, target_path: str) -> None:
        self.tab_url = tab_url
        self.target_path = target_path

    def __str__(self) -> str:
        return f'{self.tab_url}\t\t{self.target_path}'

class History:
    def __init__(self, title: str, url: str) -> None:
        self.title = title
        self.url = url

    def __str__(self) -> str:
        return f'title: {self.title}\nurl: {self.url}'