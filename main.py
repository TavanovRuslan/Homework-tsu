def parab(x):
    return x**2


def line(x):
    return 2*x


def extremum(func, a, b):
    if a > b:
        exit(-1)
    temp = [999999]
    for x in range(a, b+1):
        temp.append(func(x))
    temp.append(-999999)

    for i in range(1, len(temp)-1):
        if temp[i] > temp[i-1] and temp[i] > temp[i+1]:
            print("Максимум:", temp[i])

    for i in range(1, len(temp)-1):
        if temp[i] < temp[i-1] and temp[i] < temp[i+1]:
            print("Минимум:", temp[i])

    print(*temp[1:-1])

extremum(parab, -5, 5)
print()
extremum(parab, -10, 10)
print()
extremum(line, -5, 5)
print()
extremum(line, -10, 10)