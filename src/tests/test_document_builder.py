import unittest
from nlp.document_builder import *

class SelectWordTest(unittest.TestCase):
    def runTest(self):
        document_builder = DocumentBuilder()
        frequencies = {"x":5,"y":5}
        word = document_builder.select_word(frequencies,random_func=lambda f, t: 3)
        self.assertEqual(word,frequencies.keys()[0])
        word = document_builder.select_word(frequencies,random_func=lambda f, t: 8)
        self.assertEqual(word,frequencies.keys()[1])
        

if __name__ == "__main__":
    unittest.main()