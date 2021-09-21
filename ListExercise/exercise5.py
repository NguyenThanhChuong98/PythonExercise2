def get_first_and_last_char(lst):
    count = 0
    for x in lst:
        if x[0] == x[-1]:
            count += 1
    return count


lst_str = ['abc', 'xyz', 'aba', '1221']
print(get_first_and_last_char(lst_str))