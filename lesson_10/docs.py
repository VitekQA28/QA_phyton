#int = 4
#float = 2.5
#bool = True
#str = "Test"
#dict = ()
#list = []

def do_it(param_1: int, param_2: float, param_3: int) -> list:
    """
    Эта функция берет первые 2 параметра, складывает их и умножает на третий.

    Результат печатается в консоль.

    Параметры должы быть числовыми.

    """
    result = (param_1 + param_2) * param_3
    return (param_1, param_2, param_3, result )


lst = do_it(1, 2.5, 8)
print (lst)