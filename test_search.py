import unittest
import search


class SearchTestCase(unittest.TestCase):
    def test_basic_pattern(self):

        sequence = 'Does this string contain the string test?'
        subsequence = 'test'

        fsa = search.FSA(pattern=subsequence)
        fsa.path()
        response = fsa.search(sequence)

        self.assertEqual(response, True)


if __name__ == '__main__':
    unittest.main()
