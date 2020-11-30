from typing import Dict
def dict_printer(dict: Dict) -> None:
    for k,v in dict.items():
        print( str(k) + ": " + str(v) )


sample_dict = { "name" : "Mahesh", "age" : 20, "location": "Kathmandu" }
dict_printer(sample_dict)