def create_shallow_copy(set_input):
    set_shallow_copy = set_input.copy()
    return set_shallow_copy


new_set = {1, 2, 3, 4, 5, 6, 7, 8}
print(create_shallow_copy(new_set))
