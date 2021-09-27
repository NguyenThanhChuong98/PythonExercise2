def gene_numb(n):
    d = dict()
    for x in range(1, n + 1):
        d[x] = x * x
    print(d)


numb_input = int(input("Input a number "))
gene_numb(numb_input)
