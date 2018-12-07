import os


def iter_starting_at(start_pos, arr):
    for i in range(start_pos, len(arr)):
        yield arr[i]

def diff(first, second):
    arr = [];

    for x in range(0, len(first)):
        if x > len(second) or first[x] is not second[x]:
            arr.append(first[x]);

    if len(second) > len(first):
        arr.extend(iter_starting_at(len(first), second));

    return arr;


def readFile(fileName, scriptPath):
    dirname = os.path.dirname(scriptPath)
    filename = os.path.join(dirname, fileName)
    with open(filename) as file:
        return [line.rstrip("\n") for line in file];

