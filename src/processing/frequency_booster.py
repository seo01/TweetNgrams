


class FrequencyBooster():
    def __init__(self):
        self.chain = [RemoveStartTokens(),ReweightEndTokensForTweetLength()]
    def boost_frequencies(self,words,frequencies):
        for booster in self.chain:
            frequencies = booster.boost_frequencies(words,frequencies)
        return frequencies
    
class RemoveStartTokens():
    def boost_frequencies(self,words,frequencies):
        frequencies['^'] = 0
        return frequencies

class ReweightEndTokensForTweetLength():
    def boost_frequencies(self,words,frequencies):
        word_length = sum([len(word) for word in words])+len(words)
        total = sum(frequencies.values())
        if word_length > 100:
            frequencies['$']=((word_length-100)*total/40)
        return frequencies
    
    