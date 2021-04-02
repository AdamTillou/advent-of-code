arrival = int(open('data').read().split("\n")[0])

busses = []
for q in open('data').read().split("\n")[1].split(','):
    if q != 'x' and q != '':
        busses.append(int(q))

first_bus = busses[0]
first_time = arrival % busses[0]
for q in busses:
    current_time = q - (arrival % q)
    if current_time < first_time:
        first_bus = q
        first_time = current_time

print(first_bus, first_time)
