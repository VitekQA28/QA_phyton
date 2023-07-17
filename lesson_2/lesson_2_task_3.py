
'''
1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата — и возвращающую площадь квадрата. 

*Площадь квадрата = сторона * сторона.*

2. Если переданный аргумент был не целым, округлите результат вверх.
'''
import math

def square(side):
    area = side * side
    if not isinstance(area, int): # not isinstance не включает в себя area или числовое значение
        area = math.ceil(area) #math.ceil округляет в большую сторону
    return area


side = square(2)
print("Площадь квадрата со стороной 2: ", side)

side = square(5.5)
print("Площадь квадрата со стороной 5.5: ", side)


