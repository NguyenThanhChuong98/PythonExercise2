def find_words_long(n, lst):
    lst_words = []
    for x in lst:
        if len(x) > n:
            lst_words.append(x)
    return lst_words


list1 = ('capital', 'breakfast', 'knowledge', 'development', 'concentrate', 'snore')
print(find_words_long(8, list1))