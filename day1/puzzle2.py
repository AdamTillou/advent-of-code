numbers = open('data').read().split("\n")[0:-1]

for q in numbers:
    for r in numbers:
        for s in numbers:
            if q + r + s == 2020:
                print(str(q) + ' * ' + str(r) + ' * ' + str(s) +
                      ' = ' + str(q * r * s))
                exit()
