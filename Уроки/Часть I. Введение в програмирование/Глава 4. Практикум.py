# Первое задание.
def f1(x):
    """
    Возвращает квадрат x
    :параметр x: целое число.
    :return: квадрат x.
    """
    return x**2
print(f1(5))
# Второе задание.
def f2(string):
    """
    Выводит параметр.
    :параметр string: строка.
    :print: вывод.
    """
    print(string)
f2("Туповатое задание... или я туповат.")
# Третье задание.
def f3(a, b, c, x=0, y=1):
    """
    Выводит параметры.
    :параметры a, b, c, x, y: целые числа.
    :print: вывод.
    """
    print(a, b, c, x, y)
f3(2, 3, 4)
# Четвёртое задание.
def fun1(x):
    """
    Возвращает деление икса на 2.
    :параметр x: целое число.
    :return: частное x и 2.
    """
    return x / 2
def fun2(y):
    """
    Возвращает умнодение y на 4.
    :параметр y: целое число.
    :return: произведение y и 4.
    """
    return y * 4
move = fun1(int(input("Введите число, которое нужно разделить на 2: ")))
print(int(fun2(move)))
# Пятое задание.
def f5(x):
    """
    Возвращает вещественный x.
    :параметр x: вещественное число.
    """
    return float(x)
try:
    print(f5(input("Введите число: ")))
except ValueError:
    print("Ошибка")
# Шестое задание: добавить ко всем функциям документацию.
