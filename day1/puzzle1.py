numbers = open('data').read().split("\n")[0:-1]


print('started')
myvar = numbers
for q in numbers:
    for r in numbers:
        if q + r == 2020:
            print(str(q) + ' * ' + str(r) + ' = ' + str(q * r))
            exit()
