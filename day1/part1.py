from ..shared.core import readFile;

input = list(map(int, readFile("./input.txt", __file__)));
print(sum(input));
