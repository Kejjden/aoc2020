import math

def solve1(data):
    south = 0
    east = 0
    direction = 1
    degrees = 90
    operations = [{'code': x[0], 'param': int(x[1:])} for x in data]
    
    for op in operations:
        if op['code'] == 'F':
            if direction == 1:
                east += op['param']
            elif direction == 2:
                south += op['param']
            elif direction == 3:
                east -= op['param']
            elif direction == 4:
                south -= op['param']
        elif op['code'] == 'R':
            degrees += op['param']
            degrees = degrees % 360
            if degrees == 0:
                direction = 4
            elif degrees == 90:
                direction = 1
            elif degrees == 180:
                direction = 2
            elif degrees == 270:
                direction = 3
        elif op['code'] == 'L':
            degrees -= op['param']
            degrees = degrees % 360
            if degrees == 0:
                direction = 4
            elif degrees == 90:
                direction = 1
            elif degrees == 180:
                direction = 2
            elif degrees == 270:
                direction = 3
        elif op['code'] == 'N':
            south -= op['param']
        elif op['code'] == 'S':
            south += op['param']
        elif op['code'] == 'W':
            east -= op['param']
        elif op['code'] == 'E':
            east += op['param']

    return abs(south) + abs(east)
    

def rotate(ox, oy, px, py, angle):
    radians = math.radians(angle)
    
    qx = int(ox + math.cos(radians) * (px - ox) - math.sin(radians) * (py - oy))
    qy = int(oy + math.sin(radians) * (px - ox) + math.cos(radians) * (py - oy))
    return qx, qy

    
def solve2(data):
    waypoint_x, waypoint_y = 10, -1
    ship_x, ship_y = 0, 0

    operations = [{'code': x[0], 'param': int(x[1:])} for x in data]
    
    for op in operations:
        if op['code'] == 'F':
            diff_x = waypoint_x - ship_x
            diff_y = waypoint_y - ship_y
            
            ship_x += diff_x * op['param']
            ship_y += diff_y * op['param']
            
            waypoint_x += diff_x * op['param']
            waypoint_y += diff_y * op['param']
        elif op['code'] in ['R']:
            waypoint_x, waypoint_y = rotate(ship_x, ship_y, waypoint_x, waypoint_y, op['param'])
        elif op['code'] in ['L']:
            waypoint_x, waypoint_y = rotate(ship_x, ship_y, waypoint_x, waypoint_y, -op['param'])
        elif op['code'] == 'N':
            waypoint_y -= op['param']
        elif op['code'] == 'S':
            waypoint_y += op['param']
        elif op['code'] == 'W':
            waypoint_x -= op['param']
        elif op['code'] == 'E':
            waypoint_x += op['param']
        
    return abs(ship_x) + abs(ship_y)

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        data = input_file.read().splitlines()
        print("Part1: ", solve1(data))
        print("Part2: ", solve2(data))