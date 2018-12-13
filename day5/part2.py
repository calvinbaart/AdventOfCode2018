from ..shared.core import readFile
from .part1 import process
import re

input = readFile("./input.txt", __file__)[0]
characters = [x for x in set(input.lower())]
subs = [re.compile(x, re.IGNORECASE) for x in characters]

data = [len(process(x.sub("", input))) for x in subs]
data.sort()

print(data[0])
