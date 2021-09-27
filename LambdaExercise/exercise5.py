def filter_even(lst):
    filter_even_numb = list(filter(lambda x: x % 2 == 0, lst))
    return filter_even_numb


def filter_odd(lst):
    filter_odd_numb = list(filter(lambda x: x % 2 != 0, lst))
    return filter_odd_numb


new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_even(new_list))
print(filter_odd(new_list))
