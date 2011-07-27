


class NgramExtractor():
    
    def extract(self,tokens,n):
        ngrams = []
        for i in range(len(tokens)):
            ngram = tokens[i:min(i+n,len(tokens))]
            ngrams.append(ngram)
        return ngrams