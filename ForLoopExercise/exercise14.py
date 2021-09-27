def check_letter_numb(str_input):
    count_letter = 0
    count_numb = 0
    for x in str_input:
        if x.isalpha():
            count_letter += 1
        elif x.isdigit():
            count_numb += 1
    return count_letter, count_numb


new_string = ('Python 3.2')
print(check_letter_numb(new_string))
