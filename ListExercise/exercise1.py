def list_sum(lst):
    for x in lst:
        sum_numb = sum(lst)
        x += 1
    return sum_numb


list_numb = (1, 2, 3, 4, 5, 6, 7, 8)
print(list_sum(list_numb))
