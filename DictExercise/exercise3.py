def concat_dicts(dict1,dict2,dict3):
    init_dict = dict()
    init_dict.update(dict1.items())
    init_dict.update(dict2.items())
    init_dict.update(dict3.items())
    return init_dict


new_dict1 = {1: 10, 2: 20}
new_dict2 = {3: 30, 4: 40}
new_dict3 = {5: 50, 6: 60}
print(concat_dicts(new_dict1,new_dict2,new_dict3))
