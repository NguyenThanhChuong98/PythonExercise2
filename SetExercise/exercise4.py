def remove_item(n, set):
    set.remove(n)
    return set


new_set = {'morning', 5, 'lamp', 12, 'development'}
print(remove_item(5, new_set))
