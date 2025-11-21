def sum2(x, y):
    return x + y

def ss4(x):
    s = ''
    while x > 0:
        s = str(x % 4) + s
        x = x // 4
    return int(s)

def polindrom(x):
    if str(x)==str(x)[::-1]:
        return True

from fractions import Fraction

def add_fractions(a: Fraction, b: Fraction) -> Fraction:
    return a + b

def multiply_fractions(a: Fraction, b: Fraction) -> Fraction:
    return a * b