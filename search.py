

class FSA_Node(object):
    def __init__(self):
        self.value = None
        self.finished = False
        self.move = {}   # Dict of Nodes to move to according to the input


class FSA(object):
    def __init__(self, pattern):
        self.head = None
        self.pattern = pattern
        self.layout = {}

    def parse_pattern(self, pattern=None):
        if pattern:
            print('overriding pattern: old: {} new: {}'.format(self.pattern, pattern))
            self.pattern = pattern

        for i in self.pattern:
            # use trie and matrix to generate the data
            pass

    def search(self, sequence):
        current_node = self.head
        for i in sequence:

        return


if __name__ == '__main__':
    sequence = 'Does this string contain the string test?'
    subsequence = 'test'
    fsa = FSA(pattern=subsequence)
    fsa.search(sequence)