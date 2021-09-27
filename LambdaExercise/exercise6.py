def square_numb(lst):
    square_list = list(map(lambda x: x ** 2, lst))
    return square_list


def cube_numb(lst):
    cube_list = list(map(lambda x: x ** 3, lst))
    return cube_list


new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(square_numb(new_list))
print(cube_numb(new_list))
