import unittest
from processing.string_processor import *

class StringProcessorPreProcessTest(unittest.TestCase):
    def runTest(self):
        sp = StringProcessor()
        assert sp.pre_process("test")=="test"

class StringProcessorPostProcessTest(unittest.TestCase):
    def runTest(self):
        sp = StringProcessor()
        assert sp.post_process("test")=="test"

if __name__ == "__main__":
    unittest.main()