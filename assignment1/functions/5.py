def factorial(number: int) -> int:
    fact = 1
    for i in range(number, 0, -1):
        fact *= i
    return fact