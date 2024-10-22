print('Введите число от 3 до 20')
n = int(input())
list_ = []
if 3 <= n <= 20 and n % 2 == 0:
    for i in range(1, int((n / 2) + 1)):
            for j in range(n, 1, -1):
                if n % (i + j) == 0 and i != j:
                    list_.append(i)
                    list_.append(j)

else:
    for i in range(1, int(((n-1) / 2) + 1)):
            for j in range(n, 1, -1):
                if n % (i + j) == 0 and i != j:
                    list_.append(i)
                    list_.append(j)

print('Для числа',n,'-',list_)