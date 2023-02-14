# 式
class Expr:
    def __init__(self, type) -> None:
        self.type = type

class BinExpr(Expr):
    def __init__(self, op, lhs, rhs) -> None:
        super().__init__("BinExpr")
        self.op = op
        self.lhs = lhs
        self.rhs = rhs
        
    def evaluate(self, env):
        match self.op:
            case '+' | '-' | '*' | '/':
                return self.evaluateMathExpr(env)
            case '<' | '>' | '<=' | '>=' | '==' | '!=':
                return self.evaluateCompExpr(env)
    # 四則演算        
    def evaluateMathExpr(self, env):
        match self.op:
            case '+': return self.lhs.evaluate(env) + self.rhs.evaluate(env)
            case '-': return self.lhs.evaluate(env) - self.rhs.evaluate(env)
            case '*': return self.lhs.evaluate(env) * self.rhs.evaluate(env)
            case '/': return self.lhs.evaluate(env) / self.rhs.evaluate(env)
    # 比較        
    def evaluateCompExpr(self, env):
        match self.op:
            case '<':   return self.lhs.evaluate(env) < self.rhs.evaluate(env)
            case '>':   return self.lhs.evaluate(env) > self.rhs.evaluate(env)
            case '<=':  return self.lhs.evaluate(env) <= self.rhs.evaluate(env)
            case '>=':  return self.lhs.evaluate(env) >= self.rhs.evaluate(env)
            case '==':  return self.lhs.evaluate(env) == self.rhs.evaluate(env)
            case '!=':  return self.lhs.evaluate(env) != self.rhs.evaluate(env)
        
# 整数
class Int(Expr):
    def __init__(self, value) -> None:
        super().__init__("Int")
        self.value = value
    def evaluate(self, env):
        return self.value

# 変数代入
class Assignment(Expr):
    def __init__(self, name, expression) -> None:
        super().__init__("Assignment")
        self.name = name
        self.expression = expression
    def evaluate(self, env):
        env[self.name] = self.expression.evaluate(env)
        return env[self.name]
  
# 変数参照      
class Ident(Expr):
    def __init__(self, name) -> None:
        super().__init__("Ident")
        self.name = name
    def evaluate(self, env):
        return env[self.name]
# 連接    
class Seq(Expr):
    def __init__(self, *bodies) -> None:
        super().__init__("Seq")
        self.bodies = bodies
    def evaluate(self, env):
        for b in self.bodies:
            result = b.evaluate(env)
        return result
    

           
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