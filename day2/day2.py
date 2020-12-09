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
    return 0
    
if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().splitlines()
        print("Part1: ", solve1(data))
        print("Part2: ", solve2(data))