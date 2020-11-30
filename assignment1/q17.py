from typing import List
def product(items: List[int]) -> int:
    prod = 1

    for i in items:
        prod *= i

    return prod


#OR use reduce.