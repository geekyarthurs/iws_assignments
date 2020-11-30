from typing import List
def unique_filter(items: List) -> List:
    unique = []
    for i in items:
        if i not in unique:
            unique.append(i)
    
    return unique

