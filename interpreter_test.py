import unittest
from interpreter import *

class TestArithmeticOperations(unittest.TestCase):
    # (1 + 1) == 2
    def test_add1(self):
        e = tAdd(Int(1), Int(1))
        self.assertEqual(e.evaluate({}), 2)
    # (2 + 3) == 5    
    def test_add2(self):
        e = tAdd(Int(2), Int(3))
        self.assertEqual(e.evaluate({}), 5)
    # (1 - 1) == 0    
    def test_sub1(self):
        e = tSub(Int(1), Int(1))
        self.assertEqual(e.evaluate({}), 0)
    # (1 - 2) == -1
    def test_sub2(self):
        e = tSub(Int(1),Int(2))
        self.assertEqual(e.evaluate({}), -1)
    # (1 * 1) == 1    
    def test_mul1(self):
        e = tMul(Int(1), Int(1))
        self.assertEqual(e.evaluate({}), 1)
    # (2 * 2) == 4
    def test_mul2(self):
        e = tMul(Int(2),Int(2))
        self.assertEqual(e.evaluate({}), 4)
    # (2 * 0) == 0
    def test_mul3(self):
        e = tMul(Int(2),Int(0))
        self.assertEqual(e.evaluate({}), 0)
    # (0 / 1) == 0    
    def test_div1(self):
        e = tDiv(Int(0), Int(1))
        self.assertEqual(e.evaluate({}), 0)
    # (2 / 1) == 2
    def test_div2(self):
        e = tDiv(Int(2),Int(1))
        self.assertEqual(e.evaluate({}), 2)
    # (6 / 2) == 3
    def test_div3(self):
        e = tDiv(Int(6),Int(2))
        self.assertEqual(e.evaluate({}), 3)
        
class TestComp(unittest.TestCase):
    # (1 < 2) == True
    def test_Lt(self):
        e = tLt(Int(1), Int(2))
        self.assertEqual(e.evaluate({}), True)
    # (2 > 1) == True    
    def test_Gt(self):
        e = tGt(Int(2), Int(1))
        self.assertEqual(e.evaluate({}), True)
    # (1 <= 1) == True    
    def test_Lte(self):
        e = tLte(Int(1), Int(1))
        self.assertEqual(e.evaluate({}), True)
    # (1 >= 1) == True    
    def test_Gte(self):
        e = tGte(Int(1), Int(1))
        self.assertEqual(e.evaluate({}), True)
    # (1 == 1) == True    
    def test_Eq(self):
        e = tEq(Int(1), Int(1))
        self.assertEqual(e.evaluate({}), True)
    # (1 != 2) == True    
    def test_Neq(self):
        e = tNeq(Int(1), Int(2))
        self.assertEqual(e.evaluate({}), True)
        
class TestBool(unittest.TestCase):
    # (1 and 1) == True
    def test_and(self):
        e = tAnd(Int(1), Int(1))
        self.assertEqual(e.evaluate({}), True)
    # (1 or 1) == True
    def test_or(self):
        e = tOr(Int(1), Int(0))
        self.assertEqual(e.evaluate({}), True)
        
class TestSeqAssign(unittest.TestCase):
    # {a = 100; a} == 100
    def test_seq_assign1(self):
        e = Seq(Assignment('a', Int(100)), Ident('a'))
        self.assertEqual(e.evaluate({}), 100)
    # {a = 100; b = a + 1; b} == 101    
    def test_seq_assign2(self):
        e = Seq(
            Assignment('a', Int(100)),
            Assignment('b', tAdd(Ident('a'), Int(1))),
            Ident('b')
            )
        self.assertEqual(e.evaluate({}), 101)
        
class TestIf(unittest.TestCase):
    # (if(1 < 2) 2 else 1) == 2
    def test_if1(self):
        e = If(
            tGt(Int(1), Int(2)),
            Int(2),
            Int(1)       
        )
        self.assertEqual(e.evaluate({}), 1)
    # (if(1 > 2) 2 else 1) == 1
    def test_if2(self):
        e = If(
            tLt(Int(1), Int(2)),
            Int(2),
            Int(1)       
        )
        self.assertEqual(e.evaluate({}), 2)
    """
    {
        a = 100;
        b = 200;
        if(a < b){
            500;
        }else{
            1000;
        }
    }
    """
    def test_if3(self):
        e = Seq(
            Assignment('a', Int(100)),
            Assignment('b', Int(200)),
            If(tLt(Ident('a'), Ident('b')), Int(500), Int(1000))
        )
        self.assertEqual(e.evaluate({}), 500)

class TestWhile(unittest.TestCase):
    """
        i = 0;
        while(i < 10){
            i = i + 1;
        };
        i
    == 10
    """
    def test_while(self):
        program = Program(
            [],
            Assignment('i', Int(0)),
            While(tLt(Ident('i'), Int(10)), Assignment('i', tAdd(Ident('i'), Int(1)))),
            Ident('i')
        )
        self.assertEqual(program.evaluateProgram(), 10)
        
    def test_while2(self):
        e = Seq(
            Assignment('x', Int(0)),
            While(tLt(Ident('x'), Int(10)), Assignment('x', tAdd(Ident('x'), Int(1)))),
            Ident('x')
        ) 
        self.assertEqual(e.evaluate({}), 10)
        
class TestFor(unittest.TestCase):
    """
        sum = 0;
        for(i = 0; i < 10; i = i + 1){
            sum = sum + i;
        };
        sum
    == 45
    """
    def test_for1(self):
        program = Program(
            [],
            Assignment('sum', Int(0)),
            For(Assignment('i', Int(0)), tLt(Ident('i'), Int(10)), Assignment('i', tAdd(Ident('i'), Int(1))), Assignment('sum', tAdd(Ident('sum'),Ident('i')))),
            Ident('sum')
        )
        self.assertEqual(program.evaluateProgram(), 45)
        
    def test_for2(self):
        e = Seq(
            Assignment('sum', Int(0)),
            For(Assignment('i', Int(0)), tLt(Ident('i'), Int(10)), Assignment('i', tAdd(Ident('i'), Int(1))), Assignment('sum', tAdd(Ident('sum'),Ident('i')))),
            Ident('sum')
        )
        self.assertEqual(e.evaluate({}), 45)
    
class TestCall(unittest.TestCase):
    """
        function add(a, b){
            return a + b;
        },
        add(1, 2)
    == 3
    """
    def test_call(self):
        program = Program(
            [Func('add', ['a', 'b'], tAdd(Ident('a'), Ident('b')))],
            Call('add', Int(1), Int(2))
        )
        self.assertEqual(program.evaluateProgram(), 3)

if __name__ == '__main__':
    unittest.main()
    # e = Print(Int(3))
    # e.evaluate({})