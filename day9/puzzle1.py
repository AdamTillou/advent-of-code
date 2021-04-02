data = open('data').read().split("\n")
while '' in data:
    data.remove('')

def IsValid(number, previous):
    for q in previous:
        num = q
        for r in previous:
            if q != r and q + r == number:
                return 1

    return 0

checknums = []
for i in range(25):
    checknums.append(int(data[i]))

for i in range(25, len(data) - 1):
    number = int(data[i])
    if not IsValid(number, checknums):
        print(number)

    checknums.remove(checknums[0])
    checknums.append(int(number))

print('done')
