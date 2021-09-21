def set_difference(set1, set2):
    set_diff = set1.difference(set2)
    return set_diff


new_set1 = {1, 2, 3, 4, 5}
new_set2 = {6, 3, 5, 9, 19}

print(set_difference(new_set1,new_set2))
