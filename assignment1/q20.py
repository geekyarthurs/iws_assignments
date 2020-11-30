from typing import List
def unique_counter(items: List[str]) -> int:
    
    count = 0

    for i in items:
        if len(i) >= 2 and ( i[0] == i[-1] ):
            count += 1
    
    return count
