def calculate_fibonacci(n):
    """
    Berechnet die n-te Fibonacci-Zahl.
    n: nicht-negative ganze Zahl
    Gibt die entsprechende Fibonacci-Zahl zurück.
    """
    if not isinstance(n, int):
        raise TypeError("n muss eine ganze Zahl sein.")
    if n < 0:
        raise ValueError("n muss eine nicht-negative ganze Zahl sein.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
