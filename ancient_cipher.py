print('Введите число от 3 до 20')
n = int(input())
result = []
a = 0
if 3 <= n <= 20 and n % 2 == 0:
    for i in range(1, int((n / 2) + 1)):
            for j in range(2, n):
                if n % (i + j) == 0 and i != j and (result.count(j *10 + i) != True or j == 11):
                    if j - 10 < 0:
                        a = j + i * 10
                        result.append(a)
                    else:
                        a = j + i * 100
                        result.append(a)
else:
    for i in range(1, int(((n-1) / 2) + 1)):
            for j in range(2, n):
                if n % (i + j) == 0 and i != j:
                    if j - 10 < 0:
                        a = i * 10 + j
                        result.append(a)
                    else:
                                a = i * 100 + j
                                result.append(a)

print('Для числа',n,'-',result)
