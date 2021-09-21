def remove_item(n, set):
    if n in set:
        set.discard(n)
    return set


new_set = {'catch', 112, 981, 'say', 'lent', 'rent'}
print(remove_item('say', new_set))
