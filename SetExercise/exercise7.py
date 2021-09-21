def create_union(set1, set2):
    union_sets = set1.union(set2)
    return union_sets


new_set1 = {'city', 'united', 'street', 'country', 'road'}
new_set2 = {'city', 'united', 'link', 'group', 'combination'}
print(create_union(new_set1, new_set2))
