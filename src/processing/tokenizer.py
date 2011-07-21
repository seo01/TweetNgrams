

class Tokenizer():
    
    def tokenize(self,string):
        return string.split()
        
    def untokenize(self,tokens):
        return " ".join(tokens)