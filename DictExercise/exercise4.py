def check_key(n, dict_input):
    for x in dict_input.keys():
        if x == n:
            return True
        else:
            return False


new_dict = {1: "first", 2: "second", 3: "third"}
print(check_key(5, new_dict))
