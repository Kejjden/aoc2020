def check_hits_for(x_delta, y_delta, data):
    x, y = x_delta, y_delta
    h = len(data)
    w = len(data[0])
    hits = 0
    
    while y < h:
        if data[y][x%w] == "#":
            hits += 1

        x += x_delta
        y += y_delta
    
    return hits

def solve1(data):
    hits = check_hits_for(3, 1, data)
    return hits

def solve2(data):
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]
    
    slopes_hits = 1
    for slope in slopes:
        slopes_hits *= check_hits_for(slope[0], slope[1], data)
        
    return slopes_hits
    
if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().splitlines()
        print("Part1: ", solve1(data))
        print("Part2: ", solve2(data))