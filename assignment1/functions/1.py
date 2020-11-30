def max_of_three(x: int, y: int, z: int) -> int:
    
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z