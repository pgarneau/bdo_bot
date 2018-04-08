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
    keyboard.press('esc')
    keyboard.press('esc')
    keyboard.press('r')
    mouse.move(finder.findCoords('warehouse'))
    mouse.leftClick()

def openProcessing():
    mouse.move(finder.findCoords('process'))
    mouse.leftClick()

def chop(coords):
    mouse.move(finder.findCoords('chopping'))
    mouse.leftClick()

    mouse.move(coords)
    mouse.rightClick()

    mouse.move(finder.findCoords('process_start'))
    mouse.leftClick()

def heat(coords):
    mouse.move(finder.findCoords('heating'))
    mouse.leftClick()

    if type(coords) is list:
        for coord in coords:
            mouse.move(coord)
            mouse.rightClick()

    else:
        mouse.move(coords)
        mouse.rightClick()

    mouse.move(finder.findCoords('process_start'))
    mouse.leftClick()