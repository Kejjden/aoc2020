import re

def solve1(data):
    valid = 0
    for row in data:
        row_parts = re.split(r'\:| |\-', row)
        
        min_occurance = int(row_parts[0])
        max_occurance = int(row_parts[1])
        occurance_char = row_parts[2]
        password = row_parts[4]

        occurances = password.count(occurance_char)

        if occurances >= min_occurance and occurances <= max_occurance:
            valid += 1
    return valid

def solve2(data):
    valid = 0
    for row in data:
        row_parts = re.split(r'\:| |\-', row)

        occurance_char = row_parts[2]
        password = row_parts[4]
        chars = [
            password[int(row_parts[0]) - 1],
            password[int(row_parts[1]) - 1]
        ]

        if chars.count(occurance_char) == 1:
            valid += 1
    return valid
    
if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().splitlines()
        print("Part1: ", solve1(data))
        print("Part2: ", solve2(data))