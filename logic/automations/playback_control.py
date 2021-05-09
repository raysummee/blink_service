import pyautogui


class PlaybackControl:
    def play_pause(self):
        pyautogui.press("space")

    def record(self):
        pyautogui.press("*")

    def go_to_beginning(self):
        pyautogui.press(",")