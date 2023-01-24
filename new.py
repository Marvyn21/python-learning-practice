def print_my_string_info(my_string):
    my_string = my_string.lower()
    count_char = {}
    for i, char in enumerate(my_string):
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
        print(char + " (" + str(i) + ") - " + str(count_char[char]))
