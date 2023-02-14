# SoftwareScienceLectureA

Pythonで実装されたトイプログラミング言語です。

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

## 繰り返し式
繰り返し式は以下の二つの書き方ができます。
```
Seq(
  Assignment('x', Int(0)),
  While(tLt(Ident('x'), Int(10)), Assignment('x', tAdd(Ident('x'), Int(1)))),
  Ident('x')
)    // x = 0; while (x < 10) { x = x + 1 }; x
```
```
Program(
    [],
    Assignment('x', Int(0)),
    While(tLt(Ident('x'), Int(10)), Assignment('x', tAdd(Ident('x'), Int(1)))),
    Ident('x')
)   // x = 0; while (x < 10) { x = x + 1 }; x
```

## 関数定義
```
Program(
  [Func('add', ['x', 'y'], tAdd(Ident('x'), Ident('y')))],
  Call('add', Int(1), Int(2))
)   // function add(x, y) { x + y }; add(1, 2)
```
