'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11
'''
n = input('Input number: ')
number = (n.replace('.', '0'))
num = int(number)
sum = 0
while num != 0:
    sum += num%10
    num = num//10
print(number + ' -> ' + str(sum))