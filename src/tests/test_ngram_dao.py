import unittest
from io.ngram_dao import *

class GetFrequenciesTest(unittest.TestCase):
    def runTest(self):
        model = {"don't":{"be":{"evil":{'#':1},'#':2,'eval':{'#':1}},'#':2},'#':2,"be":{"evil":{'#':1},'#':2,'eval':{'#':1}},"evil":{'#':1},'#':6,'eval':{'#':1}}
        ngram_dao = NgramDao(model,100)
        frequencies = ngram_dao.get_frequencies(["don't","be"])
        self.assertEqual({'be': 202, 'evil': 10001, 'eval': 10001, "don't": 2},frequencies)
        frequencies = ngram_dao.get_frequencies(["don't"])
        self.assertEqual({'be': 202, 'evil': 1, 'eval': 1, "don't": 2},frequencies)
        

if __name__ == "__main__":
    unittest.main()