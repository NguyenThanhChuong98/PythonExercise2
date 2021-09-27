def remove_duplicate_list(lst):
    new_list = list(set(lst))
    return new_list


list_num = (1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 0)
print(remove_duplicate_list(list_num))
