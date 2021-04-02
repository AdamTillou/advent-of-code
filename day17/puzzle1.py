def GetBlankGrid():  # {{{1
    grid = []
    for i in range(17):
        grid.append([])
        for j in range(24):
            grid[i].append([])
            for k in range(24):
                grid[i][j].append(0)
    return grid


def NumberSurrounding(grid, coord):  # {{{1
    surrounding = 0

    for i in [-1, 0, 1]:
        z = coord[0] + i
        if z < 0 or z > 16:
            continue

        for j in [-1, 0, 1]:
            x = coord[1] + j
            if x < 0 or x > 23:
                continue

            for k in [-1, 0, 1]:
                y = coord[2] + k

                if y < 0 or y > 23:
                    continue

                if i == 0 and j == 0 and k == 0:
                    continue

                if grid[z][x][y] == 1:
                    surrounding += 1

    return surrounding


def RunCycle(current_grid):  # {{{1
    new_grid = GetBlankGrid()

    for i, q in enumerate(current_grid):
        for j, r in enumerate(q):
            for k, s in enumerate(r):
                surrounding = NumberSurrounding(current_grid, [i, j, k])

                if s == 1 and (surrounding == 2 or surrounding == 3):
                    new_grid[i][j][k] = 1
                elif s == 0 and surrounding == 3:
                    new_grid[i][j][k] = 1

    return new_grid


def PrintLayout(grid):  # {{{1
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    indicators = 'A B C D E F G H I J K L M N O P Q R S T U V W X '
    for i, q in enumerate(grid):
        printlayer = 0
        string = '  ' + indicators + "\n"

        for j, r in enumerate(q):
            string += indicators[j * 2] + ' '

            for k, s in enumerate(r):
                if s == 1:
                    string += '🟥'
                else:
                    string += '⬛'

                if s != 0:
                    printlayer = 1
            string += "\n"

        if printlayer == 1:
            print("----------------------------")
            print(string)


# Get the data {{{1
data = open('data').read().split("\n")[0:-1]
global_grid = GetBlankGrid()
for i, q in enumerate(range(8, 16)):
    for j, r in enumerate(range(8, 16)):
        if data[i][j] == '#':
            global_grid[8][q][r] = 1

# Run the cycles {{{1
PrintLayout(global_grid)
for cycle in range(6):
    global_grid = RunCycle(global_grid)
    PrintLayout(global_grid)


# Count active cubes {{{1
active_cubes = 0
for i, q in enumerate(global_grid):
    for j, r in enumerate(q):
        for k, s in enumerate(r):
            if s == 1:
                active_cubes += 1

print(active_cubes)
print('hello')

