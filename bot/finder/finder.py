from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui

def findCoords(target):
    results = []
    pyautogui.screenshot('images/game_screenshot.png')

    gameImage = cv2.imread('images/game_screenshot.png', 0)
    gameImage2 = gameImage.copy()

    if type(target) is list:
        for material in target:
            template = cv2.imread('images/' + material + '.png', 0)

            results.append(find(gameImage2, template))
        
        return results

    else:
        template = cv2.imread('images/' + target + '.png', 0)

        return find(gameImage2, template)

def isProcessing():
    pyautogui.screenshot('images/game_screenshot.png')

    gameImage = cv2.imread('images/game_screenshot.png', 0)
    gameImage2 = gameImage.copy()

    template = cv2.imread('images/progress_bar.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(gameImage2, template, eval('cv2.TM_SQDIFF_NORMED'))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    print(min_val)

    if min_val > 0.11:
        return False
    else:
        return True

def rejectOutliers(data):
    print(data)
    elements = np.array(data)
    mean = np.mean(elements, axis=0)
    sd = np.std(elements, axis=0)

    finalList = [x for x in data if (x >= mean - 1 * sd)]
    finalList = [x for x in finalList if (x <= mean + 1 * sd)]

    return finalList

def findButton(target):
    pyautogui.screenshot('images/game_screenshot.png')

    gameImage = cv2.imread('images/game_screenshot.png', 0)
    gameImage2 = gameImage.copy()

    template = cv2.imread('images/' + target + '.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(gameImage2, template, eval('cv2.TM_CCOEFF_NORMED'))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    print(max_val)

    return [max_loc[0] + w/2, max_loc[1] + h/2]
    

def find(zone, target):
    xResults = []
    yResults = []

    w, h = target.shape[::-1]

    methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        method = eval(meth)

        res = cv2.matchTemplate(zone, target, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        xResults.append(top_left[0])
        yResults.append(top_left[1])

    return [np.mean(rejectOutliers(xResults)) + w/2, np.mean(rejectOutliers(yResults)) + h/2]

def detectionTest():
    img = cv2.imread('images/game_screenshot.png',0)
    img2 = img.copy()
    template = cv2.imread('images/warehouse.png',0)
    w, h = template.shape[::-1]

    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
            print(min_val)
        else:
            top_left = max_loc
            print(max_val)
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.rectangle(img,top_left, bottom_right, 255, 2)

        plt.figure()
        plt.subplot(121),plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img,cmap = 'gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
        plt.show(block=False)

    plt.show()