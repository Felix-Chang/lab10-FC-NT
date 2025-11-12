
#https://github.com/Felix-Chang/lab10-FC-NT
#Partner 1: Felix Cheng
#Partner 2:Noah Techoueyres


import unittest
import calculator

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
    def test_multiply(self):
        assert calculator.mul(1, 2) == 2
        assert calculator.mul(20, 2) == 40
        assert calculator.mul(-6, 2) == -12

    def test_divide(self): # 3 assertions
        assert calculator.div(2, 40) == 20
        assert calculator.div(5,20) == 4
        assert calculator.div(-2,-100) == 50

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
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":

    unittest.main()