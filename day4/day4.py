import ast
import re

def solve1(data):
    required_keys = [
        'byr:',
        'iyr:',
        'eyr:',
        'hgt:',
        'hcl:',
        'ecl:',
        'pid:'
    ]
    
    valid_passports = 0
    
    for passport in data:
        if all(key in passport for key in required_keys):
            valid_passports += 1
    return valid_passports

def solve2(data):
    valid_passports = 0
    
    for passport in data:
        passport = ast.literal_eval('{"' + passport.replace('\n', '","').replace(' ', '","').replace(':', '":"') + '"}')
        
        try:
            hgt_unit = passport["hgt"][-2:]
            
            if (int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002 and
                int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020 and
                int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030 and
                (
                    (hgt_unit == 'cm' and int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2]) <= 193) or
                    (hgt_unit == 'in' and int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2]) <= 76)
                ) and
                re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', passport['hcl']) and
                re.search(r'^[0-9]{9}$', passport['pid']) and
                passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                valid_passports += 1
        except:
            pass
        
    return valid_passports
    
if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().split('\n\n')
        print("Part1: ", solve1(data))
        print("Part2: ", solve2(data))