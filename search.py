

class FSANode(object):
    def __init__(self, value=None, finished=False):
        self.value = value
        self.finished = finished
        self.move = {}   # Dict of Nodes to move to according to the input
        self.edit_distance = 0


class FSA(object):
    def __init__(self, pattern):
        self.head = None
        self.patterns = []
        self.pattern = pattern
        self.layout = {}

        self.parse_pattern()

    def parse_patterns(self):
        raise NotImplemented

    def parse_pattern(self, pattern=None):
        if pattern:
            print('overriding pattern: old: {} new: {}'.format(self.pattern, pattern))
            self.pattern = pattern

        self.head = FSANode()
        current_node = self.head
        for i in self.pattern:
            # version 1: iterative string
            next_node = FSANode(value=i)
            current_node.move[i] = next_node
            current_node = next_node
            print('current_node {}'.format(current_node.value))

        current_node.finished = True

        compressed_pattern = self.compression_algo(self.pattern)
        print("Compressed pattern: ", compressed_pattern)

    def path(self):
        current_node = self.head
        # visited = {}
        path = ''
        while not current_node.finished:
            for i in current_node.move:
                path += '->' + i
                current_node = current_node.move[i]
        print(path)
        return path

    def search(self, sequence):
        current_node = self.head
        for i, val in enumerate(sequence):
            if current_node.finished:
                print("Found pattern '{}'  @ {} in sequence '{}'".format(self.pattern, i, sequence[:i]))
                return True
            # Check for invalid paths
            if val in current_node.move:
                print('i: {} val: {}'.format(i, val))
                current_node = current_node.move[val]
            else:
                current_node = self.head
        return False

    def compression_algo(self, pattern):
        """
            Given a pattern, this method will return a compressed version of the the pattern
        :param pattern:
        :return: compression version of the pattern
        """
        print(pattern)
        compressed_pattern = '' #pattern

        # First generate the compression
        # Iterate until compression generation converges
        # Based on the compression update the FSA.move
        #
        # TODO: Update the FSA.move var

        count = 1
        for i in range(0, len(pattern)-1):
            if pattern[i] == pattern[i+1]:
                count += 1
            else:
                compressed_pattern += pattern[i] + str(count)
                count = 1

        compressed_pattern += pattern[-1] + str(count)

        print(compressed_pattern)

        return compressed_pattern

    def generate_FSA(self, pattern):
        """
            Given a pattern, generate the FSA in compressed string format
        :param pattern:
        :return:
        """
        raise NotImplementedError


if __name__ == '__main__':
    sequence = 'Does this string contain the string test?'
    subsequence = 'test'
    fsa = FSA(pattern=subsequence)
    fsa.path()
    fsa.search(sequence)
