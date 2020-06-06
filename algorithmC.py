def algorithmC(nodes):
    # algorithm C on page 5. input is a sequence of BDD nodes.
    # output is the number of binary vector that makes the function true
    # and the number of 1s in each beads.
    k = len(nodes)
    c = [0] * k
    if k == 1:
        c[0] = nodes[0].id
        return pow(2, nodes[-1].value - 1) * c[-1], [pow(2, nodes[-1].value - 1) * c[-1]]
    c[0] = 0
    c[1] = 1

    for ki in range(2, k):  # step 1
        node = nodes[ki]
        node.id = ki  # change id to be the correct order in the list, so that I can easily track the nodes.
        node_low = node.low
        node_high = node.high
        cl = c[node_low.id]
        ch = c[node_high.id]
        # step 2
        c[ki] = pow(2, (node_low.value - node.value - 1)) * cl + pow(2, (node_high.value - node.value - 1)) * ch
    return pow(2, nodes[-1].value - 1) * c[-1], c
