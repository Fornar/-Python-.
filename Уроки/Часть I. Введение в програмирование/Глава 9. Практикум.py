# Первое задание
with open(r"C:\Users\user\Desktop\Программирование\Блокнот.txt", "r") as f:
    print(f.read())

# Второе задание
answer = input("Как вас зовут?: ")
with open("answer.txt", "w") as ans:
    ans.write("Пользователя зовут: " + answer)

# Третье задание
import csv

films = [["Звёздные войны",
          "Терминатор",
          "Искусственный интеллект"],
         ["Дурак",
          "Матильда",
          "Девиафан"],
         ["Люди в чёрном",
          "Я - робот",
          "Эволюция"]]

with open("films.csv", "w") as f:
    m = csv.writer(f, delimiter=",")
    for movie_list in films:
        m.writerow(movie_list)
