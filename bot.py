import time

import numpy as np
import pyautogui
from PIL import ImageOps
import pyscreenshot as ImageGrab

class cordinates():
    replaybutton = (360,214)
    dinasaur = (149,239)

#Presses button to restart game 
#Using pyautogui
def restartGame():
    pyautogui.click(cordinates.replaybutton)
    pyautogui.keyDown('down')

#Presses space to jump
#Using pyautogui
def press_space():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')

    time.sleep(0.05)

    print('jump')

    time.sleep(0.10)

    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

#Specify the space between dino and obstacle
#Using ImageGrab
def imageGrab():
    box = (
        cordinates.dinasaur[0]+30, cordinates.dinasaur[1],
        cordinates.dinasaur[0]+120, cordinates.dinasaur[1]+2
    )

    image = ImageGrab.grab(box)

    #Changing RGB to grayscale to make processing faster
    grayImage = ImageOps.grayscale(image)
    a = np.array(grayImage.getcolors())

    print(a.sum())
    return a.sum()

restartGame()

while True:

    if imageGrab()!=213:
        press_space()
        time.sleep(0.1)
