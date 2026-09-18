import win32api
import ctypes
import wmi
import ctypes
from modules.errorMessage.errorMessage import show_message_box
# from modules.fackerror.fackerror import fackError


# https://github.com/kkent030315/detect-anyrun.git

class Anti_Analysis:
    def __init__(self):
        self.debuge_check()
        self.ckeck_process()

# extract all process and check the BLACK_LIST_PROCESS 
    def ckeck_process(self) -> None:
        BLACK_LIST_PROCESS: list[str] = [
            "ida64.exe", "ghidra.exe", "radare2.exe", "cutter.exe",
            "binaryninja.exe", "pe-bear.exe", "die.exe", "pestudio.exe",
            "cff-explorer.exe", "exeinfope.exe", "dnspy.exe", "ilspy.exe",
            "de4dot.exe", "yara.exe", "strings.exe", "binwalk.exe",
            "peid.exe", "x64dbg.exe", "ollydbg.exe", "windbg.exe",
            "immunitydebugger.exe", "procmon.exe", "processhacker.exe",
            "processexplorer.exe", "apimonitor.exe", "tcpview.exe",
            "wireshark.exe", "fiddler.exe", "sysmon.exe", "autoruns.exe",
            "regshot.exe", "volatility.exe", "rekall.exe", "redline.exe",
            "ftk-imager.exe", "cuckoo.exe", "capa.exe", "unicorn.exe",
            "qemu.exe", "capstone.exe", "keystone.exe"
        ] 

        c: object = wmi.WMI()
        for process in c.Win32_Process():
            if process.Name.lower() in BLACK_LIST_PROCESS:
                # show_message_box(f"Detected blacklisted process: {process.Name}", "labob")
                ctypes.windll.kernel32.ExitProcess(0)

    def debuge_check(self) -> None:
        if ctypes.windll.kernel32.IsDebuggerPresent():
            ctypes.windll.kernel32.ExitProcess(0)
        

        has_debugger = ctypes.c_bool(False)
        process_handle = win32api.GetCurrentProcess()
        ctypes.windll.kernel32.CheckRemoteDebuggerPresent(process_handle, ctypes.byref(has_debugger))
        
        if has_debugger.value:
            # show_message_box(f"debug ", "labob")
            
            ctypes.windll.kernel32.ExitProcess(0)

        ntdll = ctypes.windll.ntdll
        
        ProcessDebugPort = 7
        
        debug_port = ctypes.c_ulong(0)
        
        ntdll.NtQueryInformationProcess(
            ctypes.windll.kernel32.GetCurrentProcess(),
            ProcessDebugPort,
            ctypes.byref(debug_port),
            ctypes.sizeof(debug_port),
            None
        )
        
        if debug_port.value != 0:
            
            ctypes.windll.kernel32.ExitProcess(0)