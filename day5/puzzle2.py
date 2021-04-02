def GetSeat(binary_string):
    row = 0
    for i in range(7):
        if binary_string[i] == 'F':
            val = 0
        else:
            val = 1

        row += val * (2 ** (6 - i))

    seat = 0
    for i in range(3):
        if binary_string[i + 7] == 'L':
            val = 0
        else:
            val = 1

        seat += val * (2 ** (2 - i))

    return {'row': row, 'seat': seat, 'id':(row * 8 + seat)}

data = open('data').read().split("\n")

id_set = set()
for q in data:
    if len(q) != 10:
        continue

    seat_data = GetSeat(q)
    id_set.add(seat_data['id'])

for q in id_set:
    if not q + 1 in id_set and q + 2 in id_set:
        print(q + 1)
