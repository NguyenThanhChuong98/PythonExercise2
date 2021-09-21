def multip_keys(dict_input1):
    new_list = []
    numb = 1
    for x in dict_input1.keys():
        new_list.append(x)
        numb = numb * x
    return numb


def multip_values(dict_input2):
    numb = 1
    for x in dict_input2:
        numb = numb * dict_input2[x]
    return numb


new_dict = {1: 2, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
print(multip_values(new_dict))
print(multip_keys(new_dict))
