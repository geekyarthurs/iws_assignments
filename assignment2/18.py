import json


print(dir(json))

print(help(json))

my_info = {"name": "Mahesh c. Regmi", "age": 19}

json_str = json.dumps(my_info)
des_my_info = json.loads(json_str)

print(f"JSON: {json_str}")