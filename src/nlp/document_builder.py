import random
from processing.tokenizer import Tokenizer

class DocumentBuilder():
    
    def __init__(self,ngram_dao,normalised_document_dao=None,string_processor = None, tokenizer = None, frequency_booster=None, token_processor=None, default_length=100):
        self.token_processor = token_processor
        self.frequency_booster = frequency_booster
        self.ngram_dao = ngram_dao
        self.tokenizer = tokenizer if tokenizer else Tokenizer()
        self.string_processor = string_processor
        self.normalised_document_dao = normalised_document_dao
        self.default_length = default_length
    
    def build_document(self,n):
        tokens = None
        while not tokens or not self.is_tokens_ok(tokens):
            tokens = self.build_tokens(n)
        if self.token_processor:
            tokens = self.token_processor.post_process(tokens)
        string = self.tokenizer.untokenize(tokens)
        if self.string_processor:
            string = self.string_processor.post_process(string)
        return string
    
    def is_tokens_ok(self,tokens):
        return self.normalised_document_dao.is_unique(tokens) if self.normalised_document_dao else True
    
    def is_finished(self,words):
        return self.token_processor.is_end(words[-1]) if self.token_processor else len(words) >= self.default_length
    
    def build_tokens(self,n):
        words = self.token_processor.get_initial() if self.token_processor else []
        while not self.is_finished(words):
            word = self.get_next_word(words,n)
            if not word:
                break
            words.append(word)
        return words
    
    def get_next_word(self,words,n):
        ngram = words[min(n-1,len(words))*-1:]
        frequencies = self.ngram_dao.get_frequencies(ngram)
        if self.frequency_booster:
            frequencies = self.frequency_booster.boost_frequencies(words,frequencies)
        return self.select_word(frequencies)

    def select_word(self,frequencies,random_func=random.randint):
        total = sum(frequencies.values())
        index = random_func(0,total)
        cumulative = 0
        for (word,frequency) in frequencies.iteritems():
            cumulative = cumulative + frequency
            if cumulative > index:
                return word
        return None