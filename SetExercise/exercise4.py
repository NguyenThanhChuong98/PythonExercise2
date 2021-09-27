def remove_item(n, set_input):
    set_input.remove(n)
    return set_input


new_set = {'morning', 5, 'lamp', 12, 'development'}
print(remove_item(5, new_set))
