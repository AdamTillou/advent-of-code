data = open('data').read().split("\n")

line = 0
acc = 0
executed = []

while line not in executed:
    executed.append(line)

    command = data[line].split(' ')[0]
    increment = int(data[line].split(' ')[1])

    if command == 'acc':
        acc += increment

    if command == 'jmp':
        line += increment
    else:
        line += 1

print(acc)
