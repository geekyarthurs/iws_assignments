from typing import List
def long_finder(words: List) -> int:
    lengths = map(len,words)
    return max(lengths)
