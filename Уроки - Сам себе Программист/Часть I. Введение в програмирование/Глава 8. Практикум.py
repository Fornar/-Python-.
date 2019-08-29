# Первое задание
data = [1, 3, 5, 12]

import statistics
print(statistics.mean(data))

print(statistics.harmonic_mean(data)) # Гармоничное среднее - это ещё нужно учить по математике в будущем. Формула:
# n/(1/a + 1/b + 1/c...).

print(statistics.median_low(data)) # Ещё есть .high - легко додуматься, что оно выполняет
# Возвращается меньше значение, если число точек данных чётное, то возвращается меньшее из двух средних значений

# Второе задание
import cubed
cubed.cubed()
