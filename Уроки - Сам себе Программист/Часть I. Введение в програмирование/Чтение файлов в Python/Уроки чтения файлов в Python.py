# Как читать файлы
# Python содержит в себе функцию, под названием "open"
# Вот несколько примеров, как использовать функцию "открыть" для чтения:
handle = open("test.txt") # Режим "только чтения" # Автоматически просматривает папку, в которой был запущен скрипт
handle = open(r"C:\Users\user\Desktop\Программирование\Саша\Чтение файлов в Python\test.txt", "r")
# r означает, что строка обрабатываетс как исходная. Если не определить строка как исходную, то можно получить неправильный путь.
print(r"C:\Users\user\Desktop\Программирование\Саша\Чтение файлов в Python\test.txt")
# Чтение файла
handle = open("test.txt", "r")
print(handle.read()) # или через переменную data = handle.read(); print(data)
handle.close()

# Чтеие только одной строки файла
handle = open("test.txt", "r")
data = handle.readline()
print(data)
handle.close()

# Из всех строк получается список
handle = open("test.txt", "r")
data = handle.readlines()
print(data)
handle.close()


# Как читать файл по частям
# Самый простой спосб для выполнения этой задачи - использовать цикл
handle = open("test.txt", "r")
for line in handle:
    print(line)
handle.close()

# Чтение файла по частям
handle = open("test.txt", "r")
while True:
    data = handle.read(1024) # 1 килобайт = 1024 байта или символов # По 1024 символа за раз (за 1 цикл)
    print(data)

    if not data:
        handle.close()
        break

# Как читать бинарные (двоичные) файлы
handle = open("test.pdf", "rb") # rb - read-binaryy


# Пишеи в файлах в Python
# Режим написания файлов в Python это "w" и "wb" для write-mode и write-binary-mode соответственно.
# Внимание: использование режимов написания в уже существующем файлу изменит его без предупреждения
handle = open("output.txt", "w")
handle.write("This is a test!")
handle.close()
# Файловый дескриптор имеет метод writeline(написание строк), который будет принимать список строк, который дескриптор, в свою очередь,
# будет записываь по порядку на диск.


# Использование оператора "with"
# В Python есть оператор with, котоырй создаёт диспетчер контекста, который автоматически закрывает файл, по окончанию работы в нём.
with open("test.txt") as file_handler:
    for line in file_handler:
        print(line)









