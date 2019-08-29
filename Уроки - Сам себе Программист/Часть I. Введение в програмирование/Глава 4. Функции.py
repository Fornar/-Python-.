print('Программа деления одного числа на другое.')
try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("Ошибка ввода.")
