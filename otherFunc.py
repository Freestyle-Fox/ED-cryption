import time
import os
import pyautogui
from EncrypterFunctions import *
def initialise():
    print("*************Welcome to the ED Crypter!*************\n")
    print("       ***********************************")
    print("       #                                 #")
    print("       #           Let's Secure          #")
    print("       #      your personal massage      #")
    print("       #                                 #")
    print("       ***********************************")
    print("       \nInitializing the Program...     ")
    openDycripter()
    print("Initialization Complete!\n")

def openDycripter():
    file_location = os.path.abspath(__file__)
    file_location = os.path.dirname(file_location)
    pyautogui.hotkey('ctrl', 'shift', 'n')
    time.sleep(1.5)   
    pyautogui.typewrite("cls")  
    pyautogui.press("enter")
    pyautogui.typewrite('python '+'"'+file_location +'\DecrypterFunctions.py"')
    pyautogui.press('enter')