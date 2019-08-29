# Первое задание
shows = ["Ходячие мертвецы",
         "Красавцы",
         "Клан Сопрано",
         "Дневники вампира"]
for show in shows:
    print(show)
    
# Второе задание
for i in range(25, 51):
    print(i)

# Третье задание
for index, tt in enumerate(list1):
    print(tt + " - индекс элемента = {}".format(index))

# Четвёртое задание
numbers = [2, 4, 15, 12, 24, 27, 32, 36, 45, 50]
while True:
    print('Введите "Х", чтобы выйти')
    answer = input("Угадайте число от 1 до 50!: ")
    if answer == "Х":
        break
    try:
        answer = int(answer)
    except ValueError:
        print('Либо "Х", либо число.')
        continue
    if answer > 50 or answer < 1:
        print("ОТ 1 ДО 50")
        continue
    for i in numbers:
        print(i)
        if i == int(answer):
            print("Поздравляю! Вы угадали число с 20% шансов")
            break

# Пятое задание
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
all_list = list()

for i in list1:
    for j in list2:
        all_list.append(i * j)

print(all_list)
