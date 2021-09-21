def set_sym_diff(set1, set2):
    set_nym = set1.symmetric_difference(set2)
    return set_nym


new_set1 = {'coke', 'juice', 'water', 'alcohol', 'beer'}
new_set2 = {'coke', 'juice', 'tea', 'coffee'}
print(set_sym_diff(new_set1, new_set2))
