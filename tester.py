from typing import Counter
import pyautogui
import keyboard
import time
from termcolor import colored
from datetime import datetime

def set_check():
    #locate center of set_3.png and log x,y
    try:
        set_3 = pyautogui.locateCenterOnScreen('set_3.png', region=(660, 760, 1240, 260), confidence=0.9)
        #print(set_3)
        print(colored(f"set_3.png located at {set_3} with confidence 0.9", 'green'))
        #locate center of set_3.png with confidence 0.8 and log x,y
        set_3 = pyautogui.locateCenterOnScreen('set_3.png', region=(660, 760, 1240, 260), confidence=0.8)
        #print(set_3)
        print(colored(f"set_3.png located at {set_3} with confidence 0.8", 'green'))
        #locate center of set_3.png with confidence 0.7 and log x,y
        #set_3 = pyautogui.locateCenterOnScreen('set_3.png', region=(660, 760, 1240, 260), confidence=0.7)
        #print(set_3)
        #for set_0 iprint(colored(f"set_3.png located at {list(set_3)} with confidence 0.7", 'green'))
        ##locate center of set_3.png with confidence 0.6 and log x,y
        #set_3 = pyautogui.locateCenterOnScreen('set_3.png', region=(660, 760, 1240, 260), confidence=0.6)
        #print(set_3)
        #for set_0 iprint(colored(f"set_3.png located at {list(set_3)} with confidence 0.6", 'green'))
        ##locate center of set_3.png with confidence 0.5 and log x,y
        #set_3 = pyautogui.locateCenterOnScreen('set_3.png', region=(660, 760, 1240, 260), confidence=0.5)
        #print(set_3)
        #for set_0 iprint(colored(f"set_3.png located at {list(set_3)} with confidence 0.5", 'green'))
    except:
        print(colored(f"set_3.png not found", 'red'))


while keyboard.is_pressed('q') == False:
    set_check()
    time.sleep(1)