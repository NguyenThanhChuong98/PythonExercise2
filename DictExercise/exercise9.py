def iter_dict(dict_input):
    for x in dict_input.items():
        print(x)


new_dict = {"first": 1, "second": 2, "third": 3, "fourth": 4}
print(iter_dict(new_dict))