import unittest
from nlp.model_builder import *

class ExtractNgramTreeFromDocumentsTest(unittest.TestCase):
    def runTest(self):
        documents = ["how much wood would a woodchuck chuck if a wood chuck could chuck wood", "a woodchuck would chuck so much wood he wouldnt know how much wood he chucked"]
        model_builder = ModelBuilder()
        ngram_tree = model_builder.extract_ngram_tree_from_documents(documents,2)
        self.assertEqual({'a': {'#': 3, 'wood': {'#': 1}, 'woodchuck': {'#': 2}}, '#': 27, 'wouldnt': {'#': 1, 'know': {'#': 1}}, 'would': {'a': {'#': 1}, '#': 2, 'chuck': {'#': 1}}, 'much': {'#': 3, 'wood': {'#': 3}}, 'could': {'#': 1, 'chuck': {'#': 1}}, 'chuck': {'#': 4, 'wood': {'#': 1}, 'so': {'#': 1}, 'could': {'#': 1}, 'if': {'#': 1}}, 'how': {'#': 2, 'much': {'#': 2}}, 'wood': {'#': 4, 'chuck': {'#': 1}, 'would': {'#': 1}, 'he': {'#': 2}}, 'woodchuck': {'#': 2, 'chuck': {'#': 1}, 'would': {'#': 1}}, 'know': {'how': {'#': 1}, '#': 1}, 'so': {'#': 1, 'much': {'#': 1}}, 'if': {'a': {'#': 1}, '#': 1}, 'he': {'#': 2, 'chucked': {'#': 1}, 'wouldnt': {'#': 1}}},ngram_tree)
        

if __name__ == "__main__":
    unittest.main()