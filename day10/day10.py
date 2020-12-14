import sys
import re
from collections import defaultdict
from itertools import permutations, groupby, islice

def get_jolt_differences(data):
    current_jolt = 0
    sorted_adapters = sorted(data)
    jolt_difference_counter = defaultdict(int)
    jolt_difference_counter[3] = 1
    for adapter in sorted_adapters:
        if adapter != current_jolt:
            difference = adapter - current_jolt
            jolt_difference_counter[difference] += 1
        current_jolt = adapter
    return dict(jolt_difference_counter)

def solve1(data):
    differences = get_jolt_differences(data)
    return differences[1] * differences[3]

def solve2(data):
    sorted_adapters = sorted(data)
    branches = [1] + [0] * len(sorted_adapters)
    sorted_adapters = [0] + sorted_adapters
    len_sorted_adapters = len(sorted_adapters)
    
    for i in range(len_sorted_adapters):
        next_adapter = i + 1
        while True:        
            if next_adapter >= len_sorted_adapters:
                break 
            if sorted_adapters[next_adapter] - sorted_adapters[i] > 3:
                break
            
            branches[next_adapter] += branches[i]
            next_adapter += 1
    return branches[-1]

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().splitlines()
        data = list(map(int, data))
        print("Part1: ", solve1(data))
        print("Part2: ", solve2(data))