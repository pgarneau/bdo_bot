import time

from input import input
from finder import finder

chopping = ['ash', 'ash_plank', 'birch', 'birch_plank', 'cedar', 'cedar_plank', 'fir', 'fir_plank',
            'maple', 'maple_plank', 'acacia', 'acacia_plank', 'white_cedar', 'white_cedar_plank', 'pine', 'pine_plank']
heating = ['iron', ['iron_shard', 'coal'], 'copper', 'tin', 'zinc', ['copper_shard', 'tin_shard'], ['copper_shard', 'zinc_shard'], 'titanium', 'titanium_shard', 'vanadium', 'vanadium_shard']

initTime = 0

priority = ['fir', 'fir_plank', 'birch', 'birch_plank', 'cedar', 'cedar_plank', 'titanium', 'titanium_shard', 'zinc', 'copper', ['copper_shard', 'zinc_shard'],
            'acacia', 'acacia_plank', 'white_cedar', 'white_cedar_plank', 'maple', 'maple_plank', 'pine', 'pine_plank', 'tin', ['copper_shard', 'tin_shard'], 'ash', 'ash_plank', 'iron', ['iron_shard', 'coal']]

def heat(element):
    coords = finder.findCoords(element)
    input.heat(coords)

def chop(element):
    coords = finder.findCoords(element)
    input.chop(coords)

def feedWorkers():
    input.cancelProcessing()
    input.openWarehouse()
    input.store()
    input.feedWorkers()
    input.openProcessing()


def isDone():
    global initTime
    while finder.isProcessing():
        input.keepActive()

        currentTime = time.clock()
        if currentTime - initTime > 7200: #7200
            initTime = currentTime
            feedWorkers()
            return False

        time.sleep(5)

    return True

def process(element):
    if type(element) is list:
        print("PROCESSING: " + element[0] + " AND " + element[1])
    else:
        print("PROCESSING: " + element)

    if element in chopping:
        chop(element)
    else:
        heat(element)

    time.sleep(1)
        
def start():
    global initTime
    initTime = time.clock()
    input.openWarehouse()

    while True:
        index = 0
        while index < len(priority):
            input.openProcessing()

            try:
                process(priority[index])
            except ValueError:
                index += 1
                continue

            if isDone():
                input.openWarehouse()
                input.store()
                index += 1