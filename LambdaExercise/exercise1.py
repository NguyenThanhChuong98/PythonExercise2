def add_item(n):
    return lambda x: x + n


additem = add_item(15)

print(additem(10))


def multip_item(y):
    return lambda x: x * y


multitem = multip_item(6)

print(multitem(8))
