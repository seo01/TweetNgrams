import unittest
from processing.tokenizer import *

class TokenizeTest(unittest.TestCase):
    def runTest(self):
        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize("hello word")
        self.assertEqual(tokens,["hello","word"])

class UntokenizeTest(unittest.TestCase):
    def runTest(self):
        tokenizer = Tokenizer()
        string = tokenizer.untokenize(["hello","word"])
        self.assertEqual(string,"hello word")
        

if __name__ == "__main__":
    unittest.main()