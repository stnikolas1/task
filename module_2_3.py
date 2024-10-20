my_list = []
n = 0
m = 0
print('Заполните список через Enter, для завершения заполнения напишите: stop')
while 1 > 0:
    n = input()
    if n != "stop":
        n = int(n)
        my_list.append(n)
    else:
        n = len(my_list)
        break
while n > 0:
    if my_list[m] > 0:
        print(my_list[m])
        m = m + 1
        n = n -1
    else:
        if my_list[m] == 0:
            m = m + 1
            n = n -1
        else:
            break
