def find_repeat_item(tup):
    for x in tup:
        if tup.count(x) > 1:
            return x


new_tuple = (1, 1, 1, 2, 2, 2, 3, 4, 56, 7, 123, 39012, 58523)
print(find_repeat_item(new_tuple))
