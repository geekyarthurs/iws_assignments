from typing import Tuple, Any
def tup_str(tup: Tuple[Any]) -> str:
    tup_strred = (str(x) for x in tup)
    return " ".join(tup_strred)
