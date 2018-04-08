import time

import pyautogui

import coordinates
import keyboard
from finder import finder
import mouse


def init():
    pyautogui.PAUSE = 0.5
    
def getCoords():
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr + '\n')
        time.sleep(0.5)

def keepActive():
    mouse.relativeMove(5, 0)
    mouse.relativeMove(-5, 0)

def store():
    mouse.move(coordinates.INV_SLOT_1)
    mouse.rightClick()
    keyboard.press('f')
    keyboard.press('space')

    mouse.move(coordinates.INV_SLOT_2)
    mouse.rightClick()
    keyboard.press('f')
    keyboard.press('space')

def openWarehouse():
    time.sleep(0.3)
    keyboard.press('r')
    time.sleep(0.2)
    mouse.move(finder.findButton('warehouse'))
    mouse.leftClick()

def openProcessing():
    mouse.move(finder.findButton('process'))
    mouse.leftClick()

def chop(coords):
    mouse.move(finder.findButton('chopping'))
    mouse.leftClick()

    mouse.move(coords)
    mouse.rightClick()

    mouse.move(finder.findButton('process_start'))
    mouse.leftClick()

def heat(coords):
    mouse.move(finder.findButton('heating'))
    mouse.leftClick()

    if type(coords) is list:
        for coord in coords:
            mouse.move(coord)
            mouse.rightClick()

    else:
        mouse.move(coords)
        mouse.rightClick()

    mouse.move(finder.findButton('process_start'))
    mouse.leftClick()