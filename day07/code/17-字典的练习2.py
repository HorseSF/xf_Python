# dict1 = {"a":100,"b":200,"c":300}
# {100:"a",200:"b",300:"c"}

dict1 = {"a": 100, "b": 200, "c": 300}

new_dict1 = {}

for key, value in dict1.items():
    new_dict1[value] = key
print(new_dict1)

dict1 = {v: k for k, v in dict1.items()}
print(dict1)
