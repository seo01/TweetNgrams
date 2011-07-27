

class TweetIterator():
    
    def __init__(self,path):
        self.path = path
    
    def __iter__(self):
        self.f = open(self.path)
        return self
    
    def next(self):
        line = self.f.readline()
        if not line:
            self.f.close()
            raise StopIteration
        else:
            line = line.strip()
            if not line:
                return self.next()
            else:
                return line

