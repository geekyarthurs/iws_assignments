from typing import List, Dict
def summer(items: Dict) -> int:
    sum = 0

    for i in items.values():
        sum += i

    return sum


#OR use reduce.