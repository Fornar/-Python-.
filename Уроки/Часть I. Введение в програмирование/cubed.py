# Модуль для главы 8, второго задания.
def cubed():
    while True:
        try:
            x = int(input("Введите число, которое нужно возвести в куб: "))
            break
        except ValueError:
            print("Только число.")
    x = x ** 3
    print(x)
    
