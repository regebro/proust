import os
import sys
import unittest

initpy =  os.path.sep.join(__file__.split(os.path.sep)[:-2] + ['__init__.py'])
suitepy =  os.path.sep.join(__file__.split(os.path.sep)[:-1] + ['testsuite.py'])

class MainTest(unittest.TestCase):
        
    def test_benchmark(self):
        command = '%s %s %s bench1' % (sys.executable, initpy, suitepy)
        out = os.popen(command).read()
        self.assertTrue(out.startswith('Description,Count,Fastest,Total time,Iterations\n"10*10"'))
        self.assertTrue(out.endswith(',10000\n'))

    def test_suite(self):
        command = '%s %s %s suite1' % (sys.executable, initpy, suitepy)
        out = os.popen(command).read()
        self.assertTrue(out.startswith('Description,Count,Fastest,Total time,Iterations\n"10*10"'))
        lines = out.split('\n')[1:]
        for line in lines:
            if line:
                self.assertTrue(line.endswith(',10000'))
        

if __name__ == '__main__':
    unittest.main()
    
