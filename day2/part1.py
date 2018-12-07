from ..shared.core import readFile
import collections

input = readFile("./input.txt", __file__)
results = [collections.Counter(x) for x in input];
twoCounter = 0;
threeCounter = 0;

for x in results:
    two = False;
    three = False;

    for key in x:
        value = x[key];

        if value is 2:
            two = True;
        elif value is 3:
            three = True;

        if two and three:
            break;
    
    if two:
        twoCounter += 1;
    
    if three:
        threeCounter += 1;

print(twoCounter * threeCounter);

