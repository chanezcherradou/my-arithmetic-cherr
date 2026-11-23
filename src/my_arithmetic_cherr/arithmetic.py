def gcd(a: int, b: int) -> int:
    """Calcule le plus grand commun diviseur de a et b (algorithme d'Euclide)."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
