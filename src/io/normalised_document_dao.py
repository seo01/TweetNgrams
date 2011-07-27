

class NormalisedDocumentDao():
    document_hashes = None
    
    def __init__(self):
        self.document_hashes = set()
    
    def hash_document(self, tokens):
        return hash(frozenset(tokens))
    
    def write_normalised_document(self, tokens):
        h = self.hash_document(tokens)
        self.document_hashes.add(h)
        
    def is_unique(self, tokens):
        return not self.hash_document(tokens) in self.document_hashes