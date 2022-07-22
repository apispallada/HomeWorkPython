'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
#list = [15, 2, 6, 4, 11, 8, 7]
list = [8, 3, 9, 5, 2, 4, 5, 4, 3, 2]
def productOfNumbers(arr):
    prod = []
    i = 0
    if len(list)%2 == 0:
        for i in range(len(list)//2):
            prod.append(arr[i] * arr[(i+1)*-1])
    else:
        for i in range(len(list)//2+1):
            prod.append(arr[i] * arr[(i+1)*-1])
    i += 1
    return prod
print(productOfNumbers(list))

