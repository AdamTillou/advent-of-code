data = open('data').read().split("\n")[0:-1]

ones = 0
# Start at one because distance to the phone will always be 3
threes = 1

current = 0
while True:
    if str(current + 1) in data:
        ones += 1
        current += 1
    elif str(current + 2) in data:
        current += 2
    elif str(current + 3) in data:
        threes += 1
        current += 3
    else:
        break

print(ones, threes, ones * threes)
