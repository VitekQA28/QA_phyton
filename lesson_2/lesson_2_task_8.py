# Создайте список [ 18, 14, 10, 6, 2 ] с помощью функции range() и выведите его на экран.

'''
Функция `range()` используется для создания последовательности чисел. 
В данном случае, мы используем `range(18, 1, -4)`, 
где начальное значение равно 18, конечное значение равно 1 (не включительно), a шаг равен -4. 
Затем мы преобразуем результат в список c помощью `list()`, и выводим его на экран c помощью `print()`.
'''
my_list = list(range(18, 1, -4)) # от start до stop с шагом step (не включая значение stop)
print(my_list)