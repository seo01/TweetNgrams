import unittest
from processing.frequency_booster import *

class RemoveStartTokensTest(unittest.TestCase):
    def runTest(self):
        rst = RemoveStartTokens()
        frequencies = {"x":5,"y":5,"^":5}
        frequencies = rst.boost_frequencies(None,frequencies)
        self.assertEqual(False,frequencies["^"])

class ReweightEndTokensForTweetLengthTest(unittest.TestCase):
    def runTest(self):
        retftl = ReweightEndTokensForTweetLength()
        frequencies = {"x":5,"y":5,"$":5}
        frequencies1 = retftl.boost_frequencies([],frequencies)
        self.assertEqual(5,frequencies1['$'])
        frequencies2 = retftl.boost_frequencies([str(x) for x in range(100)],frequencies)
        self.assertEqual(71,frequencies2['$'])

if __name__ == "__main__":
    unittest.main()