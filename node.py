# the BDD node class


class node:
    def __init__(self, v: int, i: int, ll: int, h: int) -> None:
        self.v = v  # the variable its concerning about
        self.index = i  # its index in the sequence
        self.low = ll  # index of the low node
        self.high = h  # index of the high node

    def printBDD(self):
        print("The variable is ", self.v)
        print("The index is ", self.index)
        print("The low node is ", self.low)
        print("The high node is ", self.high)
