data = open('data').read().split("\n\n")

total = 0
for q in data:
    people = q.split("\n")
    answered_yes = map(chr, range(97, 123))

    for person in people:
        if person == '':
            continue

        new_list = []
        for question in answered_yes:
            if person.find(question) != -1:
                new_list.append(question)

        answered_yes = new_list

    total += len(answered_yes)

print(total) 
