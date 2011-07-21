import random
from io.ngram_dao import NgramDao
from processing.token_processor import TokenProcessor
from processing.tokenizer import Tokenizer

class DocumentBuilder():
    
    def __init__(self,ngram_dao = None):
        self.token_processor = TokenProcessor()
        self.frequency_booster = None
        self.ngram_dao = ngram_dao
        self.tokenizer = Tokenizer()
        self.string_processor = None
    
    def build_document(self,n):
        tokens = self.build_tokens(n)
        #TODO: check unique
        string = self.tokenizer.untokenize(tokens)
        if self.string_processor:
            string = self.string_process.post_process(string)
        return string
    
    def build_tokens(self,n):
        words = self.token_processor.get_initial()
        while not self.token_processor.is_end(words[-1]):
            ngram = words[min(n-1,len(words))*-1:]
            frequencies = self.ngram_dao.get_frequencies(ngram)
            if self.frequency_booster:
                frequencies = self.frequency_booster.boost_frequencies(words,frequencies)
            word = self.select_word(frequencies)
            if not word:
                break
            words.append(word)
        return words

    def select_word(self,frequencies,random_func=random.randint):
        total = sum(frequencies.values())
        index = random_func(0,total)
        cumulative = 0
        for (word,frequency) in frequencies.iteritems():
            cumulative = cumulative + frequency
            if cumulative > index:
                return word
        return None

from io.tweet_iterator import TweetIterator
from nlp import model_builder

def main():
    mb = model_builder.construct()
    model = mb.extract_ngram_tree_from_documents(TweetIterator("/Users/simon/Documents/git/TweetNgrams/data/tweets.txt"),3)
    document_builder = DocumentBuilder(ngram_dao = NgramDao(model))
    print document_builder.build_document(3)
    

if __name__ == '__main__':
    main()