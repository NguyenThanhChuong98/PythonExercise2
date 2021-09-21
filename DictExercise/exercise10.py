def sum_keys(dict_input1):
    new_list = []
    for x in dict_input1.keys():
        new_list.append(x)
        sum_all_keys = sum(new_list)
    return sum_all_keys


def sum_values(dict_input2):
    new_list = []
    for x in dict_input2.values():
        new_list.append(x)
        sum_all_values = sum(new_list)
    return sum_all_values


new_dict = {1: 2, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
print(sum_keys(new_dict))
print(sum_values(new_dict))
