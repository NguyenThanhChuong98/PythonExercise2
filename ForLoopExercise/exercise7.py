def print_items(lst):
    for x in lst:
        print(x,type(x))


new_list = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
print_items(new_list)
