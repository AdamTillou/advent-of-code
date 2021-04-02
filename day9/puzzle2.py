strings = open('data').read().split("\n")

data = []
for q in strings:
    if q != '':
        data.append(int(q))


def ContiguousSum(numlist):
    numsum = 0
    for q in numlist:
        numsum += q
    return numsum


special_num = 15353384
for i, q in enumerate(data):
    end = i + 1
    while end < len(data) and ContiguousSum(data[i:end]) < special_num:
        end += 1

    if ContiguousSum(data[i:end]) == special_num:
        print(data[i:end])
        print("Min:", min(data[i:end]),
              "Max:", max(data[i:end]),
              "Sum:", min(data[i:end]) + max(data[i:end]))
