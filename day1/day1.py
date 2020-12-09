import itertools

def solve1(data):
    combinations = itertools.combinations(data, 2)
    for x, y in combinations:
        if x + y == 2020:
            return x * y
            break

def solve2(data):
    combinations = itertools.combinations(data, 3)
    for x, y, z in combinations:
        if x + y + z == 2020:
            return x * y * z
            break
    
if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().splitlines()
        data = list(map(int, data))
        print("Part1: ", solve1(data))
        print("Part2: ", solve2(data))