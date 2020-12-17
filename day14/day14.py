import re
import copy
from collections import defaultdict

def masked_value(value, mask):
    bits = list('{0:036b}'.format(int(value)))

    for m, v in mask:
        bits[m] = v

    return int(''.join(bits), 2)

def masked_permutations(bits, mask, index, perms):
    for i in range(index, len(mask)):
        if mask[i] == 'X':
            for replacement in ['0', '1']:
                changed = copy.deepcopy(bits) 
                changed[i] = replacement
                masked_permutations(changed, mask, i + 1, perms)
            break
            
    perms.add(int(''.join(bits), 2))

def masked_address(address, mask):
    bits = list('{0:036b}'.format(int(address)))

    for i in range(0, len(mask)):
        if mask[i] == '1':
            bits[i] = '1'

    perms = set()
    masked_permutations(bits, mask, 0, perms)
    
    return perms

def solve1(data):
    mem = defaultdict(int)
    mask = []
    for instruction in data:
        parts = re.findall(r'\w+|\d|\d+', instruction)

        if parts[0] == 'mask':
            mask = [(i, v) for i, v in enumerate(parts[1]) if v != 'X']
        elif parts[0] == 'mem':
            mem[parts[1]] = masked_value(parts[2], mask)

    return sum([v for k, v in mem.items()])

def solve2(data):
    mem = defaultdict(int)
    mask = []
    for instruction in data:
        parts = re.findall(r'\w+|\d|\d+', instruction)

        if parts[0] == 'mask':
            mask = list(parts[1])
        elif parts[0] == 'mem':
            addresses = masked_address(parts[1], mask)
            for a in addresses:
                mem[a] = int(parts[2])

    return sum([v for k, v in mem.items()])

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().splitlines()
        print("Part1: ", solve1(data))
        print("Part2: ", solve2(data))