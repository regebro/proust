# This file contains the benchmarks and suite used by test_main.py

from proust.benchmark import Benchmark
from proust.suite import Suite

bench1 = Benchmark('10*10', iterations=10000)

def benchme():
    x = 10*10
    
bench2 = Benchmark(benchme, iterations=10000)

suite1 = Suite([bench1, bench2])
