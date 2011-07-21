from processing.ngram_extractor import NgramExtractor
from processing.string_processor import StringProcessor
from processing.ngram_tree_processor import NgramTreeProcessor
from processing.ngram_extractor import NgramExtractor
from processing.token_processor import TokenProcessor
from processing.tokenizer import Tokenizer

from io.tweet_iterator import TweetIterator

class ModelBuilder():
    """A class for building ngram language models"""
    
    def __init__(self, tokenizer=None, string_processor=None, token_processor=None, ngram_extractor=None, ngram_processor=None):
        self.tokenizer = tokenizer if tokenizer else Tokenizer()
        self.string_processor = string_processor
        self.token_processor = token_processor
        self.ngram_extractor = ngram_extractor if ngram_extractor else NgramExtractor()
        self.ngram_tree_processor = ngram_processor if ngram_processor else NgramTreeProcessor()
    
    def extract_ngrams_from_document(self,tweet,n):
        """Given a tweet, extracts ngrams"""
        ptweet = self.string_processor.pre_process(tweet) if self.string_processor else tweet
        tokens = self.tokenizer.tokenize(ptweet)
        ptokens = self.token_processor.pre_process(tokens) if self.token_processor else tokens
        #TODO: write the normalized tweet
        ngrams = self.ngram_extractor.extract(ptokens,n)
        return ngrams
    
    def extract_ngram_tree_from_document(self,tweet,n):
        ngrams = self.extract_ngrams_from_document(tweet,n)
        ngram_trees = map(self.ngram_tree_processor.tokens_to_tree,ngrams)
        ngram_tree = reduce(self.ngram_tree_processor.combine_trees,ngram_trees)
        return ngram_tree
    
    def extract_ngram_tree_from_documents(self,document_iterator,n):
        return \
            reduce(self.ngram_tree_processor.combine_trees, \
                map(lambda x: self.extract_ngram_tree_from_document(x,n),document_iterator) \
            )
def construct():
    return ModelBuilder(string_processor=StringProcessor(),token_processor=TokenProcessor())

def main():
    mb = ModelBuilder(string_processor=StringProcessor(),token_processor=TokenProcessor())
    print mb.extract_ngram_tree_from_documents(TweetIterator("/Users/simon/Documents/git/TweetNgrams/data/tweets.txt"),3)

if __name__ == '__main__':
    main()