from my_arithmetic_cherr.arithmetic import gcd


def test_gcd_simple():
    assert gcd(12, 18) == 6


def test_gcd_premiers_entre_eux():
    assert gcd(7, 13) == 1


def test_gcd_avec_zero():
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5


def test_gcd_negatifs():
    assert gcd(-12, 18) == 6


def test_gcd_identiques():
    assert gcd(9, 9) == 9
