import pyautogui

import coordinates

MOVE_SPEED = 0.5

def init():
    pyautogui.PAUSE = 2

def move(x, y):
    pyautogui.moveTo(x, y, 0.6)

def testMove():
    pyautogui.moveTo(coordinates.TEST[0], coordinates.TEST[1], MOVE_SPEED)

def store():
    # Move to 1st slot in inventory
    # Right click
    # Press f
    # Press space

    # Move to 2nd slot
    # Right click
    # f 
    # space
    print('placeholder')