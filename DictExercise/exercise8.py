def merge_two_dicts(dict_input1, dict_input2):
    new_dict = dict_input1.copy()
    new_dict.update(dict_input2)
    return new_dict


new_dict1 = {"first": 1, "second": 2, "third": 3, "fourth": 4}

new_dict2 = {"fifth": 5, "sixth": 6, "eighth": 8, "ninth": 9}
print(merge_two_dicts(new_dict1, new_dict2))
