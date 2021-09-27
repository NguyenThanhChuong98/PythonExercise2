import random

user_input = int(input("Please input your numb: "))


def guess_numb():
    random_numb = random.randint(1, 9)
    while True:
        user_input = int(input("Please input your numb: "))
        if user_input == random_numb:
            print("Well guessed!")
            break
        else:
            print("again!")


guess_numb()
