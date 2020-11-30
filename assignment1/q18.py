from typing import List, Union

# max(items) also works.
def max_finder(items: List) -> Union[int,float]:
    max_ = items[0]
    

    for i in items:
        max_ = i if i > max_ else max_

    return max_