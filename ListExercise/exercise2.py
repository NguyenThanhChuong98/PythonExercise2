def list_mult(lst):
    multi_numb = 1
    for x in lst:
        multi_numb = multi_numb * x
    return multi_numb


list_numb = (2, 4, 6)
print(list_mult(list_numb))