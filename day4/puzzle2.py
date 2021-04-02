count = 0
def IsValid(argument):
    # Add an extra space to avoid extra conditions for end of string
    passport = str(argument) + "                                  "
    passport = passport.replace("\n", " ")

    # Parse birth year
    byr_index = passport.find('byr:')
    if not passport[byr_index + 4 : byr_index + 8].isdigit():
        return 'byr'
    byr_value = int(passport[byr_index + 4 : byr_index + 8])
    if byr_index == -1 or passport[byr_index + 8] != ' ' or byr_value < 1920 or byr_value > 2002:
        return 'byr ' + str(byr_value)

    # Parse issue year
    iyr_index = passport.find('iyr:')
    if not passport[iyr_index + 4 : iyr_index + 8].isdigit():
        return 'byr'
    iyr_value = int(passport[iyr_index + 4 : iyr_index + 8])
    if iyr_index == -1 or passport[iyr_index + 8] != ' ' or iyr_value < 2010 or iyr_value > 2020:
        return 'iyr ' + str(iyr_value)

    # Parse expiration year
    eyr_index = passport.find('eyr:')
    if eyr_index == -1 or not passport[eyr_index + 4 : eyr_index + 8].isdigit():
        return 'eyr'
    eyr_value = int(passport[eyr_index + 4 : eyr_index + 8])
    if  passport[eyr_index + 8] != ' ' or eyr_value < 2020 or eyr_value > 2030:
        return 'eyr ' + str(eyr_value)

    # Parse height
    hgt_index = passport.find('hgt:')
    if hgt_index == -1:
        return 'hgt'

    if passport[hgt_index + 6 : hgt_index + 8] == 'in' and passport[hgt_index + 8] == ' ':
        hgt_units = 'in'
        hgt_string = passport[hgt_index + 4 : hgt_index + 6]
    elif passport[hgt_index + 7 : hgt_index + 9] == 'cm' and passport[hgt_index + 9] == ' ':
        hgt_units = 'cm'
        hgt_string = passport[hgt_index + 4 : hgt_index + 7]
    else:
        return 'hgt bad value'

    if (not hgt_string.isdigit()):
        return 'hgt not number'
    hgt_value = int(hgt_string)
    if hgt_units == 'in' and (hgt_value < 59 or hgt_value > 76) or hgt_units == 'cm' and (hgt_value < 150 or hgt_value > 193):
        return 'hgt range'

    # Parse hair color
    hcl_index = passport.find('hcl:')
    if hcl_index == -1 or passport[hcl_index + 4] != '#' or passport[hcl_index + 11] != ' ':
        return 'hcl'

    hcl_value = passport[hcl_index + 5 : hcl_index + 11]
    valid_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']
    for q in hcl_value:
        if not q in valid_chars:
            return 'hcl invalid char'

    # Parse eye color
    ecl_index = passport.find('ecl:')
    if ecl_index == -1 or passport[ecl_index + 7] != ' ':
        return 'ecl'

    ecl_value = passport[ecl_index + 4 : ecl_index + 7]
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if not ecl_value in valid_colors:
        return 'ecl invalid color'

    # Parse PID
    pid_index = passport.find('pid:')
    if pid_index == -1 or passport[pid_index + 13] != ' ':
        return 'pid'

    pid_value = passport[pid_index + 4 : pid_index + 13]
    if not pid_value.isdigit():
        return 'pid not number'

    # If all checks passed without returning
    return 1



data = open('data').read().split("\n\n")

valid_number = 0
invalid_number = 0

for q in data:
    is_valid = IsValid(q)
    if is_valid == 1:
        print("\n\nValid:\n    ", q)
        valid_number += 1
    else:
        print("\n\nInvalid:\n    ", q.replace("\n", " "), "\n    Reason:", is_valid)
        invalid_number += 1

print(valid_number, 'were valid,', invalid_number, 'were invalid')
