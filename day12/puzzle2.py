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
waypoint = [10, 1]
angle = 0

for q in data:
    if q['command'] == 'E':
        waypoint[0] += q['number']
    elif q['command'] == 'W':
        waypoint[0] -= q['number']
    elif q['command'] == 'N':
        waypoint[1] += q['number']
    elif q['command'] == 'S':
        waypoint[1] -= q['number']
    elif q['command'] == 'F':
        position[0] += waypoint[0] * q['number']
        position[1] += waypoint[1] * q['number']
    elif q['command'] == 'B':
        position[0] -= waypoint[0] * q['number']
        position[1] -= waypoint[1] * q['number']

    elif q['command'] == 'L':
        for i in range(int(q['number'] / 90)):
            newx = -waypoint[1]
            newy = waypoint[0]
            waypoint = [newx, newy]
        
    elif q['command'] == 'R':
        for i in range(int(q['number'] / 90)):
            newx = waypoint[1]
            newy = -waypoint[0]
            waypoint = [newx, newy]

print(position)
print(abs(position[0]) + abs(position[1]))
