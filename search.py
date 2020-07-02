

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
        self.head = FSA_Node()
        self.head.move[]
        for i in self.pattern[]:
            # use trie and matrix to generate the data
            pass

    def search(self, sequence):
        current_node = self.head
        for i in sequence:
            if current_node.finished:
                print('Found pattern {} in sequence {}'.format(self.pattern, sequence))
                return
            if i in current_node.move:
                current_node = current_node.move[i]
        return


if __name__ == '__main__':
    sequence = 'Does this string contain the string test?'
    subsequence = 'test'
    fsa = FSA(pattern=subsequence)
    fsa.search(sequence)
