import time

import pyautogui

import coordinates
import keyboard
import mouse


def init():
    pyautogui.PAUSE = 0.8
    
def getCoords():
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr + '\n')
        time.sleep(0.5)

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
    mouse.move(coordinates.WAREHOUSE)
    mouse.leftClick()

def openProcessing():
    mouse.move(coordinates.PROCESS)
    mouse.leftClick()

def chop(coords):
    mouse.move(coordinates.CHOPPING)
    mouse.leftClick()

    mouse.move(coords)
    mouse.rightClick()

    mouse.move(coordinates.START_PROCESS)
    mouse.leftClick()
    time.sleep(3)
    keyboard.press('space')

def heat(*args):
    mouse.move(coordinates.HEATING)
    mouse.leftClick()

    for coords in args:
        mouse.move(coords)
        mouse.rightClick()

    mouse.move(coordinates.START_PROCESS)
    mouse.leftClick()
    time.sleep(3)
    keyboard.press('space')