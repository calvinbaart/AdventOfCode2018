from ..shared.core import readFile

def process(input):
    num_children = input.pop()
    num_metadata = input.pop()
    metadata = []

    for _ in range(0, num_children):
        metadata = metadata + process(input)

    for x in range(0, num_metadata):
        metadata.append(input.pop())

    return metadata

if __name__ == "__main__":
    input = readFile("./input.txt", __file__)[0]
    input = [int(x) for x in input.split(" ")]
    input.reverse()

    print(sum(process(input)))
