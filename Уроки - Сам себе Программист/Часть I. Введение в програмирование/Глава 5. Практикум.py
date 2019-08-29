# Первое задание.
music_list = ["Оксимирон", "RAMMSTAIN"]
print(music_list)

# Второе задание.
my_place_list = list()
Omsk = (54.9893, 73.3682)
Sheregesh = (52.9211, 87.9893)
Sevastopol = (44.6166, 33.5254)

my_place_list.append(Omsk)
my_place_list.append(Sheregesh)
my_place_list.append(Sevastopol)
print(my_place_list)

# Третье задание.
my_dict = {'имя': 'Александр',
           'фамилия': 'Погорелов',
           'отчество': 'Александрович',
           'рост': '175',
           'вес': '62',
           'цвет глаз': 'серый '}
my_dict["темперамент"] = "флегматик"
print(my_dict)

# Четвёртое задание.
answer = input('''Введите параметр, который хотите узнать.
(вот список: имя, фамилия, отчество, рост, вес, цвет глаз, темперамент)
: ''')
if  answer in my_dict:
    print(my_dict[answer])
else:
    print("Такой параметр отсутствует")

# Пятое задание.
favorite_music = {"RAMMSTAIN": ["DEUTSCHLAND", "RADIO", "Du hast"]
                  "Oxxxymiron": ['Альбом "Горгород"', 'Не из мира сего', "Биполярочка"]}

# Шестое задание.
# Множества в файле "Контейнеры. глава 5"










