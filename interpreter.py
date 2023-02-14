# 式
class Expr:
    def __init__(self, type) -> None:
        self.type = type

# プログラム
class Program:
    def __init__(self, functions, *bodies) -> None:
        self.type = "Program"
        self.functions = functions
        self.bodies = bodies
    def evaluateProgram(self):    
        env = {}
        for f in self.functions:
            env[f.name] = f
        for body in self.bodies:
            result = body.evaluate(env)
        return result

# 関数定義
class Func:
    def __init__(self, name, params, body) -> None:
        self.type = "Func"
        self.name = name
        self.params = params
        self.body = body
        
# 関数呼び出し
class Call(Expr):
    def __init__(self, name, *args) -> None:
        super().__init__("Call")
        self.name = name
        self.args = args
    def evaluate(self, env):
        func = env[self.name]
        args = [arg.evaluate(env) for arg in self.args]
        newEnv = env
        for i, arg in enumerate(args):
            newEnv[func.params[i]] = arg
        return func.body.evaluate(newEnv)

# 二項表現    
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
            case 'and' | 'or':
                return self.evaluateBoolExpr(env)

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
    # ブール演算
    def evaluateBoolExpr(self, env):
        match self.op:
            case 'and':  return self.lhs.evaluate(env) and self.rhs.evaluate(env)
            case 'or':  return self.lhs.evaluate(env) or self.rhs.evaluate(env)
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
        for body in self.bodies:
            result = body.evaluate(env)
        return result
    
# if文
class If(Expr):
    def __init__(self, condition, thenClause, elseClause) -> None:
        super().__init__("If")
        self.condition = condition
        self.thenClause = thenClause
        self.elseClaluse = elseClause
    def evaluate(self, env):
        if self.condition.evaluate(env) == True:
            return self.thenClause.evaluate(env)
        else:
            return self.elseClaluse.evaluate(env)

# while文
class While(Expr):
    def __init__(self, condition, *bodies) -> None:
        super().__init__("While")
        self.condition = condition
        self.bodies = bodies
    def evaluate(self, env):
        while self.condition.evaluate(env) == True:
            for body in self.bodies:
                body.evaluate(env)

# For文
class For(Expr):
    def __init__(self, default, condition, update, *bodies) -> None:
        super().__init__("For")
        self.default = default
        self.condition = condition
        self.update = update
        self.bodies = bodies
    def evaluate(self, env):
        self.default.evaluate(env)
        while self.condition.evaluate(env) == True:
            for body in self.bodies:
                body.evaluate(env)
            self.update.evaluate(env)

# 出力            
class Print(Expr):
    def __init__(self, *bodies) -> None:
        super().__init__("Print")
        self.bodies = bodies
    def evaluate(self, env):
        for body in self.bodies:
            print(body.evaluate(env))
