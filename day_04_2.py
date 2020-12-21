with open('inputs/input_04.txt', 'r') as infile:
    passport_list = infile.read().split('\n\n')

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def check_field(field: str, value: str) -> bool:
    try:
        if field == 'byr':
            value = int(value)
            return 1920 <= value <= 2002
        elif field == 'iyr':
            value = int(value)
            return 2010 <= value <= 2020
        elif field == 'eyr':
            value = int(value)
            return 2020 <= value <= 2030
        elif field == 'hgt':
            if value[-2:] == 'cm':
                height = int(value[:-2])
                return 150 <= height <= 193
            elif value[-2:] == 'in':
                height = int(value[:-2])
                return 59 <= height <= 76
            else:
                return False
        elif field == 'hcl':
            return (len(value) == 7
                    and value[0] == '#'
                    and value[1:].isalnum()
                    and (value[1:].islower() or value[1:].isnumeric()))
        elif field == 'ecl':
            return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif field == 'pid':
            return value.isnumeric() and len(value) == 9
        elif field == 'cid':
            return True
        else:
            return False

    except ValueError:
        return False


valid_passports = 0

for passport in passport_list:
    valid = 1
    # check if all required fields exist
    for field in required_fields:
        valid *= passport.count(field)
    if not valid:
        continue
    # check if the fields are valid
    for element in passport.split():
        field, value = element.split(':')
        valid *= check_field(field, value)
    if valid == 1:
        valid_passports += 1

print(valid_passports)
