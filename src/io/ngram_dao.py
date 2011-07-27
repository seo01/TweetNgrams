

class NgramDao():
    
    def __init__(self,model,dampening=500):
        self.model = model
        self.dampening=dampening
    
    def get_frequencies(self,words):
        models = self.get_models(words)
        frequencies = reduce(self.reduce_frequencies,\
                map(self.map_frequencies,models,range(len(models))) \
            )
        return frequencies
        
    def get_models(self, words):
        models = [self.model]
        for i in range(len(words)):
            if words[i] in models[-1]:
                models.append(models[-1][words[i]])
        if self.dampening == None:
            models = [models[-1]]
        return models
    
    def map_frequencies(self, model, factor=1):
        frequencies = {}
        for token,ngrams in model.iteritems():
            if token != '#':
                frequencies[token] = ngrams['#']*self.dampening**factor
        return frequencies
    
    def reduce_frequencies(self, frequencies1, frequencies2):
        for token, frequency in frequencies2.iteritems():
            frequencies1[token] = frequencies1.get(token,0)+frequency
        return frequencies1

        
        