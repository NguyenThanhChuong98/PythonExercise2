def remove_key(n, dict_input1):
    del dict_input1[n]
    return dict_input1


new_dict = {1: 2, 2: 3, 4: 5}
print(remove_key(1, new_dict))
