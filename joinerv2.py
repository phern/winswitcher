import win32gui
import pyautogui


def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


if __name__ == "__main__":
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "<name of window you want to target>" in i[1].lower():
            win32gui.ShowWindow(i[0], 5)
            win32gui.SetForegroundWindow(i[0])
            pyautogui.typewrite('<placeholder>')
            pyautogui.press('<placeholder>')