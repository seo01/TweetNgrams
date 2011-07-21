import unittest
from processing.ngram_tree_processor import *

class TokensToTreeTest(unittest.TestCase):
    def runTest(self):
        ngram_tree_processor = NgramTreeProcessor()
        tree = ngram_tree_processor.tokens_to_tree(["don't","be","evil"])
        #print tree
        self.assertEqual(tree,{"don't":{"be":{"evil":{'#':1},'#':1},'#':1},'#':1})

class CombineTreeTest(unittest.TestCase):
    def runTest(self):
        ngram_tree_processor = NgramTreeProcessor()
        tree = ngram_tree_processor.combine_trees({"don't":{"be":{"evil":{'#':1},'#':1},'#':1},'#':1},{"don't":{"be":{"eval":{'#':1},'#':1},'#':1},'#':1})
        self.assertEqual(tree,{"don't":{"be":{"evil":{'#':1},'#':2,'eval':{'#':1}},'#':2},'#':2})

if __name__ == "__main__":
    unittest.main()