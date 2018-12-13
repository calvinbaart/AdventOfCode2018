from ..shared.core import readFile
import re

regex1 = r"(?<!_)(.)(?=_\1)"
regex2 = r"_(.)(?=\1)"

def process(data):
    data = ''.join([f"_{x}" if x.isupper() else x for x in data])

    while True:
        matches = re.finditer(regex1, data, re.IGNORECASE | re.MULTILINE)
        length = 2

        matches = list(matches)
        if len(matches) == 0:
            matches = re.finditer(regex2, data, re.IGNORECASE | re.MULTILINE)
            matches = list(matches)
            length = 1

        if len(matches) == 0:
            break

        matches.reverse()

        for match in matches:
            data = data[0: match.span(0)[0]] + data[match.span(0)[1] + length:]
    
    return data.replace("_", "")

if __name__ == "__main__":
    input = readFile("./input.txt", __file__)[0]
    input = process(input)

    print(len(input))
