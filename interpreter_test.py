import unittest
from interpreter import *

class TestArithmeticOperations(unittest.TestCase):
    def test_add1(self):
        e = tAdd(Int(1), Int(1))
        self.assertEqual(e.evaluate({}), 2)
        
    def test_add2(self):
        e = tAdd(Int(2), Int(3))
        self.assertEqual(e.evaluate({}), 5)
        
    def test_sub1(self):
        e = tSub(Int(1), Int(1))
        self.assertEqual(e.evaluate({}), 0)

    def test_sub2(self):
        e = tSub(Int(1),Int(2))
        self.assertEqual(e.evaluate({}), -1)
        
    def test_mul1(self):
        e = tMul(Int(1), Int(1))
        self.assertEqual(e.evaluate({}), 1)

    def test_mul2(self):
        e = tMul(Int(2),Int(2))
        self.assertEqual(e.evaluate({}), 4)
        
    def test_mul3(self):
        e = tMul(Int(2),Int(0))
        self.assertEqual(e.evaluate({}), 0)
        
    def test_div1(self):
        e = tDiv(Int(0), Int(1))
        self.assertEqual(e.evaluate({}), 0)

    def test_div2(self):
        e = tDiv(Int(2),Int(1))
        self.assertEqual(e.evaluate({}), 2)
        
    def test_div3(self):
        e = tDiv(Int(6),Int(2))
        self.assertEqual(e.evaluate({}), 3)
        
class TestComp(unittest.TestCase):
    def test_Lt(self):
        e = tLt(Int(1), Int(2))
        self.assertEqual(e.evaluate({}), True)
        
    def test_Gt(self):
        e = tGt(Int(2), Int(1))
        self.assertEqual(e.evaluate({}), True)
        
    def test_Lte(self):
        e = tLte(Int(1), Int(1))
        self.assertEqual(e.evaluate({}), True)
        
    def test_Gte(self):
        e = tGte(Int(1), Int(1))
        self.assertEqual(e.evaluate({}), True)
        
    def test_Eq(self):
        e = tEq(Int(1), Int(1))
        self.assertEqual(e.evaluate({}), True)
        
    def test_Neq(self):
        e = tNeq(Int(1), Int(2))
        self.assertEqual(e.evaluate({}), True)
        
class TestSeqAssign(unittest.TestCase):
    def test_seq_assign1(self):
        e = Seq(Assignment('a', Int(100)), Ident('a'))
        self.assertEqual(e.evaluate({}), 100)
        
    def test_seq_assign2(self):
        e = Seq(
            Assignment('a', Int(100)),
            Assignment('b', tAdd(Ident('a'), Int(1))),
            Ident('b')
            )
        self.assertEqual(e.evaluate({}), 101)
        

if __name__ == '__main__':
    unittest.main()