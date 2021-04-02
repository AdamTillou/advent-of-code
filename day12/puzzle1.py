strings = open('data').read().split("\n")
data = []
for q in strings:
    if q == '':
        continue

    instruction = {
            'command': q[0],
            'number':int(q[1:])
            }

    data.append(instruction)


position = [0, 0]
direction = [1, 0]
angle = 0

for q in data:
    if q['command'] == 'E':
        position[0] += q['number']
    elif q['command'] == 'W':
        position[0] -= q['number']
    elif q['command'] == 'N':
        position[1] += q['number']
    elif q['command'] == 'S':
        position[1] -= q['number']
    elif q['command'] == 'F':
        position[0] += direction[0] * q['number']
        position[1] += direction[1] * q['number']
    elif q['command'] == 'B':
        position[0] -= direction[0] * q['number']
        position[1] -= direction[1] * q['number']

    elif q['command'] == 'L':
        for i in range(int(q['number'] / 90)):
            newx = -direction[1]
            newy = direction[0]
            direction = [newx, newy]
        
    elif q['command'] == 'R':
        for i in range(int(q['number'] / 90)):
            newx = direction[1]
            newy = -direction[0]
            direction = [newx, newy]

print(position)
print(abs(position[0]) + abs(position[1]))
