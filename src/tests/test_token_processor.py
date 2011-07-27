import unittest
from processing.token_processor import *

class PreProcessTest(unittest.TestCase):
    def runTest(self):
        token_processor = TokenProcessor()
        tokens = token_processor.pre_process(["hello","word"])
        self.assertEqual(tokens,["^","hello","word","$"])

class PostProcessTest(unittest.TestCase):
    def runTest(self):
        token_processor = TokenProcessor()
        tokens = token_processor.post_process(["^","hello","word","$"])
        self.assertEqual(tokens,["hello","word"])
        

if __name__ == "__main__":
    unittest.main()