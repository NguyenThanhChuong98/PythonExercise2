def check_numb(x):
    new_var = lambda x: True if type(x) is int else False
    print(new_var(x))


new_string = [1,"a",4,"a"]
for c in new_string:
    check_numb(c)
