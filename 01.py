with open('./inputs/01', 'r') as infile:
    directions = infile.readline().split(', ')

def get_direction(absolute_index):
    if absolute_index > 3 or absolute_index < -4:
        absolute_index = absolute_index % 4
    return sides[absolute_index]

def add_coordinates(start,end,locations):
    is_horizontal = False
    is_vertical = False
    if start[1] == end[1]: #horizontal movement
        is_horizontal = True
        range_start = start[0]
        range_end = end[0]
    else:
        is_vertical = True
        range_start = start[1]
        range_end = end[1]

    if range_end > range_start:
        step = 1
    else:
        step = -1

    coordinate = start
    for n in range (range_start + step,range_end,step):
            if is_horizontal:
                coordinate = (n, coordinate[1]) 
            else:
                coordinate = (coordinate[0], n)
            if coordinate in locations:
                solution_2 = abs(coordinate[0]) + abs(coordinate[1])
                return solution_2
            locations.append(coordinate)
    return None


sides = ['n','e','s','w']


horizontal_distance = 0
vertical_distance = 0
absolute_index = 0
locations = [(0,0)]
solution_2 = None

for direction in directions:
    x = 0
    y = 0
    if direction[0] == 'R':
        absolute_index += 1
    else:
        absolute_index -= 1
    if get_direction(absolute_index) == 'n':
        y = int(direction[1:])
    if get_direction(absolute_index) == 's':
        y = - int(direction[1:])
    if get_direction(absolute_index) == 'e':
        x = int(direction[1:])
    if get_direction(absolute_index) == 'w':
        x = -int(direction[1:])
    vertical_distance += y
    horizontal_distance += x
    current = (horizontal_distance,vertical_distance)
    if solution_2 == None:
        solution_2 = add_coordinates(locations[-1],current,locations)
    locations.append(current)

print ("Part one solution: I am ", abs(vertical_distance) +abs(horizontal_distance), " blocks away!")
# Part one solution: I am  288  blocks away!

print ("Part two solution: Actually, the headquarters is ", solution_2, " blocks away!")
# Part two solution: Actually, the headquarters is  111  blocks away!
