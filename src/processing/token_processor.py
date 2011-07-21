


class TokenProcessor():
    
    def pre_process(self,tokens):
        new_tokens = ['^']
        new_tokens.extend(tokens)
        new_tokens.append('$')
        return new_tokens
        
    def post_process(self,tokens):
        return tokens[1:-1]
        
    def get_initial(self):
        return ['^']
    
    def is_end(self,token):
        return token == '$'