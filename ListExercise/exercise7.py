def remove_duplicate_list(lst):
    new_list = []
    for x in lst:
        if x not in new_list:
            new_list.append(x)
    return new_list


list_num = (1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 0)
print(remove_duplicate_list(list_num))