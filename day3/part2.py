from ..shared.core import readFile
from ..shared.rectangle import Rectangle

input = readFile("./input.txt", __file__)
results = [Rectangle.fromLine(x) for x in input]

for x in results:
    hit = False
    overlaps = False

    for y in reversed(results):
        if x is y:
            continue

        overlap = x.overlap(y)
        if overlap is not False:
            overlaps = True
            break
    
    if hit:
        break

    if not overlaps:
        print(x)
