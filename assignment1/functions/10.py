from typing import List
def even_filter(nums: List[int]) -> List[int]:
    evens = []

    for i in nums:
        if i % 2 == 0:
            evens.append(i)
    
    return evens
