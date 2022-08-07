'''
Задайте натуральное число N. Напишите программу, которая составит список 
простых делителей числа N. (1 - составное число)
'''
num = int(input("Введите число: "))
print("Простые делители " + str(num) + " -> ", end = " ")
for i in range(num, 1, -1):
    simple_div = 0
    if num % i == 0:
        for j in range(i-1, 1, -1):
            if i % j == 0:
                simple_div += 1
        if simple_div == 0:
            print(i, end = " ")
 
