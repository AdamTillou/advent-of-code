data = open('formatted_data').read().split("\n")

def BagsThatContain(color):
    global bags

    containing_list = []

    for q in bags:
        color_list = bags[q]
        if color in color_list:
            containing_list.append(q)

    return containing_list


# Parse the bag list
bags = {}
for q in data:
    if q == '':
        continue

    parent = q.split(':')[0]
    children = q.split(':')[1].split(',')

    bags[parent] = []

    for r in children:
        bags[parent].append(r)


bags_to_check = ['shiny gold']
valid_bags = []
while len(bags_to_check) > 0:
    next_bag = bags_to_check[0]
    bags_to_check.remove(next_bag)
    
    new_bags = BagsThatContain(next_bag)
    
    for q in new_bags:
        if not q in valid_bags:
            bags_to_check.append(q)
            valid_bags.append(q)

print(valid_bags)
print(len(valid_bags))
