def find_days_six_len(lst):
    find_days = filter(lambda x: x if len(x) == 6 else '', lst)
    for y in find_days:
        print(y)


new_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
find_days_six_len(new_list)
