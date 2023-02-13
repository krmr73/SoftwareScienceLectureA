# 抽象構文木
class Expr:
    def __init__(self, type) -> None:
        self.type = type

class BinExpr(Expr):
    def __init__(self, op, lhs, rhs) -> None:
        self.op = op
        self.lhs = lhs
        self.rhs = rhs
        
    def evaluate(self):
        match self.op:
            case '+': return self.lhs.evaluate() + self.rhs.evaluate()
            case '-': return self.lhs.evaluate() - self.rhs.evaluate()
            case '*': return self.lhs.evaluate() * self.rhs.evaluate()
            case '/': return self.lhs.evaluate() / self.rhs.evaluate()

class Int(Expr):
    def __init__(self, value) -> None:
        self.value = value
    def evaluate(self):
        return self.value

