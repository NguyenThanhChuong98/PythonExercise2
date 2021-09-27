user_input = input("Pleas input your words: ")


def reverse_words(input):
    for x in range(len(input)- 1, -1, -1):
        print(input[x], end="")




reverse_words(user_input)
