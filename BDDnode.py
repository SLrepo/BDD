import math
from graphviz import Digraph


class Node:
    def __init__(self, id, value, low, high):
        self.id = id
        self.value = value
        self.high = high
        self.low = low
        self.state1 = 1  # corresponds to sign of the low field in original algorithm R
        self.state2 = 1  # corresponds to sign of the aux field in original algorithm R
        self.aux = 0


class BDD:
    def __init__(self, truthTable):
        self.nVariables = math.log(len(truthTable), 2)
        assert(self.nVariables % 1.0 == 0.0)
        self.nVariables = int(self.nVariables)
        I0 = Node(0, self.nVariables+1, 0, 0)
        I1 = Node(1, self.nVariables+1, 1, 1)
        v = self.nVariables  # start from the last variable
        self.nodeList = [I0, I1]
        id = 2
        for i in range(pow(2, v-1)):
            newNode = Node(id, v, self.nodeList[int(truthTable[2*i])], self.nodeList[int(truthTable[2*i+1])])
            self.nodeList.append(newNode)
            id += 1
        startingID = 2
        for v in range(self.nVariables-1, 0, -1):  # e.g. number of variables is 3, [2, 1]
            for i in range(pow(2, v-1)):
                newNode = Node(id, v, self.nodeList[startingID+2*i], self.nodeList[startingID+2*i+1])
                self.nodeList.append(newNode)
                id += 1
            startingID += pow(2, v)
        self.root = self.nodeList[-1]

    def plotBDD(self, fileName, view=True):
        dot = Digraph(comment='Binary Decision Diagram')
        p = self.root
        if p.id <= 1:
            dot.node(str(p.id), str(p.id), shape='box', style='filled', color=".7 .3 1.0")
            dot.render(fileName, view=view)
            return
        # plot the two basic nodes, 1 and 0
        for i in range(2):
            n = self.nodeList[i]
            dot.node(str(n.id), str(n.id), shape='box', style='filled', color=".7 .3 1.0")
        h = set()
        self.plotHelper(p, dot, h)
        dot.render(fileName, view=view)

    def plotHelper(self, root, dot, h):
        if root.id <= 1:  # this is the two base nodes
            return
        if root.id not in h:
            dot.node(str(root.id), str(root.value), shape='circle')
            dot.edge(str(root.id), str(root.low.id), label='0', style='dashed')
            dot.edge(str(root.id), str(root.high.id), label='1')
            h.add(root.id)
            self.plotHelper(root.low, dot, h)
            self.plotHelper(root.high, dot, h)
