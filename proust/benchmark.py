import gc
from timeit import Timer, default_timer as timer
from types import FunctionType, MethodType

from proust.result import Result

try:
    xrange = xrange
except NameError:
    xrange = range

try:
    callable = callable
except NameError:
    def callable(obj):
        return any("__call__" in klass.__dict__ for klass in type(obj).__mro__)

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
                time = Timer(self.benchmark).timeit(self.iterations)
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
