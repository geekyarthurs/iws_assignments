from typing import List, Tuple
def sorter( items: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    
    sorted_items = sorted(items,key=lambda x: x[-1])

    return sorted_items