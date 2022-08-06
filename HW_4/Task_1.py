'''
Вычислить число c заданной точностью d
Пример:
- при d = 3, π = 3.141
'''
d = int(input("Введите желаемое количество знаков числа 'Пи': "))
n = 10000
pi = 0.0
current = 1
for i in range(1, n):
    pi = (12 ** 0.5) * (1 - current / ((2 * i + 1) * 3 ** i))
    current *= -1
print(round(pi, d))