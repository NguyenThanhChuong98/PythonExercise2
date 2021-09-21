def unpack_tup(lst):
    new_tup = tuple(lst)
    (first, second, third, *fourth) = new_tup
    return first, second, third, fourth


list1 = ['Tokyo', 'New York', 'Sydney', 'London', 'Vancouver']
print(unpack_tup(list1))