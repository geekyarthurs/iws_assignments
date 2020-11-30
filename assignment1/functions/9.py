def prime_checker(num: int) -> bool:

    for i in range(2, int(num ** 1/2) + 1):
        if num % i == 0:
            return False
    return True