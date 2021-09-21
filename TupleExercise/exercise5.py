def add_item(tup):
    new_list = list(tup)
    new_list.append("Hello")
    tup = tuple(new_list)
    return tup


new_tuple = ()
print(add_item(new_tuple))