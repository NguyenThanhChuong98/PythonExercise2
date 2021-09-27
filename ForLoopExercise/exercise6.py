def count_odd_even(tup):
    count_odd = 0
    count_even = 0
    for x in tup:
        if x % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print("Number of odd: ", count_odd, "Number of event: ", count_even)


new_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd_even(new_tup)
