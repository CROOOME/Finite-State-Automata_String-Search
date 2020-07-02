

class FSA_Node(object):
    def __init__(self):
        self.value = None
        self.finished = False
        self.move = {}   # Dict of Nodes to move to according to the input


class FSA(object):
    def __init__(self, pattern):
        self.head = None
        self.pattern = pattern


if __name__ == '__main__':
    sequence = 'Does this string contain the string test?'
    subsequence = 'test'
    fsa = FSA(pattern=subsequence)
    fsa.search(sequence)