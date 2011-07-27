import unittest
from nlp.document_builder import *
from io.ngram_dao import NgramDao

class SelectWordTest(unittest.TestCase):
    def runTest(self):
        frequencies = {"x":5,"y":5}
        document_builder = DocumentBuilder(NgramDao(frequencies))
        word = document_builder.select_word(frequencies,random_func=lambda f, t: 3)
        self.assertEqual(word,frequencies.keys()[0])
        word = document_builder.select_word(frequencies,random_func=lambda f, t: 8)
        self.assertEqual(word,frequencies.keys()[1])

#TODO: More tests

if __name__ == "__main__":
    unittest.main()