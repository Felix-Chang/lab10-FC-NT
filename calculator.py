#https://github.com/Felix-Chang/lab10-FC-NT
#Partner 1: Felix Chang
#Partner 2: Noah Techoueyres
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError as e:
        print(e)

def hypotenuse(a, b):
    try:
        return math.hypot(a,b)
    except TypeError as e:
        print(e)

def add(a, b): return a + b

def subtract(a, b): return a - b

def mul(a, b): return a * b

def div(a, b): # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError
    return b / a 

def logarithm(a, b): # use math library + raise ValueError
    if a < 0 or b < 0 or a == 1:
        raise ValueError
    return math.log(b, a) 

def exp(a, b): 
    return a ** b
