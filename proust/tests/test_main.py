import os
import sys
import unittest

initpy =  os.path.sep.join(__file__.split(os.path.sep)[:-2] + ['__init__.py'])
suitepy =  os.path.sep.join(__file__.split(os.path.sep)[:-1] + ['testsuite.py'])

class MainTest(unittest.TestCase):
        
    def test_benchmark(self):
        command = '%s %s %s bench1' % (sys.executable, initpy, suitepy)
        out = os.popen(command).read()
        self.assertEqual(out, """The result""")
        

if __name__ == '__main__':
    unittest.main()
    
