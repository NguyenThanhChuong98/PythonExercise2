def check_numb(lst):
    for x in lst:
        if x / 7 and x * 5 in range(1500, 2700):
            print(x)


new_list = [100, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]
check_numb(new_list)
