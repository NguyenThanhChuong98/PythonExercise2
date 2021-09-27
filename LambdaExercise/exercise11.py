def inter_arrays(arr1, arr2):
    result = list(filter(lambda x: x in arr1, arr2))
    return result


new_array1 = [1, 2, 3, 5, 7, 8, 9, 10]
new_array2 = [1, 2, 4, 8, 9]
print(inter_arrays(new_array1, new_array2))
