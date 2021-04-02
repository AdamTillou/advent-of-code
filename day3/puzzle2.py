lines = open('data').readlines()
print('hi')

data = []
for q in lines:
    data.append(q[0:-1])

width = len(data[0])

def GetTrees(across, down):
    global data
    global width
    
    trees = 0
    count = 0
    
    line = 0
    column = 0
    while line < len(data):
        count += 1
        position = line * q['across']
        string_index = column % width

        if data[line][string_index] == '#':
            trees += 1

        line += down
        column += across
    return {'trees':trees, 'count':count}

slopes = [
        {'across':1, 'down':1},
        {'across':3, 'down':1},
        {'across':5, 'down':1},
        {'across':7, 'down':1},
        {'across':1, 'down':2}
        ]

product = 1
for q in slopes:
    output = GetTrees(q['across'], q['down'])
    trees = output['trees']
    count = output['count']
    
    print('Across:', q['across'], 'Down:', q['down'], 'Total:', count, 'Trees:', trees)
    
    product = product * trees

print('Product:', product)
