numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range (len (numbers)):
    if numbers [i] < 2:
        continue                       # если число меньше 2, то перескакивает в начало цикла
    is_primes = True
    for j in range (2, numbers [i]):   # проверка, что выбранное число не делится в диапазоне от 2х до num[i]
        if numbers [i] % j == 0:       # проверка на простоту/сложные числа
            not_primes.append (numbers[i]) # записывает в список со сложными числами
            is_primes = False
            break
    if is_primes:                       # если флаг = True, то записываем в список простых чисел
        primes.append (numbers [i])

print (primes)
print (not_primes)