from algorithmC import algorithmC
from node import node


# define a BDD tree.
nodes = [None] * 9
nodes[0] = node(5, 0, 0, 0)
nodes[0] = node(5, 0, 0, 0)
nodes[1] = node(5, 1, 1, 1)
nodes[2] = node(4, 2, 0, 1)
nodes[3] = node(4, 3, 1, 0)
nodes[4] = node(3, 4, 3, 2)
nodes[5] = node(3, 5, 1, 0)
nodes[6] = node(2, 6, 0, 1)
nodes[7] = node(2, 7, 5, 4)
nodes[8] = node(1, 8, 7, 6)

c, cs = algorithmC(nodes)
print("The number of vectors that makes f(x) 1 is ", c)
print("The number of 1s in each node is ", cs)
