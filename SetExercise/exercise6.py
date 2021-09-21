def inter_sets(set1, set2):
    inter = set1.intersection(set2)
    return inter


new_set1 = {1, 2, 3, 4, 5, 6, 7}
new_set2 = {8, 9, 10, 11, 12, 1}
print(inter_sets(new_set1, new_set2))
