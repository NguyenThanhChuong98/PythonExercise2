def check_list(lst):
    for x in range(len(lst)):
        if len(lst) == 0:
            return None
        else:
            return lst


lst_1 = []
lst_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(check_list(lst_1))
print(check_list(lst_2))