from typing import List
def summer(items: List[int]) -> int:
    sum = 0

    for i in items:
        sum += i

    return sum


#OR use reduce.