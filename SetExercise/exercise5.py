def remove_item(n, set_input):
    if n in set_input:
        set_input.discard(n)
    return set_input


new_set = {'catch', 112, 981, 'say', 'lent', 'rent'}
print(remove_item('say', new_set))
