from typing import Dict, List
def empty_counter(items: List[Dict]) -> bool:
    
    for i in items:
        # print(bool(i))
        if  bool(i):
            return False
    
    return True