'''
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние 
между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''
print('Bведите через пробел координаты X и Y первой точки: ')
x1, y1 = map(int, input().split())
print('Bведите через пробел координаты X и Y второй точки: ')
x2, y2 = map(int, input().split())
distance = round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)
print(distance)