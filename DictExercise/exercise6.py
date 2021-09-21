def gene_dict(n):
    new_dict = dict()
    for x in range(1, n + 1):
        new_dict[x] = x * x
        x += 1
    return new_dict


print(gene_dict(5))
