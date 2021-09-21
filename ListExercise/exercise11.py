def get_common_mem(lst1, lst2):
    new_lst = []
    for x in lst1:
        new_lst.append(x)
    for y in lst2:
        if y not in new_lst:
            new_lst.append(y)
        else:
            return y


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 11, 12, 13, 14, 15, 16, 17, 18]
print(get_common_mem(list1, list2))