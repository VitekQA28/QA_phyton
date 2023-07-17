'''
1. Создайте функцию is_year_leap, принимающую 1 аргумент — год (число) — и возвращающую True, если год високосный, и False — иначе.

Год високосный, если его номер делится на 4 без остатка. 
Например, 2020 или 2008. 2009 или 2023 не делится на 4 без остатка, значит, год не високосный.
'''

def is_year_leap(year):
    if year % 4 == 0: # Если делится на 4 без остатка (0) то високосный
        return True
    else:
        return False

is_year = is_year_leap(2024)
print("год 2024:", is_year)

is_year = is_year_leap(2023)
print("год 2023:", is_year)

is_year = is_year_leap(2020)
print("год 2020:", is_year)

is_year = is_year_leap(2009)
print("год 2009:", is_year)

is_year = is_year_leap(2008)
print("год 2008:", is_year)

print(sep ='\n')

# Второй вариант выполнения (Интереснее)
def is_year_leap(year):
    if year % 4 == 0: 
        return True
    else:
        return False

year = int(input("Введите год: "))  
Y = is_year_leap(year)  
print(Y)  