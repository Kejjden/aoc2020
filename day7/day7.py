import re

def can_contain(contains, target, rules):
    if "no other" in [c['name'] for c in contains]:
        return False

    if target in [c['name'] for c in contains]:
        return True
    
    return any([can_contain(rules[c['name']], target, rules) for c in contains])

def parse_rules(data):
    rules = {}
    
    for rule in data:
        matches = re.findall(r'(\d+ )?([^\d\W]+ [^\d\W]+) ba', rule)
        rules[matches[0][1]] = [
            {"count":int(match[0]), "name":match[1]}  for match in matches[1:] 
            if match[0]
        ]
    
    return rules

def count_containing(target, rules, index):
    rule = rules[target]
    
    if rule:
        count = index
        for inner_bag in rule:
            count += inner_bag['count'] * count_containing(inner_bag['name'], rules, index)
        return count
    else:
        return 1

def solve1(data):
    target = 'shiny gold'

    rules = parse_rules(data)

    valid_colors = []

    for color, contains in rules.items():
        if can_contain(contains, target, rules):
            valid_colors.append(color)

    return len(valid_colors)

def solve2(data):
    rules = parse_rules(data)
    target = 'shiny gold'
    
    count = count_containing(target, rules, 1) - 1
    return count
    
if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().splitlines()
        print("Part1: ", solve1(data))
        print("Part2: ", solve2(data))