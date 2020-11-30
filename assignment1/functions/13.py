from typing import Tuple, Any, List
def tuple_sorter(tup: List[Tuple[Any]]) -> List[Tuple[Any]]:
    return (sorted(tup, key = lambda x: x[0]))

