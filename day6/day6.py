from collections import defaultdict

def solve1(data):
    answers = defaultdict(set)
    group = 0
    
    for person_answers in data:
        if person_answers == '':
            group += 1
            continue

        answers[group].update(list(person_answers))

    answer_count = sum([len(v) for k, v in answers.items()])

    return answer_count

def solve2(data):
    answers = defaultdict(list)
    group = 0
    
    for person_answers in data:
        if person_answers == '':
            group += 1
            continue

        answers[group].append(set(person_answers))
    
    answer_count = 0
    
    for k, v in  answers.items():
        if len(v) == 1:
            answer_count += len(v[0])
            continue
        
        answer_count += len(set.intersection(*v))
    return answer_count
    
if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().splitlines()
        print("Part1: ", solve1(data))
        print("Part2: ", solve2(data))