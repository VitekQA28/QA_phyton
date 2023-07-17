
'''
1. Напишите функцию fizz_buzz, которая принимает один аргумент — n (число).
2. Функция должна печатать числа от 1 до n. При этом:
    1. если число делится на 3, печатать `Fizz`;
    2. если число делится на 5, печатать `Buzz`;
    3. если число делится на 3 и на 5, печатать `FizzBuzz`.
'''
def fizz_buzz(n):
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Вызываем функцию fizz_buzz с аргументом 17
fizz_buzz(17)