def iter_int():
    multi_three = 3
    multi_five = 5
    for x in range(51):
        if x % multi_three == 0 and x % multi_five == 0:
            print("FizzBuzz")
            continue
        elif x % multi_three == 0:
            print("Fizz")
            continue
        elif x % multi_five == 0:
            print("Buzz")
            continue
        print(x)


iter_int()
