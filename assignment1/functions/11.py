from typing import Callable
adder: Callable[[int], int] = lambda x: x + 15 

qu2: Callable[[int, int], None] = lambda x,y: print(x * y)