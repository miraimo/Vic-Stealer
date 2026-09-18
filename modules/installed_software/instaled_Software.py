import winreg
import os

def get_installed_programs(path_file: str) -> None:
    programs = []

    registry_paths = [
        (
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        ),
        (
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
        ),
        (
            winreg.HKEY_CURRENT_USER,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
        ),
    ]

    for hive, path in registry_paths:
        try:
            key = winreg.OpenKey(hive, path)

            for i in range(winreg.QueryInfoKey(key)[0]):
                try:
                    subkey_name = winreg.EnumKey(key, i)
                    subkey = winreg.OpenKey(key, subkey_name)

                    try:
                        name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                    except FileNotFoundError:
                        name = None

                    try:
                        version = winreg.QueryValueEx(subkey, "DisplayVersion")[0]
                    except FileNotFoundError:
                        version = None

                    if name:
                        programs.append({
                            "name": name,
                            "version": version
                        })

                    winreg.CloseKey(subkey)

                except OSError:
                    continue

            winreg.CloseKey(key)

        except OSError:
            continue
    with open(os.path.join(path_file, "installedSoftware.txt"), 'w', encoding='utf-8') as f:
        for program in programs:
            f.write(
                f'{program["name"]}'
                + (f' - {program["version"]}' if program["version"] else '')
                + '\n'
            )
