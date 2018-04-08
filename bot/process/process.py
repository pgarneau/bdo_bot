from input import input
from finder import finder

chopping = ['ash', 'ash_plank', 'birch', 'birch_plank', 'cedar', 'cedar_plank', 'fir', 'fir_plank', 'maple', 'maple_plank']
heating = ['iron', ['iron_shard', 'coal'], 'copper', 'tin', 'zinc', ['copper_shard', 'tin_shard'], ['copper_shard', 'zinc_shard']]

priority = ['fir', 'fir_plank', 'birch', 'birch_plank', 'cedar', 'cedar_plank', 'maple', 'maple_plank', 'ash', 'ash_plank',
            'zin', 'tin', 'copper', ['copper_shard', 'zinc_shard'], ['copper_shard', 'tin_shard'], 'iron', ['iron_shard', 'coal']]

def start():
    input.openWarehouse()

    for element in priority:
        input.openProcessing()

        if element in chopping:
            print("PROCESSING: " + element)
            coords = finder.findCoords(element)
            input.chop(coords)

        else:
            print("PROCESSING: " + element)
            coords = finder.findCoords(element)
            input.heat(coords)

        input.openWarehouse()
        input.store()