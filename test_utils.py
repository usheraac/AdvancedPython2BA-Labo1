# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        # À compléter...
        self.assertEqual(1,utils.fact(0))
        self.assertEqual(6,utils.fact(3))
        with self.assertRaises(ValueError):
            utils.fact(-1)
    
    def test_roots(self):
        # À compléter...
        self.assertEqual(utils.roots(1,4,0),(-1,-3))
        self.asserEqual(utils.roots(0,0,0), (0,0))
        with self.assertRaises(valuerError):
            utils.roots(4,2,1)
        
        
    
    def test_integrate(self):
        # À compléter...
        self.assertEqual(utils.integrate('x',0,10),50)
        self.assertEqual(utils.integrate('x**2 -1 ',-1,1),(-4/3))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
