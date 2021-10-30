f = open("input.txt", 'rt')

a = []

for line in f:
    a.append(line)

# Проверка
    try:
        line[1:len(line)] == int(line[1:len(line)])
    except:
        print("Неверная инструкция")
        exit()

    if line[0] != "R" and line[0] != "L" and line[0] != "W" and line[0] != "E" and line[0] != "S" and line[0] != "N" and line[0] != "F":
        print("Неверная инструкция")
        exit()

    if line[0] == "R" or line[0] == "L":
        if int(line[1:len(line)]) % 90 != 0:
            print("Неверная инструкция")
            exit()

na = 1  # Направление, 0 - север, 1 - восток, 2 - юг, 3 - запад

x = 0
y = 0

# Основной код
i = 0
while i < len(a):
    NN = a[i][1:len(a[i])]
    NN = int(NN)

# a[i][0] - первая буква, NN - число после первой буквы
    if a[i][0] == "N":
        y += NN
        print(x, y)
    if a[i][0] == "S":
        y -= NN
        print(x, y)
    if a[i][0] == "E":
        x += NN
        print(x, y)
    if a[i][0] == "W":
        x -= NN
        print(x, y)

# na - направление. Меняет направление взависимости от угла
    if a[i][0] == "R" and NN == 90:
        na += 1
    if a[i][0] == "R" and NN == -90:
        na -= 1
    if a[i][0] == "L" and NN == -90:
        na += 1
    if a[i][0] == "L" and NN == 90:
        na -= 1

    if a[i][0] == "R" and NN == 180:
        na += 2
    if a[i][0] == "R" and NN == -180:
        na -= 2
    if a[i][0] == "L" and NN == -180:
        na += 2
    if a[i][0] == "L" and NN == 180:
        na -= 2

    if a[i][0] == "R" and NN == 270:
        na += 3
    if a[i][0] == "R" and NN == -270:
        na -= 3
    if a[i][0] == "L" and NN == -270:
        na += 3
    if a[i][0] == "L" and NN == 270:
        na -= 3

    if a[i][0] == "R" and NN == 360:
        na += 4
    if a[i][0] == "R" and NN == -360:
        na -= 4
    if a[i][0] == "L" and NN == -360:
        na += 4
    if a[i][0] == "L" and NN == 360:
        na -= 4

# Направление должно быть не меньше нуля и не больше трех.
    if na == 4:
        na = 0
    if na == 5:
        na = 1
    if na == 6:
        na = 2
    if na == 7:
        na = 3

    if na == -1:
        na = 3
    if na == -2:
        na = 2
    if na == -3:
        na = 1
    if na == -4:
        na = 0

    # F зависит от направления
    if a[i][0] == "F":
        if na == 0:
            y += NN
        if na == 1:
            x += NN
        if na == 2:
            y -= NN
        if na == 3:
            x -= NN
        print(x, y)

    i += 1

print(abs(x) + abs(y))
