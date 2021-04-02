import math


# Figure out the least common multiple of the delays
def LeastCommonMultiple(x, y):
    if x > y:
        larger = x
        smaller = y
    else:
        larger = y
        smaller = x

    factors = GetPrimeFactors(smaller)

    lcm = larger
    for q in factors:
        if larger % q != 0:
            lcm *= q
        else:
            larger /= q

    return lcm


def GetPrimeFactors(num):
    for i in range(2, num + 1):
        if num % i == 0:
            new_num = int(num / i)
            if new_num == 1:
                return [i]
            else:
                return [i] + GetPrimeFactors(new_num)


# Read and parse the data
bus_string = open('data').read().split("\n")[1]

unsorted_busses = []
for i, q in enumerate(bus_string.split(',')):
    if q == '' or q == 'x':
        continue
    else:
        unsorted_busses.append({'total': -i, 'delay': int(q)})

# Combine busses that will arrive at the same time
combined_busses = []
for q in unsorted_busses:
    can_combine = False
    for r in combined_busses:
        if (r['total'] - q['total']) % q['delay'] == 0:
            can_combine = True
            r['delay'] = LeastCommonMultiple(r['delay'], q['delay'])
            break
        if (r['total'] - q['total']) % r['delay'] == 0:
            can_combine = True
            r['delay'] = LeastCommonMultiple(r['delay'], q['delay'])
            r['total'] = q['total']
            break

    if not can_combine:
        combined_busses.append(q)

# Sort the busses with the largest delay first
busses = []
while len(combined_busses) > 0:
    largest = {'delay': 0}
    for q in combined_busses:
        if q['delay'] > largest['delay']:
            largest = q

    busses.append(largest)
    combined_busses.remove(largest)

# Remove the bus with the largest delay from the list and assign it the leader
leader = busses[0]
busses.remove(leader)

# Calibrate each bus's total to be just higher than the leader's total,
# and give each bus a 'cycle' to show how far behind the leader they are
leader['total'] += leader['delay']
leader['cycle'] = 0
for q in busses:
    while q['total'] > leader['total']:
        q['total'] -= q['delay']
    while q['total'] < leader['total']:
        q['total'] += q['delay']
    q['cycle'] = 0

# Figure out how many of each bus delay goes into the largest bus delay
for q in busses:
    quotient = math.floor(leader['delay'] / q['delay'])
    q['jump'] = q['delay'] * quotient

# Figure out the delay where they all match
solved = -1
while solved == -1:
    leader['total'] += leader['delay']
    leader['cycle'] += 1

    for q in busses:
        behind = leader['cycle'] - q['cycle']
        q['total'] += behind * q['jump']
        q['cycle'] = leader['cycle']

        while q['total'] < leader['total']:
            q['total'] += q['delay']

        if q['total'] > leader['total']:
            break

        if q == busses[-1]:
            solved = leader['total']

print(solved)
