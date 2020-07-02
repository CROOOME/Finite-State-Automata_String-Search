

class FSA_Node(object):
    def __init__(self):
        self.value = None
        self.finished = False
        self.move = {}   # Dict of Nodes to move to according to the input


class FSA(object):
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    fsa = FSA()