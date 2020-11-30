# list(set(items)) also works.
from typing import List

def dup_remover(items: List):
    new_list = []

    for i in items:
        if i not in new_list:
            new_list.append(i)
    
    return new_list