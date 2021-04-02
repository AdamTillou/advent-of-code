data = open('data').read().split("\n\n")

total = 0
for q in data:
answers = 0
    alphabet = map(chr, range(97, 123))
    for r in alphabet:
        if q.find(r) != -1:
            answers += 1

    total += answers

print(total) 
