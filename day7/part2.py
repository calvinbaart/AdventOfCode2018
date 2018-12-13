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

class DependencyWorker:
    def __init__(self, index):
        self.index = index
        self.time = 0
        self.node = None

    def start(self, node, time):
        self.time = time
        self.node = node

    def step(self):
        self.time = self.time - 1

        if self.time < 0:
            self.time = 0

    def is_working(self):
        return self.time > 0

    def __repr__(self):
        return f"DependencyWorker[{self.index}, is_working={self.is_working()}]"

class DependencyGraph:
    def __init__(self, num_workers):
        self.nodes = {}
        self.workers = []

        for x in range(0, num_workers):
            self.workers.append(DependencyWorker(x))

    def addNode(self, node: str, depends_on: str):
        if node not in self.nodes:
            self.nodes[node] = DependencyNode(node)

        if depends_on not in self.nodes:
            self.nodes[depends_on] = DependencyNode(depends_on)

        self.nodes[node].dependOn(self.nodes[depends_on])

    def resolve(self):
        openList = []
        workingList = []
        closedList = []
        step = 0

        for x in self.nodes:
            openList.append(self.nodes[x])

        while True:
            for worker in self.workers:
                if worker.is_working() == False:
                    continue

                worker.step()

                if worker.is_working() == False:
                    workingList.remove(worker.node)
                    closedList.append(worker.node)

                    for x in worker.node.children:
                        if x in openList or x in workingList or x in closedList:
                            continue

                        openList.append(x)

            workers = [x for x in self.workers if x.is_working() is False]
            step = step + 1

            if len(workers) == 0:
                continue

            currentList = [x for x in openList if len(
                [y for y in x.parents if y not in closedList]) == 0]
            currentList.sort(key=lambda x: x.key, reverse=True)

            if len(currentList) == 0:
                if len([x for x in self.workers if x.is_working() is True]) > 0:
                    continue
                else:
                    break

            for worker in workers:
                if len(currentList) == 0:
                    break
    
                current = currentList.pop()
                openList.remove(current)
                workingList.append(current)

                worker.start(current, (60 + ord(current.key) - ord('A')) + 1)

        return step - 1


if __name__ == "__main__":
    regex = r"Step\s(.*?)\s.*step\s(.*?)\s.*"
    input = readFile("./input.txt", __file__)
    input = [re.findall(regex, x, re.IGNORECASE)[0] for x in input]

    graph = DependencyGraph(5)

    for x in input:
        graph.addNode(x[1], x[0])

    order = graph.resolve()
    print(order)
