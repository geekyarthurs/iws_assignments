from typing import List
def last_elem_replacer(parent: List, child: List):
    return [ *parent[:-1] , *child ]