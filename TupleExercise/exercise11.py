def convert_list_to_tup(tup):
    new_string = ''
    for x in tup:
        new_string += x
    return new_string


new_tup1 = ("at least", " they have", " a car")
print(convert_list_to_tup(new_tup1))
