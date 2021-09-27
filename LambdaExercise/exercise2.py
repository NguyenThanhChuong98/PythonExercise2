def take_argument(input):
    return lambda x: input * x


new_var = take_argument(15)
print(new_var(3))
