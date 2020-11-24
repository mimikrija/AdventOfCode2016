with open('./inputs/01', 'r') as infile:
    directions = infile.readline().split(', ')

def get_direction(absolute_index):
    sides = ['n','e','s','w']
    if absolute_index > 3 or absolute_index < -4:
        absolute_index = absolute_index % 4
    return sides[absolute_index]

def direction_factor(side):
    if side == 'n' or side == 'e':
        return 1
    else:
        return -1

def manhatan_distance(coordinate):
    return abs(coordinate[0]) + abs(coordinate[1])

horizontal_distance = 0
vertical_distance = 0
absolute_index = 0
locations = [(0,0)]
solution_2 = None

for direction in directions:
    rotation, distance = direction[0], int(direction[1:])
    x = 0
    y = 0
    if rotation == 'R':
        absolute_index += 1
    else:
        absolute_index -= 1
    global_direction = get_direction(absolute_index)
    sign = direction_factor(global_direction)
    if global_direction == 'n' or global_direction == 's':
        y = sign * distance
    if global_direction == 'e' or global_direction == 'w':
        x = sign * distance

    current = locations[-1]

    if solution_2 == None:
        dx = 0
        dy = 0
        for _ in range(distance):
            if global_direction == 'n' or global_direction == 's':
                dy += sign
                coordinate = (current[0],current[1]+dy)
            if global_direction == 'e' or global_direction == 'w':
                dx += sign
                coordinate = (current[0]+dx,current[1])
            if coordinate in locations:
                solution_2 = manhatan_distance(coordinate)
            locations.append(coordinate)
    locations.append((current[0]+x,current[1]+y))

print ("Part one solution: I am ", manhatan_distance(locations[-1]), " blocks away!")
# Part one solution: I am  288  blocks away!

print ("Part two solution: Actually, the headquarters is ", solution_2, " blocks away!")
# Part two solution: Actually, the headquarters is  111  blocks away!
