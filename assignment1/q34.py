

def dict_merger(dict1, dict2):

    result = dict()

    result.update(dict1)
    result.update(dict2)
    
    return result

# or just [**dict1, **dict2]