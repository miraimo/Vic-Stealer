import subprocess
import socket
import os

def network_data(folder_path: str) -> None:
    net_info: dict[str, str] = {}
    
    try:
        net_info["dns"] = subprocess.getoutput("ipconfig /displaydns")
    except Exception:
        pass

    try:
        net_info["arp"] = subprocess.getoutput("arp -a")
    except Exception:
        pass

    try:
        net_info["net_stats"] = subprocess.getoutput("netstat -ano")
    except Exception:
        pass

    try:
        net_info["config"] = subprocess.getoutput("ipconfig /all")
    except Exception:
        pass

    try:
        net_info["profiles"] = subprocess.getoutput("netsh wlan show profiles")
    except Exception:
        pass

    try:
        net_info["interfaces"] = socket.gethostbyname_ex(socket.gethostname())[2]
    except Exception:
        pass

    try:
        net_info["open_ports"] = subprocess.getoutput("netstat -an | findstr LISTENING")
    except Exception:
        pass

    try:
        net_info["routes"] = subprocess.getoutput("route print")
    except Exception:
        pass

    try:
        net_info["firewall"] = subprocess.getoutput("netsh advfirewall show allprofiles")
    except Exception:
        pass

    try:
        net_info["mac_addresses"] = subprocess.getoutput("getmac /v /fo csv")
    except Exception:
        pass

    if net_info:
        path_folder_network_info: str = os.path.join(folder_path, "Netword-Info")
        os.makedirs(path_folder_network_info, exist_ok=True)
        for name, value in net_info.items():
            with open(f'{path_folder_network_info}\\{name}.txt', 'w', encoding='utf-8', errors='ignore') as f:
                f.write(str(value))