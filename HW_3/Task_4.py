'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''
number = int(input('Input number: '))
binarray = []
while number > 0:
    binarray.append(number % 2)
    number = number // 2
    binarray.reverse()
print("".join(map(str, binarray)))


