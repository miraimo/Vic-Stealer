import win32api
import win32con

# Syntax: MessageBox(hWnd, text, caption, type)
def show_message_box(message, title):
    win32api.MessageBox(0, message, title, win32con.MB_OK)