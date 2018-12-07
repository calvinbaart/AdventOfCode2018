from ..shared.core import readFile, diff
import collections

input = readFile("./input.txt", __file__)

for x in input:
    lhs = list(x);

    for y in input:
        if x == y:
            continue
        
        rhs = list(y);
        difference = diff(lhs, rhs);
        if len(difference) == 1:
            string = "".join([x for x in lhs if x != difference[0]]);
            print(string);
            exit();
