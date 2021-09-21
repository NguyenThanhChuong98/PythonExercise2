def sort_ascend(dict_input):
    sorted_dict = sorted(dict_input.items(),
                         key=lambda x: x[1])
    return sorted_dict


new_dict = {"second": 2, "first": 1, "fourth": 4, "third": 3, "fifth": 5, }
print(sort_ascend(new_dict))


def sort_descend(dict_input_2):
    sorted_dict = sorted(dict_input_2.items(),
                         key=lambda x: x[1], reverse=True)
    return sorted_dict


new_dict_2 = {"second": 2, "first": 1, "fourth": 4, "third": 3, "fifth": 5, }
print(sort_descend(new_dict_2))
