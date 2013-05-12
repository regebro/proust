
class Platform(object):
     
    def __init__(self, executable):
        self.executable = executable
        self.results = {}
        
    
    def run(self, suite, **kw):
        results = suite.run(**kw)

