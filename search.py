

class FSA_Node(object):
    def __init__(self, value=None, finished=False):
        self.value = value
        self.finished = finished
        self.move = {}   # Dict of Nodes to move to according to the input


class FSA(object):
    def __init__(self, pattern):
        self.head = None
        self.pattern = pattern
        self.layout = {}

        self.parse_pattern()

    def parse_pattern(self, pattern=None):
        if pattern:
            print('overriding pattern: old: {} new: {}'.format(self.pattern, pattern))
            self.pattern = pattern

        self.head = FSA_Node()
        current_node = self.head
        for i in self.pattern:
            # version 1: iterative string
            next_node = FSA_Node(value=i)
            current_node.move[i] = next_node
            current_node = next_node
            print('current_node {}'.format(current_node.value))

        current_node.finished = True

    def path(self):
        current_node = self.head
        # visited = {}
        path = ''
        while not current_node.finished:
            for i in current_node.move:
                path += '->' + i
                print(path)
                current_node = current_node.move[i]
        return path

    def search(self, sequence):
        current_node = self.head
        for i in sequence:
            if current_node.finished:
                print('Found pattern {} in sequence {}'.format(self.pattern, sequence))
                return
            if i in current_node.move:
                current_node = current_node.move[i]
            else:
                current_node = self.head
        return


if __name__ == '__main__':
    sequence = 'Does this string contain the string test?'
    subsequence = 'test'
    fsa = FSA(pattern=subsequence)
    fsa.path()
    fsa.search(sequence)
