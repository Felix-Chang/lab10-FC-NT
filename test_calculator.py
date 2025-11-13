#https://github.com/Felix-Chang/lab10-FC-NT
#Partner 1: Felix Chang
#Partner 2: Noah Techoueyres


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        assert calculator.add(1, 2) == 3
        assert calculator.add(20, 2) == 22
        assert calculator.add(-6, 2) == -4


    def test_subtract(self): # 3 assertions
        assert calculator.sub(1, 2) == -1
        assert calculator.sub(20, 2) == 18
        assert calculator.sub(-6, 2) == -8

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,4), 8)
        self.assertEqual(mul(0,2), 0)
        self.assertEqual(mul(-2,4), -8)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(1,5), 5)
        self.assertEqual(div(4,2), 0.5)
        self.assertEqual(div(4,-2), -0.5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 20)


    def test_logarithm(self): # 3 assertions
       assert calculator.log(10,10000) == 4
       assert calculator.log(10,100) == 2
       assert calculator.log(10,100000) == 5

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.log(10,-1)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(5,12), 13)
        self.assertEqual(hypotenuse(24,7), 25)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
            square_root(4)
            square_root(100)
    ##########################

# Do not touch this
if __name__ == "__main__":

    unittest.main()