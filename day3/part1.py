from ..shared.core import readFile
from ..shared.rectangle import Rectangle

input = readFile("./input_test.txt", __file__)
map = {}
results = [Rectangle.fromLine(x, map) for x in input]
total = len([map[x] for x in map.keys() if map[x] >= 2])

print(total)

