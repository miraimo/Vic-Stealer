import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False
    
def run_as_admin():
    if not is_admin():
        result = ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            sys.executable,
            " ".join(f'"{arg}"' for arg in sys.argv),
            None,
            1
        )

        if result > 32:
            # New elevated process started successfully
            sys.exit()
        else:
            # Failed to start elevated process
            pass