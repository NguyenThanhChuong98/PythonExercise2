def clone_list(lst):
    new_list = lst.copy()
    return new_list


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = ['dog', 'cat', 'fish', 'tiger', 'buffalo']

print(clone_list(list_1))
print(clone_list(list_2))