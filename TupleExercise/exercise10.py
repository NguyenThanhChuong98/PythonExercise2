def find_num(n, tup):
    numb = n
    for x in tup:
        if x == numb:
            return numb


new_tup = (1, 2, 3, 4, 5, 6, 7)
print(find_num(1, new_tup))

