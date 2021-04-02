lines = open('data').readlines()

data = []
for q in lines:
    split = q.split(' ')
    range_split = split[0].split('-')

    datapoint = {
            'min': int(range_split[0]),
            'max': int(range_split[1]),
            'letter': split[1][0],
            'password': split[2][0:-1]
            }

    data.append(datapoint)

valid_num = 0
invalid_num = 0
for q in data:
    real_num = 0
    for r in q['password']:
        if r == q['letter']:
            real_num += 1

    if real_num >= q['min'] and real_num <= q['max']:
        valid_num += 1
    else:
        invalid_num += 1

print('Valid:', valid_num, 'Invalid:', invalid_num)
