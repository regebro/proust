
class Suite(object):
     
    def __init__(self, benchmarks=None):
        if benchmarks is None:
            benchmarks = []
        self.benchmarks = benchmarks
    
    def run(self, **kw):
        return [bench.run(**kw) for bench in self.benchmarks]

