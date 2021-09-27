numb = 5

def nested_loop():
    for i in range(numb):
        for j in range(i):
            print("* ", end=" ")
        print('')

    for x in range(numb, 0, -1):
        for y in range(x):
            print("* ", end=" ")
        print('')


nested_loop()
