from typing import Dict, List
def key_remover(item: Dict, key) -> Dict: 
    item = item.copy()
    if key in item:
        del item[key]
    return item