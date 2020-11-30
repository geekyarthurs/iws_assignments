from typing import List

def inserter(items: List, string: str) -> None:

    items = items.copy()
    for i in range(len(items)):
        items[i] = string + str(items[i]) 
    
    return items
