strings = open('data').read().split("\n")
data = []
for q in strings:
    if q != '':
        data.append(int(q))

end = max(data)
saved = {}


def CountArrangement(start):
    global data
    global end
    global saved

    if start in saved:
        return saved[start]

    possibilities = []
    if start + 1 in data:
        possibilities.append(start + 1)
    if start + 2 in data:
        possibilities.append(start + 2)
    if start + 3 in data:
        possibilities.append(start + 3)

    arrangements = 0
    for q in possibilities:
        if q == end:
            arrangements += 1
        else:
            arrangements += CountArrangement(q)

    saved[start] = arrangements
    return arrangements


print(CountArrangement(0))
