import unittest
from proust.benchmark import Benchmark

class BenchmarkTest(unittest.TestCase):
        
    def test_statement(self):
        # You can benchmark a python statement by passing in a string.
        # This is fast, because you don't have function calling overhead.
        bench1 = Benchmark('10*10', iterations=10000)
        bench1.run()
        
    def test_function(self):
        # For more complex tests you can pass in a function:
        runs = [0]
        def blah():
            runs[0] += 1
            
        bench1 = Benchmark(blah, iterations=10000)
        result = bench1.run()
        
        # Check that the function was wrong approximately the expected
        # amounts of times. Allow for up to two runs "wrong":
        self.assertTrue(abs(runs[0]/30000)-result.count < 2)
        
    def test_keywords(self):
        # You can pass in keywords to the test function, to parameterize the test
        runs = {}
        def blah(foo, bar):
            runs[foo] = bar
            
        bench1 = Benchmark(blah, iterations=1, bestof=1)
        bench1.run(foo=1, bar='A')
        bench1.run(foo=2, bar='B')
        bench1.run(foo=3, bar='C')

        self.assertEqual(runs, {1: 'A', 2: 'B', 3: 'C'} )
        
    def test_bestof(self):
        # Tests are being run multiple times, and the best result is picked.
        # This is tested by setting the duration to 0, because then each run
        # will always be one iteration. This test also makes sure the
        # Benchmark doesn't fail if the test takes longer than the duration.
        runs = [0]
        def blah():
            runs[0] += 1
            
        bench1 = Benchmark(blah, iterations=1, duration=0, bestof=5)
        result = bench1.run()
        
        self.assertEqual(runs[0], 5)
        
    def test_csv(self):
        bench1 = Benchmark('10*10', iterations=10000)
        results = bench1.run(foo=1, bar='A')
        self.assertEqual(results.csv_header(), 'Description,Count,Fastest,Total time,Iterations,foo,bar')
        csv = results.csv_data()
        self.assertTrue(csv.startswith('"10*10"'))
        self.assertTrue(csv.endswith(',10000,1,A'))
        self.assertEqual(len(csv.split(',')), 7)
    

if __name__ == '__main__':
    unittest.main()
    
