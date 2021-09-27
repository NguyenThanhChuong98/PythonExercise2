def input_line():
    user_input = input("Please input your words: ")
    if len(user_input) == 0:
        exit()
    else:
        x = user_input.lower()
    print(x)


input_line()
