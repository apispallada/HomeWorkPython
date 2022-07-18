'''
Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''
for x in range(2):
    for y in range(2):
        for z in range(2):
            a = not (x or y or z)
            b = not (x) and not (y) and not(z)
            print(f'{x}\t {y}\t {z}\t {a==b}\t')