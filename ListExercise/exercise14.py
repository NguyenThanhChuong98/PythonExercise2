def list_remove_even_numb(lst):
    new_list = []
    for x in lst:
        if x % 2 == 0:
            new_list.append(x)
    return new_list


list1 = [10, 11, 12, 45, 6, 7, 8, 2123]
print(list_remove_even_numb(list1))
