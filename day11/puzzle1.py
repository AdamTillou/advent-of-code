data = []
for q in open('data').read().split("\n"):
    if q == '':
        continue
    data.append([])
    for r in q:
        if r == 'L':
            data[-1].append(0)
        else:
            data[-1].append(-1)

def NumberSurrounding(current_data, point):
    surrounding = 0

    for i in [-1, 0, 1]:
        row = point[0] + i
        if row < 0 or row >= len(current_data):
            continue

        for j in [-1, 0, 1]:
            col = point[1] + j
            if col < 0 or col >= len(data[0]):
                continue
            if i == 0 and j == 0:
                continue

            if current_data[row][col] == 1:
                surrounding += 1

    return surrounding

def RunCycle(current_data):
    new_data = []
    for i, q in enumerate(current_data):
        new_data.append([])
        for j, r in enumerate(q):
            if r == -1:
                new_data[-1].append(-1)
                continue

            surrounding = NumberSurrounding(current_data, [i, j])
            if (r == 1 and surrounding < 4) or (r == 0 and surrounding == 0):
                new_data[-1].append(1)
            else:
                new_data[-1].append(0)

    return new_data

old_data = 1
while data != old_data:
    old_data = data
    data = RunCycle(data)

occupied = 0
for q in data:
    for r in q:
        if r == 1:
            occupied += 1

print(occupied)
