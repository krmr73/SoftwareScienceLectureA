# 抽象構文木
class Expr:
    def __init__(self, type) -> None:
        self.type = type

class BinExpr(Expr):
    def __init__(self, op, lhs, rhs) -> None:
        super().__init__("BinExpr")
        self.op = op
        self.lhs = lhs
        self.rhs = rhs
        
    def evaluate(self):
        match self.op:
            case '+' | '-' | '*' | '/':
                return self.evaluateMathExpr()
            case '<' | '>' | '<=' | '>=' | '==' | '!=':
                return self.evaluateCompExpr()
            
    def evaluateMathExpr(self):
        match self.op:
            case '+': return self.lhs.evaluate() + self.rhs.evaluate()
            case '-': return self.lhs.evaluate() - self.rhs.evaluate()
            case '*': return self.lhs.evaluate() * self.rhs.evaluate()
            case '/': return self.lhs.evaluate() / self.rhs.evaluate()
            
    def evaluateCompExpr(self):
        match self.op:
            case '<':   return self.lhs.evaluate() < self.rhs.evaluate()
            case '>':   return self.lhs.evaluate() > self.rhs.evaluate()
            case '<=':  return self.lhs.evaluate() <= self.rhs.evaluate()
            case '>=':  return self.lhs.evaluate() >= self.rhs.evaluate()
            case '==':  return self.lhs.evaluate() == self.rhs.evaluate()
            case '!=':  return self.lhs.evaluate() != self.rhs.evaluate()
        

class Int(Expr):
    def __init__(self, value) -> None:
        super().__init__("Int")
        self.value = value
    def evaluate(self):
        return self.value

# 変数代入
class Assignment(Expr):
    def __init__(self, name, expression) -> None:
        super().__init__("Assignment")
        self.name = name
        self.expression = expression
  
# 変数参照      
class Ident(Expr):
    def __init__(self, name) -> None:
        super().__init__("Ident")
        self.name = name
    
# 連接    
class Seq(Expr):
    def __init__(self, bodies) -> None:
        super().__init__("Seq")
        self.bodies = bodies
        
# 補助関数
def tAdd(a, b):
    return BinExpr('+', a, b)
def tSub(a, b):
    return BinExpr('-', a, b)
def tMul(a, b):
    return BinExpr('*', a, b)
def tDiv(a, b):
    return BinExpr('/', a, b)
def tLt(a, b):
    return BinExpr('<', a, b)
def tGt(a, b):
    return BinExpr('>', a, b)
def tLte(a, b):
    return BinExpr('<=', a, b)
def tGte(a, b):
    return BinExpr('>=', a, b)
def tEq(a, b):
    return BinExpr('==', a, b)
def tNeq(a, b):
    return BinExpr('!=', a, b)