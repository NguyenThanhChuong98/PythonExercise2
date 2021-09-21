def remove_elements(lst):
    first_element = lst[0]
    fourth_element = lst[4]
    fifth_element = lst[5]
    lst.remove(first_element)
    lst.remove(fourth_element)
    lst.remove(fifth_element)
    return lst


list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_elements(list1))