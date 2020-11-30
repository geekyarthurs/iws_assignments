

def dict_updater(*dicts):

    result = dict()

    for di in dicts:
        result.update(di)
    
    return result

# or just [**dict1, **dict2]