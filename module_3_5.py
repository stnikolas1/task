def get_multiplied_digits (number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        first = int(str_number[0])
        first = first * get_multiplied_digits(int(str_number[1:]))
    return first
print(get_multiplied_digits(150908))
