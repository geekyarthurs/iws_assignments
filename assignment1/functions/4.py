# you can simply [::-1]

def reverser(string: str):
    result = ""

    for i in range(len(string)-1, -1, -1):
        result += string[i]
    return result