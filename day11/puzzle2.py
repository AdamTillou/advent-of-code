data = []
for q in open('data').read().split("\n"):
    if q == '':
        continue
    data.append([])
    for r in q:
        if r == 'L':
            data[-1].append(1)
        else:
            data[-1].append(0)

def NumberSurrounding(current_data, point):
    surrounding = 0

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue

            coefficient = 1
            while True:
                row = point[0] + (i * coefficient)
                col = point[1] + (j * coefficient)

                if row < 0 or col < 0 or row >= len(current_data) or col >= len(current_data[0]):
                    break
                if current_data[row][col] == 1:
                    break
                if current_data[row][col] == 2:
                    surrounding += 1
                    break
                coefficient += 1

    return surrounding

def RunCycle(current_data):
    new_data = []
    for i, q in enumerate(current_data):
        new_data.append([])
        for j, r in enumerate(q):
            if r == 0:
                new_data[-1].append(0)
                continue

            surrounding = NumberSurrounding(current_data, [i, j])
            if (r == 2 and surrounding < 5) or (r == 1 and surrounding == 0):
                new_data[-1].append(2)
            else:
                new_data[-1].append(1)

    return new_data

old_data = []
while data != old_data:
    old_data = data
    data = RunCycle(data)

occupied = 0
for q in data:
    for r in q:
        if r == 2:
            occupied += 1

print(occupied)
