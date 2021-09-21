def sort_ascend(dict_input):
    sorted_dict = sorted(dict_input.items())
    return sorted_dict


new_dict = {2: "First", 5: "Second", 7: "Third", 9: "Fourth", 10: "Fifth", 16: "Sixth"}
print(sort_ascend(new_dict))
