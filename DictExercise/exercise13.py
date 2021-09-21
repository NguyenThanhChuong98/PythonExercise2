def map_two_lists(list_input1, list_input2):
    new_dict = dict()
    new_list = list_input1 + list_input2
    for x in range(1, len(new_list)):
        new_dict[x] = x + 1
    return new_dict


list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [8, 9, 10, 11, 12, 13, 14, 15]
print(map_two_lists(list1, list2))
