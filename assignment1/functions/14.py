from typing import Tuple, Any
def dict_sorter(tup: Tuple[Any], key: Any) -> Any:
    return tuple(sorted(tup, key = lambda x: x[key]))

