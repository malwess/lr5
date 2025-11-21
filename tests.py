from main import *

def test_sum2():
    assert sum2(15, 8) == 0

def test_true():
    assert True

def test_message():
    assert False, 'тест провален'

def test_pass():
    pass

def test_ss4():
    assert ss4(123) == 1323

def test_polindrom():
    assert polindrom(1221) == True

def test_add_functions():
    assert add_fractions(Fraction(1, 2), Fraction(1, 3)) == Fraction(5, 6)
    assert add_fractions(Fraction(-1, 4), Fraction(1, 4)) == 0

def test_multiply_fractions():
    assert multiply_fractions(Fraction(2, 3), Fraction(3, 4)) == Fraction(1, 2)

