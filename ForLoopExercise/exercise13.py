def binary_numb():
    new_str = ("0100,0011,1010,1001,1100,1001")
    str_split = new_str.split(',')
    new_list = []
    for x in str_split:
        conv_int = int(x, base=2)
        if not conv_int % 5:
            new_list.append(x)
    print(','.join(new_list))

binary_numb()

