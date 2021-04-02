def GetBlankGrid():  # {{{1
    grid = []
    for h in range(17):
        grid.append([])
        for i in range(17):
            grid[h].append([])
            for j in range(24):
                grid[h][i].append([])
                for k in range(24):
                    grid[h][i][j].append(0)
    return grid


def NumberSurrounding(grid, coord):  # {{{1
    surrounding = 0

    for h in [-1, 0, 1]:
        w = coord[0] + h
        if w < 0 or w > 16:
            continue

        for i in [-1, 0, 1]:
            z = coord[1] + i
            if z < 0 or z > 16:
                continue

            for j in [-1, 0, 1]:
                x = coord[2] + j
                if x < 0 or x > 23:
                    continue

                for k in [-1, 0, 1]:
                    y = coord[3] + k

                    if y < 0 or y > 23:
                        continue

                    if h == 0 and i == 0 and j == 0 and k == 0:
                        continue

                    if grid[w][z][x][y] == 1:
                        surrounding += 1

    return surrounding


def RunCycle(current_grid):  # {{{1
    new_grid = GetBlankGrid()

    for h, p in enumerate(current_grid):
        for i, q in enumerate(p):
            for j, r in enumerate(q):
                for k, s in enumerate(r):
                    surrounding = NumberSurrounding(current_grid, [h, i, j, k])

                    if s == 1 and (surrounding == 2 or surrounding == 3):
                        new_grid[h][i][j][k] = 1
                    elif s == 0 and surrounding == 3:
                        new_grid[h][i][j][k] = 1

    return new_grid


# Get the data {{{1
data = open('data').read().split("\n")[0:-1]
global_grid = GetBlankGrid()
for i, q in enumerate(range(8, 16)):
    for j, r in enumerate(range(8, 16)):
        if data[i][j] == '#':
            global_grid[8][8][q][r] = 1

# Run the cycles {{{1
for cycle in range(6):
    global_grid = RunCycle(global_grid)

print('cycled')
# Count active cubes {{{1
active_cubes = 0
for p in global_grid:
    for q in p:
        for r in q:
            for s in r:
                if s == 1:
                    active_cubes += 1

print(active_cubes)
