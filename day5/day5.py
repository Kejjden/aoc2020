
import math

def get_seat_number(seat):
    min_row, max_row = 0, 127
    min_col, max_col = 0, 7
    
    for direction in seat:
        if direction == "F":
            max_row = math.floor((min_row + max_row) / 2)
        elif direction == "B":
            min_row = math.ceil((min_row + max_row) / 2)
        elif direction == "L":
            max_col = math.floor((min_col + max_col) / 2)
        elif direction == "R":
            min_col = math.ceil((min_col + max_col) / 2)
    
    seat_number = max_row * 8 + max_col
    
    return seat_number

def solve1(data):
    highest_seat = 0

    for seat in data:
        seat_number = get_seat_number(seat)
        if seat_number > highest_seat:
            highest_seat = seat_number

    return highest_seat

def solve2(data):
    seats = []
    for seat in data:
        seats.append(get_seat_number(seat))
        
    for i in range(min(seats), max(seats)):
        if i not in seats and i + 1 in seats and i - 1 in seats:
            return i

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().splitlines()
        print("Part1: ", solve1(data))
        print("Part2: ", solve2(data))