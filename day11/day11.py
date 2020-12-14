import copy

def check_hits(row):
    for tile in row:
        if tile == '#':
            return 1
        if tile == 'L':
            return 0
    return 0
    
def apply_new_rules(input_map):
    new_map = copy.deepcopy(input_map)
    map_width = len(input_map[0])
    map_height = len(input_map)
    change = False
    
    for y in range(0, map_height):
        for x in range(0, map_width):
            hits = 0
            if input_map[y][x] != '.':
                # Check Left
                hits += check_hits(reversed(input_map[y][:x]))
                # Check Right
                hits += check_hits(input_map[y][x + 1:])
                # Check up
                hits += check_hits(reversed([row[x] for index, row in enumerate(input_map) if index < y]))
                # Check down
                hits += check_hits([row[x] for index, row in enumerate(input_map) if index > y])
                # Check upleft
                hits += check_hits([input_map[row][col] for row,col in zip(reversed(range(0, y)), reversed(range(0, x)))])
                # Check downright
                hits += check_hits([input_map[row][col] for row,col in zip(range(y + 1, map_height), range(x + 1, map_width))])
                # Check upright
                hits += check_hits([input_map[row][col] for row,col in zip(reversed(range(0, y)), range(x + 1, map_width))])
                # Check downleft
                hits += check_hits([input_map[row][col] for row,col in zip(range(y + 1, map_height), reversed(range(0, x)))])
                
                if input_map[y][x] == 'L' and hits == 0:
                    new_map[y][x] = '#'
                    change = True
                elif input_map[y][x] == '#' and hits >= 5:
                    new_map[y][x] = 'L'
                    change = True
    
    return new_map if change else False

def apply_rules(input_map):
    l = len(input_map) - 1
    h = len(input_map[0]) - 1
    new_map = copy.deepcopy(input_map)
    change = False
    
    for y in range(1, l):
        for x in range(1, h):
            if input_map[y][x] != '.':
                occupied_count = (input_map[y-1][x-1:x+2] + 
                                input_map[y][x-1:x+2:2] + 
                                input_map[y+1][x-1:x+2]).count('#')
                if input_map[y][x] == 'L' and occupied_count == 0:
                    new_map[y][x] = '#'
                    change = True
                elif input_map[y][x] == '#' and occupied_count >= 4:
                    new_map[y][x] = 'L'
                    change = True
    
    return new_map if change else False

def solve1(data):
    data = [['.'] + list(row) + ['.'] for row in ['.' * len(data[0])] + data + ['.' * len(data[0])]]
    
    while True:
        step_changes = apply_rules(data)
        
        if not step_changes:
            return ''.join([''.join(x) for x in data]).count('#')
        
        data = step_changes
    
def solve2(data):
    data = [list(row) for row in data]

    while True:
        step_changes = apply_new_rules(data)
        
        if not step_changes:
            return ''.join([''.join(x) for x in data]).count('#')
        
        data = step_changes

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().splitlines()
        print("Part1: ", solve1(data))
        print("Part2: ", solve2(data))