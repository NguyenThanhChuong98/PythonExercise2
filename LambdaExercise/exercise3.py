def sort_list(lst):
    lst.sort(key=lambda x: x[0])
    return lst


new_list = [('english', 88), ('science', 90), ('Maths', 97), ('Social sciences', 82)]

print(sort_list(new_list))
