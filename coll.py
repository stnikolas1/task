calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info (string):
    cor = ()
    n = len(string)
    cor = cor + (n, string.upper(), string.lower())
    calls = count_calls()
    return cor
def is_contains(string, list):
    string = string.lower()
    for i in range(len(list)):
        list [i] = list[i].lower()
        if string == list[i]:
            argument = True
            break
        else:
            argument = False
    calls = count_calls()
    return argument
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban',['ban','BaNaN','urBAN']))
print(calls)