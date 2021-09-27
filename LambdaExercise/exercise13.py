def count_odd(arr):
    cout_odd = len(list(filter(lambda x: (x % 2 != 0), arr)))
    return cout_odd


def count_even(arr):
    cout_even = len(list(filter(lambda x: (x % 2 == 0), arr)))
    return cout_even


new_array = [1, 2, 3, 5, 7, 8, 9, 10]
print(count_odd(new_array))
print(count_even(new_array))
