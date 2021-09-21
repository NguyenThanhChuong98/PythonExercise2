def create_tup_numb(lst):
    new_tuple = tuple(lst)
    return new_tuple[-3]


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(create_tup_numb(list1))