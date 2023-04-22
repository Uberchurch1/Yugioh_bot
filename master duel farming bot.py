#master duel farming bot
from typing import Counter
import pyautogui
import keyboard
import time
from termcolor import colored
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")


def click_event(x, y, t):
    
    pyautogui.click(x, y)
    time.sleep(t)


def start_match():
    #checks if duel button is available in two places and clicks it
    #use pyautogui to check if the pixel 1661,1139 is the same color as 203,253,0 and the pixel color combination 1862,1153,0,0,0 is true
    try:
        print((current_time), ('[LOG] Start Match'))
        if pyautogui.pixelMatchesColor(1661, 1139, (203, 253, 0)) and pyautogui.pixelMatchesColor(1862, 1153, (0, 0, 0)):
            #print current time and action performed
            click_event(1862, 1153, 0.5)
            #log match started
            print((current_time), ('[LOG] Match Started'))
    except:
        print((current_time), ('[LOG] Start Match Not Found'))

def coin_flip():
    #checks if coin flip is available and clicks it
    #check if pixel color combo 833,1098,203,253,0 and 958,1128,194,242,0 are true then click the second pixel
    try:
        print((current_time), ('[LOG] Coin Flip'))
        if pyautogui.pixelMatchesColor(833, 1098, (203, 253, 0)) and pyautogui.pixelMatchesColor(958, 1128, (194, 242, 0)):
            #print current time and action performed
            click_event(958, 1128, 0.5)
    except:
        print((current_time), ('[LOG] Coin Flip Not Found'))

def player_turn():
    #try locate main.png and log player turn then click on center main.png
    try:
        main = pyautogui.locateCenterOnScreen('main.png', confidence=0.8)
        print((current_time), ('[LOG] Player Turn'))
        #click on main using click_event function
        click_event(main[0], main[1], 0.5)
        if pyautogui.pixelMatchesColor(2026, 1010, (253, 253, 251)):
            #log phase skip and click pixel
            print((current_time), ('[LOG] Phase Skip'))
            #click pixel 2026,1010,253,253,251
            click_event(2026, 1010, 0.5)
    except:
        print((current_time), ('[LOG] Main Not Found'))
    #check if 1974,670,34,134,199 and 601,596,83,189,251 and 444,1160,43,253,251 pixel colors are correct then click the first pixel
    if pyautogui.pixelMatchesColor(444, 1160, (43, 253, 251)):
        #print current time and action performed
        print((current_time), ('[LOG] Player Turn'))
        click_event(1974, 670, 0.5)
        #check if 2026,1010,253,253,251 and click pixel
        if pyautogui.pixelMatchesColor(2026, 1010, (253, 253, 251)):
            #log phase skip and click pixel
            print((current_time), ('[LOG] Phase Skip'))
            #click pixel 2026,1010,253,253,251
            click_event(2026, 1010, 0.5)

def discard():
    #check if 1856,832,59,159,246 and 949,1069,97,77,42 then click second pixel
    try:
        #log discard
        print((current_time), ('[LOG] Discard'))
        if pyautogui.pixelMatchesColor(1856, 832, (59, 159, 246)):

            #print current time and action performed
            print((current_time), ('[LOG] Start Discard'))
            #click pixel 949,1069,97,77,42
            click_event(949, 1069, 0.5)
            #check if 1117,1344,203,253,0 and 1237,1352,166,207,0 then click second pixel
            if pyautogui.pixelMatchesColor(1117, 1344, (203, 253, 0)) and pyautogui.pixelMatchesColor(1237, 1352, (166, 207, 0)):
                #print current time and action performed
                print((current_time), ('[LOG] Complete Discard'))
                #click pixel 1237,1352,166,207,0
                click_event(1237, 1352, 0.5)
    except:
        print((current_time), ('[LOG] Discard Not Found'))

def game_end():
    try:
        print((current_time), ('[LOG] Game End'))
        #check 1060,1066,27,127,199 and 968,1265,203,253,0 and 1286,1293,203,253,0 and click third pixel
        if pyautogui.pixelMatchesColor(1060, 1066, (27, 127, 199)) and pyautogui.pixelMatchesColor(968, 1265, (203, 253, 0)) and pyautogui.pixelMatchesColor(1286, 1293, (203, 253, 0)):
            #print current time and action performed
            #click pixel 1286,1293,203,253,0
            click_event(1286, 1293, 0.5)
            #log game ended
            print((current_time), ('[LOG] Game Ended'))
    except:
        print((current_time), ('[LOG] Game End Not Found'))

def duel_pass():
    #check 1889,1299,203,253,0 and 2120,1325,194,242,0 and click second pixel
    if pyautogui.pixelMatchesColor(1889, 1299, (203, 253, 0)) and pyautogui.pixelMatchesColor(2120, 1325, (194, 242, 0)):
        #print current time and action performed
        print((current_time), ('[LOG] Duel Pass'))
        #click pixel 2120,1325,194,242,0
        click_event(2120, 1325, 0.5)

def duel_score():
    #check 2049,1287,203,253,0 adn 2175,1316,202,252,0 and click second pixel
    if pyautogui.pixelMatchesColor(2049, 1287, (203, 253, 0)) and pyautogui.pixelMatchesColor(2175, 1316, (202, 252, 0)):
        #print current time and action performed
        print((current_time), ('[LOG] Duel Score'))
        #click pixel 2175,1316,202,252,0
        click_event(2175, 1316, 0.5)

def enemy_turn():
    #check 1985,668,134,34,33
    if pyautogui.pixelMatchesColor(1985, 668, (134, 34, 33)):
        #log enemy turn
        print((current_time), ('[LOG] Enemy Turn'))
        #check not 444,1169,68,253,251
        if pyautogui.pixelMatchesColor(444, 1169, (68, 253, 251)):
            #log player effect
            print((current_time), ('[LOG] Player Effect'))
            #check 81,63,33,190,251 and click the pixel
            return False
        else:
            return True
    else:
        return True

def surrender():
    if pyautogui.pixelMatchesColor(81, 63, (33, 190, 251)):
        #print current time and action performed
        print((current_time), ('[LOG] Menu Open'))
        #click pixel 81,63,33,190,251
        click_event(81, 63, 0.5)
        #check 355,1274,155,0,0 and click the pixel
        if pyautogui.pixelMatchesColor(355, 1274, (155, 0, 0)):
            #print current time and action performed
            print((current_time), ('[LOG] Surrender'))
            #click pixel 355,1274,155,0,0
            click_event(355, 1274, 0.5)
            #check 1326,836,203,255,0 and 1500,870,199,250,0 clcik second pixel
            if pyautogui.pixelMatchesColor(1326, 836, (203, 255, 0)) and pyautogui.pixelMatchesColor(1500, 870, (199, 250, 0)):
                #log surrender confirm
                print((current_time), ('[LOG] Surrender Confirm'))
                #click pixel 1500,870,199,250,0
                click_event(1500, 870, 0.5)

def error():
    #check 1079,842,203,255,0 and 1286,869,203,255,0 then click second pixel
    if pyautogui.pixelMatchesColor(1079, 842, (203, 255, 0)) and pyautogui.pixelMatchesColor(1286, 869, (203, 255, 0)):
        #print current time and action performed
        print((current_time), ('[LOG] Error'))
        #click pixel 1286,869,203,255,0
        click_event(1286, 869, 0.5)
        start_match()

def card_select():
    #check 1653,883,59,159,247 and 1257,1075,201,156,26 then click 2nd pixel
    if pyautogui.pixelMatchesColor(1653, 883, (59, 159, 247)) and pyautogui.pixelMatchesColor(1257, 1075, (201, 156, 26)):
        #print current time and action performed
        print((current_time), ('[LOG] Card Select'))
        #click pixel 1257,1075,201,156,26
        click_event(1257, 1075, 0.5)
        #check 1118,1336,203,253,0 and 1276,1361,203,253,0 then click 2nd pixel
        if pyautogui.pixelMatchesColor(1118, 1336, (203, 253, 0)) and pyautogui.pixelMatchesColor(1276, 1361, (203, 253, 0)):
            print((current_time), ('[LOG] Card Selected'))
            #click 2nd pixel
            click_event(1276, 1361, 0.5)

def choose_level():
    #checkl 1928,272,59,159,247 and 706,511,178,221,0 then click 2nd pixel
    if pyautogui.pixelMatchesColor(1928, 272, (59, 159, 247)) and pyautogui.pixelMatchesColor(706, 511, (178, 221, 0)):
        #print current time and action performed
        print((current_time), ('[LOG] Choose Level'))
        #click pixel 706,511,178,221,0
        click_event(706, 511, 0.5)
        #check 1075,1014,203,253,0 and 1286,1034,203,253,0 then click 2nd pixel
        if pyautogui.pixelMatchesColor(1075, 1014, (203, 253, 0)) and pyautogui.pixelMatchesColor(1286, 1034, (203, 253, 0)):
            #print current time and action performed
            print((current_time), ('[LOG] Level Selected'))
            #click 2nd pixel
            click_event(1286, 1034, 0.5)

def set_card():
    try:
        #locate 'card.png' on screen
        x,y = pyautogui.locateCenterOnScreen('card.png', confidence=0.9)
        if (y > 1100) and (1900 > x > 670):
            #log card selected
            print((current_time), ('[LOG] Card Selected'))
            #click x,y pixel
            click_event(x, y, 0.5)
    except:
        player_turn()
    #repeat try except for 'set.png' and 'yellow.png'
    try:
        x2,y2 = pyautogui.locateCenterOnScreen('set.png', confidence=0.9)
        print((current_time), ('[LOG] Set Card'))
        click_event(x2, y2, 0.5)
    except:
        player_turn()
    try:
        x3,y3 = pyautogui.locateCenterOnScreen('yellow.png', confidence=0.9)
        if (y > 670) and (1900 > x > 670):
            print((current_time), ('[LOG] Yellow Card'))
            click_event(x3, y3, 0.5)
    except:
        player_turn()

def check_set():
    try:
        x3,y3 = pyautogui.locateCenterOnScreen('card.png', confidence=0.9)
        #check if face down card is below y = 670
        if y3 > 670:
            card_set = True
        else:
            card_set = False
    except:
        card_set = False
    return card_set

def exit():
    #locate exit.png on screen and click it
    try:
        x,y = pyautogui.locateCenterOnScreen('exit.png', confidence=0.5)
        click_event(x, y, 0.5)
    except:
        pass


while keyboard.is_pressed('q') == False:
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    #exit()
    start_match()
    error()
    coin_flip()
    discard()
    player_turn()
    #if check_set == True:
    #    player_turn()
    #else:
    #    set_card()
    card_select()
    discard()
    choose_level()
    game_end()
    duel_pass()
    duel_score()
    #if not enemy_turn():
    #    time.sleep(1)
    #    if not enemy_turn():
    #        surrender()
    #    else:
    #        continue
    