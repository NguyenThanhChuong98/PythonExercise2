def add_key(dict_input, key, value):
    dict_input[key] = value
    return dict_input


new_dict = {0: 10, 1: 20}
print(add_key(new_dict, 2, 30))
