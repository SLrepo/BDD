from BDDnode import *
from algorithmR import *
from algorithmC import *


def dfs(root, nodes, N):  # N is the number of variables in the BDD function
    if root.value == N+1:
        if root not in nodes:
            nodes.append(root)
        return
    dfs(root.low, nodes, N)
    dfs(root.high, nodes, N)
    nodes.append(root)


if __name__ == "__main__":
    # define a BDD node sequence.
    truthTable = [False, False, False, True, False, True, True, True]
    # truthTable = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    truthTable = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    # truthTable = [False, True, False, True, False, True, True, True]
    bdd = BDD(truthTable)
    algorithmR(bdd)
    nodes = []
    dfs(bdd.root, nodes, bdd.nVariables)  # put all the valid nodes in a list.

    c, cs = algorithmC(nodes)
    print("The number of vectors that makes f(x) 1 is ", c)
    print("The number of 1s in each node is ", cs)
