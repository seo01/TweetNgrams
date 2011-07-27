import unittest
from processing.ngram_extractor import *

class ExtractTest(unittest.TestCase):
    def runTest(self):
        ngram_extractor = NgramExtractor()
        ngrams = ngram_extractor.extract(["does","what","it","says","on","the","tin"],3)
        self.assertEqual([['does', 'what', 'it'], ['what', 'it', 'says'], ['it', 'says', 'on'], ['says', 'on', 'the'], ['on', 'the', 'tin'], ['the', 'tin'], ['tin']],ngrams)        

if __name__ == "__main__":
    unittest.main()