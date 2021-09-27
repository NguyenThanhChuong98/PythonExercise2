def zip_dict(keys, values):
    map_dict = dict(zip(keys, values))
    return map_dict


new_keys = ['Power', 'Energy', 'Speed']
new_values = [100, 60, 90]

print(zip_dict(new_keys,new_values))
