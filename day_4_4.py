with open('inputs/input_4.txt', 'r') as infile:
    passport_list = infile.read().split('\n\n')

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_passports = 0

for passport in passport_list:
    valid = 1
    for field in required_fields:
        valid *= passport.count(field)
    if valid >= 1:
        valid_passports += 1

print(valid_passports)
