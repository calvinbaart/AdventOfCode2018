from ..shared.core import readFile

input = list(map(int, readFile("./input.txt", __file__)))
current = 0;
frequencies = {};

while True:
    found = False;

    for x in input:
        current += x;

        if (current in frequencies):
            found = True;
            break;
        
        frequencies[current] = 1;
    
    if found:
        break;

print(current);
