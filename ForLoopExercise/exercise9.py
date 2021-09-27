def fib_numb(numb1, numb2):
    print(numb1)
    for x in range(0, 51):
        print(numb1 + numb2)
        numb1 += numb2
        numb2 = numb1 - numb2


fib_numb(0, 1)