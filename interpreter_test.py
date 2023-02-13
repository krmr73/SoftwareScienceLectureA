import unittest
from interpreter import *

def tAdd(a, b):
    return BinExpr('+', a, b)
def tSub(a,b):
    return BinExpr('-', a, b)
def tMul(a,b):
    return BinExpr('*', a, b)
def tDiv(a,b):
    return BinExpr('/', a, b)
def tInt(value):
    return Int(value)

class TestArithmeticOperations(unittest.TestCase):
    def test_add1(self):
        e = tAdd(tInt(1), tInt(1))
        self.assertEqual(e.evaluate(), 2)
        
    def test_add2(self):
        e = tAdd(tInt(2), tInt(3))
        self.assertEqual(e.evaluate(), 5)
        
    def test_sub1(self):
        e = tSub(tInt(1), tInt(1))
        self.assertEqual(e.evaluate(), 0)

    def test_sub2(self):
        e = tSub(tInt(1),tInt(2))
        self.assertEqual(e.evaluate(), -1)
        
    def test_mul1(self):
        e = tMul(tInt(1), tInt(1))
        self.assertEqual(e.evaluate(), 1)

    def test_mul2(self):
        e = tMul(tInt(2),tInt(2))
        self.assertEqual(e.evaluate(), 4)
        
    def test_mul3(self):
        e = tMul(tInt(2),tInt(0))
        self.assertEqual(e.evaluate(), 0)
        
    def test_div1(self):
        e = tDiv(tInt(0), tInt(1))
        self.assertEqual(e.evaluate(), 0)

    def test_div2(self):
        e = tDiv(tInt(2),tInt(1))
        self.assertEqual(e.evaluate(), 2)
        
    def test_div3(self):
        e = tDiv(tInt(6),tInt(2))
        self.assertEqual(e.evaluate(), 3)

if __name__ == '__main__':
    unittest.main()