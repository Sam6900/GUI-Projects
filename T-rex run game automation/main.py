import pyautogui
import time


def jump():
    pyautogui.press('space')

    
# Start the game    
width, height = pg.size()
pyautogui.click(width / 2 - 100, height / 2)
pyautogui.press("space")
    
