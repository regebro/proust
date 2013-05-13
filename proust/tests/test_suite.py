import unittest
from proust.benchmark import Benchmark
from proust.suite import Suite

class SuiteTest(unittest.TestCase):
        
    def test_suite(self):
        suite = Suite(benchmarks=[Benchmark('10*10', iterations=10000, duration=0.1)])
        suite.benchmarks.append(Benchmark('100*100', iterations=10000, duration=0.1))
        results = suite.run()
        self.assertEqual(len(results), 2)

if __name__ == '__main__':
    unittest.main()
    
