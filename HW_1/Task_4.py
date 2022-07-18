'''
Напишите программу, которая по заданному номеру четверти, показывает диапазон 
возможных координат точек в этой четверти (x и y).
'''

print('Input quaerter number: ')
quart = int(input())
if (quart < 1 or quart > 4):
    print('Incorrect number')
elif quart == 1:
    print('X > 0, Y > 0')
elif quart == 2:
    print('X < 0, Y > 0')
elif quart == 3:
    print('X < 0, Y < 0')
elif quart == 4:
    print('X > 0, Y < 0')