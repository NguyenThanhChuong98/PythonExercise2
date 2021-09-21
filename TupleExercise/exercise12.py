def remove_item(n, tup):
    conv_list = list(tup)
    conv_list.remove(n)
    conv_tup = tuple(conv_list)
    return conv_tup


new_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(remove_item(2, new_tup))
