from ..shared.core import readFile

class Node:
    def __init__(self):
        self.children = []
        self.metadata = []

    def process(self, input):
        num_children = input.pop()
        num_metadata = input.pop()

        for _ in range(0, num_children):
            child = Node()
            child.process(input)

            self.children.append(child)
        
        for _ in range(0, num_metadata):
            self.metadata.append(input.pop())
    
    def value(self):
        if len(self.children) is 0:
            return sum(self.metadata)
        
        value = 0
        for index in self.metadata:
            if index is 0 or index > len(self.children):
                continue

            value = value + self.children[index - 1].value()

        return value

if __name__ == "__main__":
    input = readFile("./input.txt", __file__)[0]
    input = [int(x) for x in input.split(" ")]
    input.reverse()

    root = Node()
    root.process(input)

    print(root.value())
