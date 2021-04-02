data = open('data').read().split("\n\n")

necessary_items = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
        ]

valid_number = 0
invalid_number = 0

for q in data:
    is_valid = 1
    for r in necessary_items:
        if q.find(r + ':') == -1:
            is_valid = 0
            break

    if is_valid:
        valid_number += 1
    else:
        invalid_number += 1

print(valid_number, 'were valid,', invalid_number, 'were invalid')
