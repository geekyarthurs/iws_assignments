from typing import List 
def prod_of_numbers(number: List):
    prod = 1
    for i in number:
        prod *= i
    return prod