from node import node


def algorithmC(nodes):
    # algorithm C on page 5. input is a sequence of BDD nodes.
    # output is the number of binary vector that makes the function true
    # and the number of 1s in each beads.
    k = len(nodes)
    c = [0] * k
    c[0] = 0
    c[1] = 1
    for ki in range(2, k):
        node = nodes[ki]
        node_low = nodes[node.low]
        node_high = nodes[node.high]
        cl = c[node.low]
        ch = c[node.high]
        c[ki] = pow(2, (node_low.v - node.v - 1)) * cl + pow(2, (node_high.v - node.v - 1)) * ch
    return c[-1], c
