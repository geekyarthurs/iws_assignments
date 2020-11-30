from typing import Tuple, Any
def tuple_remover(tup: Tuple[Any], item: Any) -> Tuple:
    
    return tuple(filter(lambda x: x != item, tup))