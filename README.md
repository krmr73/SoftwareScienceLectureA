# SoftwareScienceLectureA

Pythonで実装された抽象構文木のインタプリタです。

## 仕様
このプログラム言語には以下の機能があります。
- 四則演算
- 比較演算
- ブール演算
- 変数の代入・参照
- 関数定義・呼び出し
- 条件分岐(if)
- 繰り返し(for, while)
- 標準出力

## 数式
数式は以下のように書きます。
```
tAdd(Int(1), Int(2))  // 1 + 2
tSub(Int(1), Int(2))  // 1 - 2
tMul(Int(1), Int(2))  // 1 * 2
tDiv(Int(1), Int(2))  // 1 / 2
```

## 比較式
比較式は以下のように書きます。
```
tLt(Int(1), Int(2))   // 1 < 2
tGt(Int(1), Int(2))   // 1 > 2
tLte(Int(1), Int(2))  // 1 <= 2
tGte(Int(1), Int(2))  // 1 >= 2
tEq(Int(1), Int(2))   // 1 == 2
tNeq(Int(1), Int(2))  // 1 != 2
```

## ブール演算
ブール演算は以下のように書きます。
```
tAnd(Int(1), Int(0))  // 1 and 0
tOr(Int(1), Int(0))   // 1 or 0
```

## 代入式
代入式は以下のように書きます。
```
Assignment('x', Int(1))  // x = 1
```

## 連接式
連接式は以下のように書きます。
```
Seq(Assignment('x', Int(1)), Assignment('y', Int(2)))   // x = 1; y = 2
```

## 条件分岐式
条件分岐式は以下のように書きます。
```
If(tEq(Int(1), Int(2)), Assignment('x', Int(1)), Assignment('x', Int(2)))
// if (1 == 2) { x = 1 } else { x = 2 }
```

## While式
While式は以下のように書きます。
```
While(tLt(Ident('x'), Int(10)), Assignment('x', tAdd(Ident('x'), Int(1))))
// while (x < 10) { x = x + 1 }
```

## For式
For式は以下のように書きます。
```
For(Assignment('x', Int(0)), tLt(Ident('x'), Int(10)), Assignment('x', tAdd(Ident('x'), Int(1))), Assignment('y', tAdd(Ident('y'),Ident('x'))))
// For (x = 0; x < 10; x = x + 1) { y = y + x }
```

## 関数定義
関数定義は以下のように書きます。
```
Program(
  [Func('add', ['x', 'y'], tAdd(Ident('x'), Ident('y')))],
  Call('add', Int(1), Int(2))
)   // function add(x, y) { x + y }; add(1, 2)
```

## 標準出力
標準出力は以下のように書きます。
```
Print(Int(1))   // print(1)
```
