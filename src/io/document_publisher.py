

class DocumentPublisher():
    
    def __init__(self):
        pass
    
    def publish(self,document):
        print document
        print "\n"

class FilePublisher():
    
    def __init__(self,fh):
        self.fh = fh
    
    def publish(self,document):
        self.fh.write('%s\n'%document)
