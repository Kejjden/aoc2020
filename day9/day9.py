from itertools import combinations

def solve1(data, offset):
    for number in range(offset, len(data)):
        look_behind = data[number-offset:number]
        look_behind_combos = list(combinations(look_behind, 2))
        look_behind_sums = [n + m for n, m in look_behind_combos]
        
        if not data[number] in look_behind_sums:
            return data[number]

def solve2(data, offset):
    invalid_number = solve1(data, offset)
    
    for data_index in range(0, len(data)):
        if data[data_index] > invalid_number:
            continue
           
        count, index = data[data_index], data_index
        visited_list=[data[data_index]]
        
        while count < invalid_number:
            index += 1
            count += data[index]
            visited_list.append(data[index])
            if count == invalid_number:
                return min(visited_list) + max(visited_list)
            
            if count >= invalid_number:
                break

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().splitlines()
        data = list(map(int, data))
        print("Part1: ", solve1(data, 25))
        print("Part2: ", solve2(data, 25))