def get_elements(tup):
    fourth_element = tup[4]
    last_fourth_element = tup[-4]
    return fourth_element, last_fourth_element


new_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(get_elements(new_tuple))