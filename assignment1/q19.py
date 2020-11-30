from typing import List, Union

# min(items) also works.
def min_finder(items: List) -> Union[int,float]:
    min_ = items[0]

    for i in items:
        min_ = i if i < min_ else min_

    return min_