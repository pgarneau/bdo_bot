import pyautogui

MOVE_SPEED = 0.5

def rightClick():
    pyautogui.mouseDown(button='right')
    pyautogui.mouseUp(button='right')

def leftClick():
    pyautogui.mouseDown()
    pyautogui.mouseUp()

def move(coords):
    pyautogui.moveTo(coords[0], coords[1], MOVE_SPEED)