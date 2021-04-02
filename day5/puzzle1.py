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

max_id = 0
for q in data:
    if len(q) != 10:
        continue

    seat_data = GetSeat(q)
    print(q, ":", str(seat_data))

    if seat_data['id'] > max_id:
        max_id = seat_data['id']

print(max_id)
