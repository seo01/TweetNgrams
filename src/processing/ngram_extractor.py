


class NgramExtractor():
    
    def extract(self,tokens,n):
        ngrams = []
        for i in range(len(tokens)-n+1):
            ngram = tokens[i:i+n]
            ngrams.append(ngram)
        return ngrams