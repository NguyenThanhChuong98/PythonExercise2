def frozen_set(set_input):
    new_frozen_set = frozenset(set_input)
    return new_frozen_set


new_set = {1, 2, 3, 4, 6, 7, 8, 9}
print(frozen_set(new_set))
