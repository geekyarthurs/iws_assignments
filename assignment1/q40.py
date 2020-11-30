from typing import Tuple, Any
def tuple_adder(tup: Tuple[Any], item: Any) -> Tuple:
    return (*tup, item)