import pyautogui


class FileControl:
    def save(self):
        pyautogui.hotkey("ctrl", "s")
