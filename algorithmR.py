from BDDnode import *


def algorithmR(bdd):
    # given a bdd that is not reduced, reduce its unnecessary nodes.
    # implemented using Algorithm R in The Art of Computer Programming
    # initialization
    avail = 1  # keeps a list of node that should be deleted.
    root = bdd.nodeList[-1]
    if root.id <= 1:
        print("The BDD only has one node, always 0 or always 1")
        return
    zero = bdd.nodeList[0]
    one = bdd.nodeList[1]
    zero.state2 = -1
    one.state2 = -1
    root.state2 = -1
    head = [-1] * (bdd.nVariables + 1)  # variables counts start from 1

    # R1: dfs to mark all state2 of all nodes reachable from root negative
    # and like all node that have the same value together begin with head.
    def R1(s):
        if s == 0:
            return
        p = s
        s = 0
        p.aux = head[p.value]
        head[p.value] = p
        if p.low.state2 >= 0:
            p.low.state2 = -1
            s = p.low
        R1(s)
        if p.high.state2 >= 0:
            p.high.state2 = -1
            s = p.high
        R1(s)
    R1(root)
    # R2 loop over all the values
    zero.state2 = 0
    one.state2 = 0
    for v in range(bdd.nVariables, 0, -1):
        p = head[v]
        s = 0
        # R3 check redundancy in each layer. remove nodes that
        # have the same low and high nodes
        # In the original algorithm, the two otherwise case in R3 is
        # used to link all the node that are not
        # deleted with together, by going through the aux of the node's
        # low field, if two node adjacent have
        # the same low field, then they are link together directly, if not,
        # they are linked through one node's own
        # aux field point the other node's low field, and the other nodes
        # low field points to the other node itself.
        # the two cases use different signs in the aux field, thus R4 can
        # tell which case it is when cleaning it up
        # Also in this way, the nodes are bucket sorted by their low field.
        # Nodes with the same low field are linked
        # together before going to the next different low field.
        while p != -1:  # go over all the nodes that have the same value (on the same layer)
            pPrime = p.aux
            q = p.high
            # q is deleted, q's low field points to the corresponding node not deleted.
            if q.state1 < 0:
                p.high = q.low
            q = p.low
            if q.state1 < 0:
                p.low = q.low
                q = p.low  # set q to be the current p low field
            # low field and high field points to the same node,
            # the current node show be deleted
            if q == p.high:
                p.state1 = -1  # mark as -1 if the node should be deleted
                p.high = avail
                p.aux = 0  # this node has been processed
                p.state2 = 1
                avail = p  # add p to the list of nodes that should be deleted.
            elif q.state2 >= 0:  # nodes with different low field are linked
                p.aux = s
                if p.aux == 0:  # mark the end of the linked nodes.
                    p.state2 = 0
                else:
                    p.state2 = -1
                s = q
                q.state2 = -1
                q.aux = p
            else:  # nodes with the same low field are linked
                p.aux = q.aux.aux
                p.state2 = q.aux.state2
                q.aux.aux = p
                q.aux.state2 = 1
            p = pPrime
        # R4 clean up, this links the different bucket directly together.
        r = s
        rSign = 0
        s = 0
        while rSign >= 0 and r != 0:
            q = r.aux  # go to the next bucket.
            r.state2 = 0
            r.aux = 0
            if s == 0:  # set s if s hasn't been set.
                s = q
            else:
                p.aux = q  # link to next bucket from previous bucket.
                p.state2 = 0
            p = q
            # nodes in the same bucket, they are already linked.
            while p.state2 > 0 and p.aux != 0:
                p = p.aux
            if p.aux == 0:
                rSign = -1
            r = p.aux
        # after R4 all nodes remaining are link through their aux field,
        # staring with s point to the first node.
        # R5, loop on the remaining list
        if s == 0:  # there are no nodes left in the current layer.
            continue

        # R6 & R7 & R8 remove nodes that has the same low and high
        p = s
        q = p
        while p != 0:  # loop on each p
            s = p.low
            # R7: this loop only continues if low are the same,
            # if low is not the same, go the next bucket. this
            # works because in R3, the nodes are already bucket sorted.
            while q != 0 and q.low == s:
                r = q.high
                # if sees a new high field, mark its aux field as negative
                if r.state2 >= 0:
                    r.state2 = -1
                    r.aux = q
                else:
                    # aux field is negative, it has been seen before,
                    # then the current node is the same as one
                    # node before it, remove it.
                    q.low = r.aux
                    q.state1 = -1
                    q.high = avail
                    avail = q
                q = q.aux
            while p != q:  # R8 mark all aux field as 0
                if p.state1 >= 0:
                    p.high.aux = 0
                    p.high.state2 = 1
                p = p.aux

    # R9
    if root.state1 < 0:  # root has been deleted
        root = root.low
    bdd.root = root








