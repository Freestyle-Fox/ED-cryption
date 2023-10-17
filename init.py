import pygetwindow as gw
import pyautogui
import time
import os
from EncrypterFunctions import *
from otherFunc import *
import random
  
initialise()

while True:
    user_input = input(">> ")
    if user_input == "exit":
        exit()
        break

    func = [encrypter001, encrypter002, encrypter003, encrypter004, encrypter005, encrypter006]
    user_input = func[random.randrange(0,len(func))](user_input)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.typewrite(user_input)
    if len(user_input)>50:
        time.sleep(2)
    elif len(user_input)>20:
        time.sleep(0.3)
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'tab')
    
