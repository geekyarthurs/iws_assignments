from typing import Dict
def generator(n: int) -> Dict[int, int]:

    result = dict()

    for i in range(1, n+1):
        result[i] = i ** 2
    
    return result


print(generator(15))