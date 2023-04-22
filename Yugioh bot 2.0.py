from typing import Counter
import pyautogui
import keyboard
import time
from termcolor import colored
from datetime import datetime

pyautogui.PAUSE = 1.5

class ImageNotFoundException(Exception):
    pass

def click_event(x, y, t):
    
    pyautogui.click(x, y)
    time.sleep(t)

def log(message, color):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    #log message
    print(colored(f"{current_time} {message}", color))

def in_match():
    #locate player icon.png and if found return true
    try:
        player_icon = pyautogui.locateCenterOnScreen('player_icon.png', confidence=0.7)
        if player_icon == None:
            raise ImageNotFoundException
        #log player_icon.png located in green
        log(f"player_icon.png located at {player_icon}", 'green')
        return True
    except ImageNotFoundException:
        #log player_icon.png not found in red
        log(f"player_icon.png not found", 'red')
        #locate player_icon1.png and if found return true
        try:
            player_icon1 = pyautogui.locateCenterOnScreen('player_icon1.png', confidence=0.7)
            if player_icon1 == None:
                raise ImageNotFoundException
            #log player_icon1.png located in green
            log(f"player_icon1.png located at {player_icon1}", 'green')
            return True
        except ImageNotFoundException:
            #log player_icon1.png not found in red
            log(f"player_icon1.png not found", 'red')
            return False
    
def player_turn():
    #try locating player_main.png and if == none raise ImageNotFoundException then log if found or not
    try:
        player_main = pyautogui.locateCenterOnScreen('player_main.png', confidence=0.7)
        if player_main == None:
            raise ImageNotFoundException
        #log player_main.png located in green
        log(f"player_main.png located at {player_main}", 'green')
        return True
    except ImageNotFoundException:
        #log player_main.png not found in red
        log(f"player_main.png not found", 'red')
        return False

def enemy_turn():
    #try locating enemy_main.png and if == none raise ImageNotFoundException then log if found or not
        try:
            enemy_main = pyautogui.locateCenterOnScreen('enemy_main.png', confidence=0.7)
            if enemy_main == None:
                raise ImageNotFoundException
            #log enemy_main.png located in green
            log(f"enemy_main.png located at {enemy_main}", 'green')
            return True
        except ImageNotFoundException:
            #log enemy_main.png not found in red
            log(f"enemy_main.png not found", 'red')
            return False

def select_confirm():
    #try locating select.png and if == none raise ImageNotFoundException then log if found or not
    try:
        select = pyautogui.locateCenterOnScreen('select.png', confidence=0.7)
        if select == None:
            raise ImageNotFoundException
        #log select.png located in green
        log(f"select.png located at {select}", 'green')
        #click select.png
        click_event(*select, t=.5)
    except ImageNotFoundException:
        #log confirm.png not found in red
        log(f"select.png not found", 'red')
        #locate ok.png and if found click it
        try:
            ok = pyautogui.locateCenterOnScreen('ok.png', confidence=0.7)
            if ok == None:
                raise ImageNotFoundException
            #log ok.png located in green
            log(f"ok.png located at {ok}", 'green')
            #click ok.png
            click_event(*ok, t=.5)
        except ImageNotFoundException:
            #log ok.png not found in red
            log(f"ok.png not found", 'red')

def return_menu():
    #try locating return.png and if == none raise ImageNotFoundException then log if found or not
    try:
        return_menu = pyautogui.locateCenterOnScreen('return.png', confidence=0.7)
        if return_menu == None:
            raise ImageNotFoundException
        #log return.png located in green
        log(f"return.png located at {return_menu}", 'green')
        #click return.png
        click_event(*return_menu, t=.5)
    except ImageNotFoundException:
        #log return.png not found in red
        log(f"return.png not found", 'red')

def start_match():
    #try locating start.png and if == none raise ImageNotFoundException then log if found or not
    try:
        start = pyautogui.locateCenterOnScreen('start.png', confidence=0.7)
        if start == None:
            raise ImageNotFoundException
        #log start.png located in green
        log(f"start.png located at {start}", 'green')
        #click start.png
        click_event(*start, t=.5)
    except ImageNotFoundException:
        #log start.png not found in red
        log(f"start.png not found", 'red')

def coin_flip():
    #try locating first.png and if == none raise ImageNotFoundException then log if found or not
    try:
        first = pyautogui.locateCenterOnScreen('first.png', confidence=0.7)
        if first == None:
            raise ImageNotFoundException
        #log first.png located in green
        log(f"first.png located at {first}", 'green')
        #click first.png
        click_event(*first, t=.5)
    except ImageNotFoundException:
        #log first.png not found in red
        log(f"first.png not found", 'red')

def draw():
    #try locating draw.png and if == none raise ImageNotFoundException then log if found or not
    try:
        draw = pyautogui.locateCenterOnScreen('draw.png', confidence=0.7)
        if draw == None:
            raise ImageNotFoundException
        #log draw.png located in green
        log(f"draw.png located at {draw}", 'green')
        #click draw.png
        click_event(*draw, t=.5)
    except ImageNotFoundException:
        #log draw.png not found in red
        log(f"draw.png not found", 'red')

def phase_skip():
    #locate player_main.png and if found click it
    try:
        main = pyautogui.locateCenterOnScreen('player_main.png', confidence=0.7)
        if main == None:
            raise ImageNotFoundException
        #log player_main.png located in green
        log(f"player_main.png located at {main}", 'green')
        #click player_main.png
        click_event(*main, t=.5)
        #locate end.png and if found click it
        try:
            end = pyautogui.locateCenterOnScreen('end.png', confidence=0.7)
            if end == None:
                raise ImageNotFoundException
            #log end.png located in green
            log(f"end.png located at {end}", 'green')
            #click end.png
            click_event(*end, t=.5)
        except ImageNotFoundException:
            #log end.png not found in red
            log(f"end.png not found", 'red')
    except ImageNotFoundException:
        #log player_main.png not found in red
        log(f"player_main.png not found", 'red')

def discard():
    #try locating discard.png and if == none raise ImageNotFoundException then log if found or not
    try:
        discard = pyautogui.locateCenterOnScreen('discard.png', confidence=0.7)
        if discard == None:
            raise ImageNotFoundException
        #log discard.png located in green
        log(f"discard.png located at {discard}", 'green')
        #locate and click card1.png
        try:
            card1 = pyautogui.locateCenterOnScreen('card1.png', confidence=0.7)
            if card1 == None:
                raise ImageNotFoundException
            #click face down card1.png
            click_event(*card1, t=.5)
            select_confirm()
        except ImageNotFoundException:
            #log card1.png not found in red
            log(f"card1.png not found", 'red')
    except ImageNotFoundException:
        #log discard.png not found in red
        log(f"discard.png not found", 'red')

def select_card():
    #locate select_card.png
    try:
        select_card = pyautogui.locateCenterOnScreen('select_card.png', confidence=0.7)
        if select_card == None:
            raise ImageNotFoundException
        #log select_card.png located in green
        log(f"select_card.png located at {select_card}", 'green')
        #locate and click face down card1.png
        try:
            face_down_card1 = pyautogui.locateCenterOnScreen('face_down_card1.png', confidence=0.7)
            if face_down_card1 == None:
                raise ImageNotFoundException
            #click face down card1.png
            click_event(*face_down_card1, t=.5)
            select_confirm()
        except ImageNotFoundException:
            #log face_down_card1.png not found in red
            log(f"face_down_card1.png not found", 'red')
    except ImageNotFoundException:
        #log select_card.png not found in red
        log(f"select_card.png not found", 'red')

def level_select():
    #locate level.png and if found click it
    try:
        level = pyautogui.locateCenterOnScreen('level.png', confidence=0.7)
        if level == None:
            raise ImageNotFoundException
        #log level.png located in green
        log(f"level.png located at {level}", 'green')
        #click level.png
        click_event(*level, t=.5)
        select_confirm()
    except ImageNotFoundException:
        #log level.png not found in red
        log(f"level.png not found", 'red')

def defeat():
    #locate defeat.png and if found click it
    try:
        defeat = pyautogui.locateCenterOnScreen('defeat.png', confidence=0.7)
        if defeat == None:
            raise ImageNotFoundException
        #log defeat.png located in green
        log(f"defeat.png located at {defeat}", 'green')
        #locate ok.png and if found click it
        select_confirm()
    except ImageNotFoundException:
        #log defeat.png not found in red
        log(f"defeat.png not found", 'red')

def duel_pass():
    #locate duel_pass.png and if found call select confirm
    try:
        duel_pass = pyautogui.locateCenterOnScreen('duel_pass.png', confidence=0.7)
        if duel_pass == None:
            raise ImageNotFoundException
        #log duel_pass.png located in green
        log(f"duel_pass.png located at {duel_pass}", 'green')
        #locate ok.png and if found click it
        select_confirm()
    except ImageNotFoundException:
        #log duel_pass.png not found in red
        log(f"duel_pass.png not found", 'red')

def duel_results():
    #locate duel_results.png and if found call select confirm
    try:
        duel_results = pyautogui.locateCenterOnScreen('duel_results.png', confidence=0.7)
        if duel_results == None:
            raise ImageNotFoundException
        #log duel_results.png located in green
        log(f"duel_results.png located at {duel_results}", 'green')
        #locate ok.png and if found click it
        return_menu()
    except ImageNotFoundException:
        #log duel_results.png not found in red
        log(f"duel_results.png not found", 'red')

def rank_up():
    #locate rank_up.png and if found call select confirm
    try:
        rank_up = pyautogui.locateCenterOnScreen('rank_up.png', confidence=0.7)
        if rank_up == None:
            raise ImageNotFoundException
        #log rank_up.png located in green
        log(f"rank_up.png located at {rank_up}", 'green')
        #locate ok.png and if found click it
        select_confirm()
    except ImageNotFoundException:
        #log rank_up.png not found in red
        log(f"rank_up.png not found", 'red')

while keyboard.is_pressed('q') == False:
    while in_match() == True:
        #log in match and current time in yellow
        log(f"in match", 'yellow')
        coin_flip()
        defeat()
        while player_turn() == True:
            #log player turn and current time in blue
            log(f"player turn", 'blue')
            #draw()
            phase_skip()
            discard()
            time.sleep(0.5)
        while enemy_turn() == True:
            #log enemy turn and current time in purple
            log(f"enemy turn", 'yellow')
            select_card()
            level_select()
            time.sleep(0.5)
            break
    while not in_match():
        start_match()
        duel_pass()
        duel_results()
        rank_up()

