import random

class TwitterNgram():
    
    NGRAMS = {}
    ALL_TWEETS = []
    
    def buildAndGenerateTeets(self, count, n):
        tweets = self.getTweets()
        self.ALL_TWEETS.extend(tweets)
        self.buildNgrams(tweets,n)
        #print self.NGRAMS
        for i in range(count):
            print self.generateTweet(n)
            print "\n"
    
    def getTweets(self):
        f = open("/Users/simon/Documents/git/TweetNgrams/data/tweets.txt") 
        lines = f.readlines()
        f.close()
        new_lines = []
        for line in lines:
            if len(line) > 5:
                new_lines.append(line)
        return new_lines
    
    def buildNgrams(self,tweets,n):
        for tweet in tweets:
            ngrams = self.extractNgrams(tweet,n)
            for ngram in ngrams:
                self.add_ngrams(ngram,self.NGRAMS)
                
    def add_ngrams(self,ngram,ngrams):
        if len(ngram) == 1:
            ngrams[ngram[0]] = ngrams.get(ngram[0],0)+1
        else:
            if ngram[0] not in ngrams:
                ngrams[ngram[0]] = {}
            self.add_ngrams(ngram[1:],ngrams[ngram[0]])
    
    def extractNgrams(self,tweet,n):
        ngrams = []
        #split the tweet into words and filter crap
        words = tweet.split()
        #add pseudo tokens
        new_words = ['^']
        new_words.extend(words)
        new_words.append('$')
        words = new_words
        for i in range(len(words)-n+1):
            ngram = words[i:i+n]
            ngrams.append(ngram)
        return ngrams
    
    def generateTweet(self,n):
        words = self.generateWordList(n)
        tweet = " ".join(words)
        if self.is_unique(tweet):
            return tweet
        else:
            return self.generateTweet()
            
    def is_unique(self,tweet):
        return tweet not in self.ALL_TWEETS
    
    def generateWordList(self,n):
        words = ['^']
        while True:
            l = min(n-1,len(words))
            nwords = words[l*-1:]
            word = self.getNextWord(nwords)
            words.append(word)
            if word == '$':
                break
        return words[1:-1]
        
    
    def getNextWord(self, words):
        frequencies = self.getWordsAndFrequencies(words)
        #print frequencies
        total = sum(frequencies.values())
        index = random.randint(0,total)
        cumulative = 0
        #print words
        #print self.NGRAMS
        for (word,frequency) in frequencies.iteritems():
            cumulative = cumulative + frequency
            if cumulative > index:
                #print word
                return word
        #if you get here drop a word
        return self.getNextWord(words[1:])
        #print "ERROR"
        #raise Exception("Poo")
    
    def getWordsAndFrequencies(self, words):
        #navigate ngrams
        #print words
        tree = self.NGRAMS
        for word in words:
            if word in tree:
                tree = tree[word]
            else:
                return {}
            
        
        #colapse tree
        colapsed_tree = {}
        for word in tree.keys():
            colapsed_tree[word] = self.colapseTree(tree[word])
        return colapsed_tree
    
    def colapseTree(self,tree):
        if isinstance(tree, dict):
            return sum([self.colapseTree(x) for x in tree.values()])
        else:
            return tree
def main():
    twitterNgram = TwitterNgram()
    twitterNgram.buildAndGenerateTeets(10,3)
        
if __name__ == '__main__':
    main()