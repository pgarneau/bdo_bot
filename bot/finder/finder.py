from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui

def getGameImage():
    pyautogui.screenshot('images/game_screenshot.png')

    gameImage = cv2.imread('images/game_screenshot.png', 0)
    return gameImage.copy()

def loadAndFind(target, zone, method):
    template = cv2.imread('images/' + target + '.png', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(zone, template, eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    return min_val, max_val, min_loc, max_loc, w, h

def isProcessing():
    gameImage = getGameImage()

    min_val, _, _, _, _, _ = loadAndFind('progress_bar', gameImage, 'cv2.TM_SQDIFF_NORMED')
    # print(min_val)

    if min_val > 0.11:
        return False
    else:
        return True

def findButton(target):
    gameImage = getGameImage()

    for _ in xrange(3):
        _, max_val, _, max_loc, w, h = loadAndFind(target, gameImage, 'cv2.TM_CCOEFF_NORMED')
        # print(max_val)

        if max_val > 0.9:
            return [max_loc[0] + w/2, max_loc[1] + h/2]

    raise ValueError('Could not find button!')

def findCoords(target):
    results = []
    gameImage = getGameImage()

    if type(target) is list:
        for material in target:
            template = cv2.imread('images/' + material + '.png', 0)

            results.append(find(gameImage, template))
        
        return results

    else:
        template = cv2.imread('images/' + target + '.png', 0)

        return find(gameImage, template)

def find(zone, target):
    xResults = []
    yResults = []

    w, h = target.shape[::-1]

    methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for _ in xrange(3):
        for meth in methods:
            method = eval(meth)

            res = cv2.matchTemplate(zone, target, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                if method is cv2.TM_SQDIFF_NORMED:
                    minimum = min_val

                top_left = min_loc
            else:
                top_left = max_loc

            xResults.append(top_left[0])
            yResults.append(top_left[1])
        
        if len(set(xResults)) <= 1 and len(set(yResults)) <= 1:
            print(minimum)
            if minimum < 0.022:
                return [xResults[0] + w/2, yResults[0] + h/2]
    
    raise ValueError('Could not confirm material location')

def detectionTest():
    img = cv2.imread('images/bdo_mats.png',0)
    img2 = img.copy()
    template = cv2.imread('images/maple_plank.png',0)
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

# def rejectOutliers(data):
#     print(data)
#     elements = np.array(data)
#     mean = np.mean(elements, axis=0)
#     sd = np.std(elements, axis=0)

#     finalList = [x for x in data if (x >= mean - 1 * sd)]
#     finalList = [x for x in finalList if (x <= mean + 1 * sd)]

#     return finalList