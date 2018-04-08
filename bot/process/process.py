import time

from input import input
from finder import finder

chopping = ['ash', 'ash_plank', 'birch', 'birch_plank', 'cedar', 'cedar_plank', 'fir', 'fir_plank', 'maple', 'maple_plank']
heating = ['iron', ['iron_shard', 'coal'], 'copper', 'tin', 'zinc', ['copper_shard', 'tin_shard'], ['copper_shard', 'zinc_shard']]

priority = ['fir', 'fir_plank', 'birch', 'birch_plank', 'cedar', 'cedar_plank', 'maple', 'maple_plank', 'ash', 'ash_plank',
            'zinc', 'tin', 'copper', ['copper_shard', 'zinc_shard'], ['copper_shard', 'tin_shard'], 'iron', ['iron_shard', 'coal']]
# priority = ['zinc', 'tin', 'copper', ['copper_shard', 'zinc_shard']]

def heat(element):
    coords = finder.findCoords(element)
    input.heat(coords)

def chop(element):
    coords = finder.findCoords(element)
    input.chop(coords)

def start():
    initTime = time.clock()
    input.openWarehouse()

    while True:
        for element in priority:
            input.openProcessing()

            if element in chopping:
                print("PROCESSING: " + element)
                try:
                    chop(element)
                except ValueError:
                    continue

            else:
                if type(element) is list:
                    print("PROCESSING: " + element[0] + " AND " + element[1])
                else:
                    print("PROCESSING: " + element)
                
                try:
                    heat(element)
                except ValueError:
                    continue
            
            time.sleep(1)
            while (finder.isProcessing()):
                input.keepActive()

                currentTime = time.clock()
                if currentTime - initTime > 10800:
                    initTime = currentTime

                    input.cancelProcessing()
                    input.openWarehouse()
                    input.store()
                    input.feedWorkers()
                    input.openProcessing()

                    if element in chopping:
                        chop(element)
                    else:
                        heat(element)

                time.sleep(5)

            input.openWarehouse()
            input.store()