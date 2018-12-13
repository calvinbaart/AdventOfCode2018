from ..shared.core import readFile
from .guard import Guard, process
import operator

input = readFile("./input.txt", __file__)
processed = [process(x) for x in input]
processed.sort(key=lambda tup: tup[0])

guards = {}
current = None

for x in processed:
    if x[1] is 0:
        if x[2] not in guards:
            current = Guard(x[2])
            guards[x[2]] = current
        else:
            current = guards[x[2]]
    elif x[1] is 1:
        current.wakeup(x[0])
    elif x[1] is 2:
        current.sleep(x[0])

highest = sorted(guards.values(), key=operator.attrgetter(
    "totalSleepTime"), reverse=True)[0]
print(highest.id * highest.regularSleepMinute()[0])
