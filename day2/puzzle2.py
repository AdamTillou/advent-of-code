lines = open('data').readlines()

data = []
for q in lines:
    split = q.split(' ')
    range_split = split[0].split('-')

    datapoint = {
            'first': int(range_split[0]),
            'second': int(range_split[1]),
            'letter': split[1][0],
            'password': split[2][0:-1]
            }

    data.append(datapoint)

valid_num = 0
invalid_num = 0
for q in data:
    matches = 0
    
    if q['password'][q['first'] - 1] == q['letter']:
        matches += 1
    if q['password'][q['second'] - 1] == q['letter']:
        matches += 1
        
    if matches == 1:
        valid_num += 1
    else:
        invalid_num += 1

print('Valid:', valid_num, 'Invalid:', invalid_num)
