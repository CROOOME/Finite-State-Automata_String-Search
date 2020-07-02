

class FSA_Node(object):
    def __init__(self):
        self.value = None
        self.correct = None     # Node to move if correct sequence is entered
        self.alternative = {}   # Dict of possible moves
        self.start = None       # Starting node to restart the FSA search


class FSA(object):
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    fsa = FSA()