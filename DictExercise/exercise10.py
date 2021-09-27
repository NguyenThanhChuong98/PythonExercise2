def sum_values(dict_input1):
    new_list = []
    for x in dict_input1.values():
        new_list.append(x)
    sum_all_values = sum(new_list)
    return sum_all_values


def sum_values_2(dict_input2):
    sum = 0
    for x in dict_input2.values():
        sum += x
    return sum


new_dict = {1: 2, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
print(sum_values(new_dict))
print(sum_values_2(new_dict))
