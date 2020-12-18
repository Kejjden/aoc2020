from collections import deque

def solve1(data, target_round):
    history = deque(map(int, data))
    round_offset = len(history)
    game_round = len(history) + 1
    indices = {
        n: [i + 1] for i,n in enumerate(history)
    }
    
    last = history[-1]
    while game_round <= target_round:
        
        spoken = 0
        if last in indices.keys():
            if len(indices[last]) >= 2:
                spoken = indices[last][-1] - indices[last][-2]
                indices[last] = [indices[last][-1]]
        if spoken in indices.keys():
            indices[spoken].append(game_round)
        else:
            indices[spoken] = [game_round]
        
        last = spoken
        game_round += 1
    return last

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().split(',')
        print("Part1: ", solve1(data, 2020))
        print("Part2: ", solve1(data, 30000000))