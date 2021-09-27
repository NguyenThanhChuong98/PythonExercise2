def two_dimen(m, n):
    new_list = []
    for i in range(0, m):
        new_list_1 = []
        for j in range(0, n):
            new_list_1.append(0)
        new_list.append(new_list_1)
    for k in range(m):
        for l in range(n):
            new_list[k][l] = k * l

    print(new_list)

two_dimen(3, 4)

