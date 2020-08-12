import unittest
import search


class SearchTestCase(unittest.TestCase):
    def test_basic_pattern_positive(self):

        sequence = 'Does this string contain the string test?'
        subsequence = 'test'

        fsa = search.FSA(pattern=subsequence)
        fsa.path()
        response = fsa.search(sequence)

        self.assertEqual(response, True)

    def test_basic_pattern_positive_front(self):
        sequence = 'Does this string contain the string test?'
        subsequence = 'Does'

        fsa = search.FSA(pattern=subsequence)
        fsa.path()
        response = fsa.search(sequence)

        self.assertEqual(response, True)

    def test_basic_pattern_negative(self):
        sequence = 'Does this string contain the string test?'
        subsequence = 'water'

        fsa = search.FSA(pattern=subsequence)
        fsa.path()
        response = fsa.search(sequence)

        self.assertEqual(response, False)

    def test_adding_spaces_pattern_positive(self):

        sequence = 'Does this string contain the string test?'
        subsequence = ' contain '

        fsa = search.FSA(pattern=subsequence)
        fsa.path()
        response = fsa.search(sequence)

        self.assertEqual(response, True)



if __name__ == '__main__':
    unittest.main()
