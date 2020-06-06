# this algorithm generate the BDDs of all 256 Boolean functions of three variables
from algorithmR import *
from testC import dfs
from algorithmC import *


# list all possible truth tables of three variables
def permutation(truthTable):
    if len(truthTable) == 8:
        bdd = BDD(truthTable)
        algorithmR(bdd)
        fileName = ""
        for i in range(8):
            fileName += str(int(truthTable[i]))
        bdd.plotBDD('256/'+fileName+'.gv', view=False)
        # test algorithm C at the same time.
        nodes = []
        dfs(bdd.root, nodes, bdd.nVariables)
        c, cs = algorithmC(nodes)
        print("The number of vectors that makes f(x) 1 is ", c)
        print("The number of 1s in each node is ", cs)
        return
    permutation(truthTable + [False])
    permutation(truthTable + [True])


if __name__ == "__main__":
    permutation([])
