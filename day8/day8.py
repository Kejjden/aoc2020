def run_code(code):
    acc, index, visited_indexes = 0, 0, []
    program_len = len(code)
    
    while True:
        if (index in visited_indexes):
            return 1, acc, index
        elif index >= len(code):
            return 0, acc, index
        
        visited_indexes.append(index)

        op, arg = code[index].split(' ')
        arg = int(arg)
        
        if op == 'acc':
            acc += arg
        elif op == 'jmp':
            index += arg
            continue
            
        index += 1
        
    return acc, index

def get_next_change(index, data):
    for i in range(index, len(data)):
        if data[i][:3] == 'nop':
            return i, data[i].replace('nop', 'jmp')
        if data[i][:3] == 'jmp':
            return i, data[i].replace('jmp', 'nop')

def solve1(data):
    exit_code, acc, index = run_code(data)
    return acc

def solve2(data):
    change_index, change_instruction = get_next_change(0, data)
    
    for i in range(len(data)):
        changed_data = data.copy()
        changed_data[change_index] = change_instruction
        exit_code, acc, index = run_code(changed_data)
        
        if exit_code == 0:
            return acc

        change_index, change_instruction = get_next_change(change_index + 1, data)
    
    return 0

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().splitlines()
        print("Part1: ", solve1(data))
        print("Part2: ", solve2(data))