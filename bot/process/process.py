import time

from input import input
from finder import finder

chopping = ['ash', 'ash_plank', 'birch', 'birch_plank', 'cedar', 'cedar_plank', 'fir', 'fir_plank', 'maple', 'maple_plank']
heating = ['iron', ['iron_shard', 'coal'], 'copper', 'tin', 'zinc', ['copper_shard', 'tin_shard'], ['copper_shard', 'zinc_shard']]

priority = ['fir', 'fir_plank', 'birch', 'birch_plank', 'cedar', 'cedar_plank', 'maple', 'maple_plank', 'ash', 'ash_plank',
            'zinc', 'tin', 'copper', ['copper_shard', 'zinc_shard'], ['copper_shard', 'tin_shard'], 'iron', ['iron_shard', 'coal']]

def start():
    input.openWarehouse()

    for element in priority:
        input.openProcessing()

        if element in chopping:
            print("PROCESSING: " + element)
            coords = finder.findCoords(element)
            input.chop(coords)

        else:
            if type(element) is list:
                print("PROCESSING: " + element[0] + " AND " + element[1])
            else:
                print("PROCESSING: " + element)
            
            coords = finder.findCoords(element)
            input.heat(coords)

        time.sleep(1)
        while (finder.isProcessing()):
            input.keepActive()
            time.sleep(5)

        input.openWarehouse()
        input.store()