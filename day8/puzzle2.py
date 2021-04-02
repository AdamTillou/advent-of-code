real_data = open('data').read().split("\n")
while '' in real_data:
    real_data.remove('')

def DoesItTerminate(data):
    line = 0
    acc = 0
    executed = []

    while True:
        executed.append(line)

        command = data[line].split(' ')[0]
        increment = int(data[line].split(' ')[1])

        if command == 'acc':
            acc += increment

        if command == 'jmp':
            line += increment
        else:
            line += 1

        if line in executed:
            return 0
        if line >= len(data):
            return acc

for i, q in enumerate(real_data):
    new_data = real_data[0 : len(real_data)]

    command = q.split(' ')[0]
    increment = q.split(' ')[1]

    if command == 'acc':
        continue

    if command == 'nop':
        new_data[i] = 'jmp ' + increment
    elif command == 'jmp':
        new_data[i] = 'nop ' + increment

    terminates = DoesItTerminate(new_data)
    if terminates != 0:
        print(terminates)
        break
