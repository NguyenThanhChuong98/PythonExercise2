def check_sub_set(set1, set2):
    sub_set = set2.issubset(set1)
    return sub_set


new_set1 = {1, 2, 3, 4, 5, 6, 7, 8}
new_set2 = {1, 2, 3}
print(check_sub_set(new_set1, new_set2))
