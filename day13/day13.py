from functools import reduce

def solve1(data):
    earliest_time = int(data[0])
    ticks_to_wait = [(int(id), int(id) - earliest_time%int(id)) for id in data[1].split(',') if id != 'x']
    
    closest_departure = min(ticks_to_wait, key = lambda x: x[1])
    
    return closest_departure[0] * closest_departure[1]

# I'm just stealing the implementation for CRT from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
    
def solve2(data):
    ids = [(int(id), time) for time, id in enumerate(data[1].split(',')) if id != 'x']

    n = [x[0] for x in ids]
    a = [x[0] - x[1] for x in ids]
    
    return chinese_remainder(n, a)

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().splitlines()
        print("Part1: ", solve1(data))
        print("Part2: ", solve2(data))