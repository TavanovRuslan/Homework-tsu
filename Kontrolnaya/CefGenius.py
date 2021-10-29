f = open("input.txt", 'rt')


a = []

for line in f:
    a.append(line)

na = 1     # направление, 0 - север, 1 - восток, 2 - юг, 3 - запад

x = 0
y = 0

i = 0
while i < len(a):
    NN = a[i][1:len(a[i])]

    if a[i][0] == "N":
        y += int(NN)
        print(x, y)
    if a[i][0] == "S":
        y -= int(NN)
        print(x, y)
    if a[i][0] == "E":
        x += int(NN)
        print(x, y)
    if a[i][0] == "W":
        x -= int(NN)
        print(x, y)

    if a[i][0] == "R" and int(NN) == 90:
        na += 1
    if a[i][0] == "R" and int(NN) == -90:
        na -= 1
    if a[i][0] == "L" and int(NN) == -90:
        na += 1
    if a[i][0] == "L" and int(NN) == +90:
        na -= 1

    if na == -1:
        na = 3
    if na == -2:
        na = 2
    if na == -3:
        na = 1
    if na == -4:
        ma = 0

    if na == 4:
        na = 0
    if na == 5:
        na = 2
    if na == 6:
        na = 1
    if na == 7:
        ma = 0

    if a[i][0] == "R" and int(NN) == 180:
        na += 2
    if a[i][0] == "R" and int(NN) == -180:
        na -= 2
    if a[i][0] == "L" and int(NN) == -180:
        na += 2
    if a[i][0] == "L" and int(NN) == +180:
        na -= 2

    if a[i][0] == "F":
        if na == 0:
            y += int(NN)
        if na == 1:
            x += int(NN)
        if na == 2:
            y -= int(NN)
        if na == 3:
            x -= int(NN)
        print(x, y)

    i += 1

print(abs(x) + abs(y))
