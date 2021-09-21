def slice_tup(tup):
    get_right_element = tup[3:5]
    get_left_element = tup[-3:-1]
    return get_right_element, get_left_element


new_tup = (1, "people", "play", 4, 5, 6, "candy", "lollipop", 10)
print(slice_tup(new_tup))
