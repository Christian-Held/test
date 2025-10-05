def calculate_fibonacci(n):
    """
    Berechnet die n-te Fibonacci-Zahl für n >= 0.
    Fibonacci-Folge: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2) für n>=2
    """
    if not isinstance(n, int):
        raise TypeError("n muss eine ganze Zahl sein.")
    if n < 0:
        raise ValueError("n muss >= 0 sein.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
