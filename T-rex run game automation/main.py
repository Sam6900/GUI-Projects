import pyautogui
import time


def jump():
    pyautogui.press('space')

    
# Start the game    
width, height = pg.size()
pyautogui.click(width / 2 - 100, height / 2)
pyautogui.press("space")
  
while True:
    # check if the T-Rex has stopped
    if pyautogui.locateOnScreen('trex_stop.png'):
        break
        
    t_rex_position = pyautogui.locateOnScreen('trex_run.png') 
    obstacle_small = pyautogui.locateOnScreen('obstacle_small.png')
    obstacle_large = pyautogui.locateOnScreen('obstacle_large.png')
    
    if obstacle_small and obstacle_small[0] - trex_pos[0] < 100:
        pg.press("space")
    if obstacle_large and obstacle_large[0] - trex_pos[0] < 100:
        pg.press("space")
            
    time.sleep(0.5)
