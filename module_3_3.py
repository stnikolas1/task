def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = ['good', False, 34.78]
values_dict = {'a': True, 'b': 45.12, 'c': 'Nikolas'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [34.12, 'By-By']
print_params(*values_list_2, 42)