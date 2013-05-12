import gc
from timeit import timeit, default_timer as timer
from types import FunctionType, MethodType

class Result(object):
    def __init__(self, count, fastest, cumul_time, iterations, keywords, description):
        self.count = count
        self.fastest = fastest
        self.cumul_time = cumul_time
        self.iterations = iterations
        self.keywords = keywords
        self.description = description
        
    def csv_data(self):
        description = self.description.replace('"', '\"')
        res = '"%s",%s,%s,%s,%s' % (description, self.count, self.fastest, self.cumul_time, self.iterations)
        keywords = ','.join([str(x) for x in self.keywords.values()])
        if keywords:
            res += ',' + keywords
        return res
    
    def csv_header(self):
        res = 'Description,Count,Fastest,Total time,Iterations'
        keywords = ','.join([str(x) for x in self.keywords])
        if keywords:
            res += ',' + keywords
        return res
    
    def __eq__(self, other):
        if not isinstance(other, Result):
            return NotImplemented
        return self.__dict__ == other.__dict__
        

class Benchmark(object):
     
    def __init__(self, benchmark, description='', duration=0.1, iterations=1, bestof=3, gc=True):
        self.benchmark = benchmark
        self.duration = duration
        self.iterations = iterations
        self.bestof = bestof
        self.gc = True

        if callable(benchmark):
            self.statement = False
            if not description:
                self.description = benchmark.__name__
        else:
            self.statement = True
            if not description:
                self.description = benchmark
            
        
    def _run_once(self, **kw):
        times = []
        cumul_time = 0
        benchmark = self.benchmark
        if not self.gc:
            gc.disable()

        while True:
            # Benchmark
            if self.statement:
                time = timeit(self.benchmark, number=self.iterations)
            else:
                start = timer()
                for x in xrange(self.iterations):
                    benchmark(**kw)
                time = timer() - start

            if cumul_time + time > self.duration:
                break
            cumul_time += time
            times.append(time)
            
        if not self.gc:
            gc.enable()
            
        if times:
            fastest = min(times)
        else:
            fastest = float('NaN')
            
        return Result(len(times), fastest, cumul_time, self.iterations, kw, self.description)
            
    def run(self, **kw):
        results = [self._run_once(**kw) for x in range(self.bestof)]
        best = sorted(results, key=lambda x: x.count)[-1]
        return best
