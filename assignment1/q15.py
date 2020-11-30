def insert_string_middle(braces: str, string: str) -> str:
    center_index = int(len(braces) / 2)
    result = braces[:center_index] + string + braces[center_index:]
    return result