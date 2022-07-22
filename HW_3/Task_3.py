'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
arr = [1.1, 1.2, 3.1, 5, 10.01]
def numberСonversion(arr):
    new_arr = []
    for i in range(len(arr)):
        a = arr[i]
        new_arr.append(round(a - int(a), 2))
        i += 1
    return new_arr
print(numberСonversion(arr))

def maxmin_difference(arr):
    max_num = arr[0]
    min_num = arr[0]
    diff = 0
    for i in range(len(arr)):
        if arr[i] != 0 and arr[i] > max_num:
            max_num = arr[i]
        if arr[i] != 0 and arr[i] < min_num:
            min_num = arr[i]
            print(max_num, min_num)
    diff = max_num - min_num
    return diff
print(maxmin_difference(numberСonversion(arr)))

