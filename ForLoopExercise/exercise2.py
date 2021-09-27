input = ("60F")


# c/5 = f-32/9
# c = (f - 32) * 5 / 9
# f = ((c/5) * 9) + 32

def convert_celsius(f):
    c = ((f - 32) * 5) / 9
    return c


def convert_fahrenheit(c):
    f = ((c / 5) * 9) + 32
    return f


print(convert_celsius(45))
print(convert_fahrenheit(60))
