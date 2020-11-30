from typing import List, Dict
def product(items: Dict) -> int:
    prod = 1

    for i in items.values():
        prod *= i

    return prod


#OR use reduce.