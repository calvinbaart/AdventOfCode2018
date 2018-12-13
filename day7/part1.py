from ..shared.core import readFile
import re

class DependencyNode:
    def __init__(self, key):
        self.key = key
        self.parents = []
        self.children = []

    def dependOn(self, node):
        self.parents.append(node)
        node.children.append(self)

    def __repr__(self):
        return f"DependencyNode[{self.key}]"

class DependencyGraph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, node: str, depends_on: str):
        if node not in self.nodes:
            self.nodes[node] = DependencyNode(node)

        if depends_on not in self.nodes:
            self.nodes[depends_on] = DependencyNode(depends_on)

        self.nodes[node].dependOn(self.nodes[depends_on])

    def resolve(self):
        openList = []
        closedList = []

        for x in self.nodes:
            openList.append(self.nodes[x])
        
        while True:
            currentList = [x for x in openList if len([y for y in x.parents if y not in closedList]) == 0]
            currentList.sort(key=lambda x: x.key, reverse = True)

            if len(currentList) == 0:
                break
            
            current = currentList.pop()
            openList.remove(current)
            closedList.append(current)

            for x in current.children:
                if x in openList:
                    continue
                
                openList.append(x)

        return "".join([x.key for x in closedList])


if __name__ == "__main__":
    regex = r"Step\s(.*?)\s.*step\s(.*?)\s.*"
    input = readFile("./input.txt", __file__)
    input = [re.findall(regex, x, re.IGNORECASE)[0] for x in input]
    
    graph = DependencyGraph()
    
    for x in input:
        graph.addNode(x[1], x[0])

    order = graph.resolve()
    print(order)
