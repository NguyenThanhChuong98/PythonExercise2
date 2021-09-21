def find_index(n, tup):
    tup_index = tup.index(n)
    return tup_index


new_tup = (2, 1, 6, 8, 9, 0, 12, 34, 53, 65, 14)
print(find_index(53, new_tup))
