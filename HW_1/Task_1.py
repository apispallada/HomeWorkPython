'''
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот 
день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
'''
usernumber = int(input('Input number of weekday: '))
if (usernumber < 1 or usernumber > 7):
    print('Incorrect number')
if (usernumber == 6 or usernumber == 7):
    print('Yes!')
if (usernumber >= 1 and usernumber <= 5):
    print('No')
