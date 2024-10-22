numbers = []
primes = []
not_primes =[]
n = 0
print('Заполните список через Enter до 28, для завершения заполнения напишите: stop')
while 1 > 0:
    n = input()
    if n != "stop":
        n = int(n)
        numbers.append(n)
    else:
        break
numbers.sort()
n = 0
for i in range(len(numbers)):
    if numbers[i] != 1:
        for j in range(2, max(numbers) + 1):
            if numbers[i] / j == 1 and n == 0:
                primes.append(numbers[i])
                n = 0
                break
            else:
                if numbers[i] % j == 0:
                    n += 1
                    if (numbers[i] < j or numbers[i] == j) and n != 0:
                        not_primes.append(numbers[i])
                        n = 0
                        break

print(primes)
print(not_primes)