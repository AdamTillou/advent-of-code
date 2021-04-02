lines = open('data').readlines()

data = []
for q in lines:
    data.append(q[0:-1])

width = len(data[0])
trees = 0
for i in range(len(data)):
    position = i * 3
    string_index = position % width

    if data[i][string_index] == '#':
        trees += 1

print('Total:', i + 1, 'Trees:', trees)
