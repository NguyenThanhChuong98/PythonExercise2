def check_char(char):
    return lambda x: True if x.startswith(char) else False


find_first_char = check_char("C")
print(find_first_char("Clown"))
