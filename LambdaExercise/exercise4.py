def sort_list(lst_input):
    sort_list_input = sorted(lst_input, key=lambda x: x['color'])
    return sort_list_input


new_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
            {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
            {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print(sort_list(new_list))
