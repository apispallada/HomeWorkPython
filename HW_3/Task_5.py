'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
*Пример:*
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''
num = int(input('введите число: '))
count = 2
i = 2
fibpossitiv = [1, 1]
fibnegativ = [1, -1]
while count < num:
    fibpossitiv.append(fibpossitiv[i-2] + fibpossitiv[i-1])
    fibnegativ.append(fibnegativ[i-2] + fibnegativ[i-1]*(-1))
    count += 1
    i += 1
fibneg_rev = list(reversed(fibnegativ))
result = [*fibneg_rev, 0, *fibpossitiv]
print(result)
