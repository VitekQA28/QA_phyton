
def bank(X, Y): # Функция bank принимает 2 параметра X и Y, где X - сумма вклада, а Y - срок
       
    for _ in range(Y): # for _ in range(Y) запускаем цикл на Y лет
        X += X * 0.1
    return X # возвращаем сумму вклада 

X = int(input("Введите сумму вклада: "))
Y = int(input("Введите срок вклада (в годах): "))

sum_X = bank(X, Y)
print("Сумма на счету через", Y, "лет:", sum_X)