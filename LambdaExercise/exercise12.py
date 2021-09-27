def rearrange_numb(arr):
    result = sorted(arr, key=lambda i: 0 if i == 0 else -1 / i)
    return result


array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
print(rearrange_numb(array_nums))
