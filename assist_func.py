from interpreter import *

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
def tAnd(a, b):
    return BinExpr('and', a, b)
def tOr(a, b):
    return BinExpr('or', a, b)