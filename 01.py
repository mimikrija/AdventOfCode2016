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


absolute_index = 0
locations = [(0,0)]
solution_2 = None
x = 0
y = 0

for direction in directions:
    rotation, distance = direction[0], int(direction[1:])
    coordinate = (x,y)

    if rotation == 'R':
        absolute_index += 1
    else:
        absolute_index -= 1
    global_direction = get_direction(absolute_index)
    sign = direction_factor(global_direction)
    if global_direction == 'n' or global_direction == 's':
        y += sign * distance
    if global_direction == 'e' or global_direction == 'w':
        x += sign * distance
    
    # part 2:
    if solution_2 == None:
        for _ in range(distance):
            if global_direction == 'n' or global_direction == 's':
                coordinate = (coordinate[0],coordinate[1]+sign)
            if global_direction == 'e' or global_direction == 'w':
                coordinate = (coordinate[0]+sign,coordinate[1])
            if coordinate in locations:
                solution_2 = manhatan_distance(coordinate)
            locations.append(coordinate)
#print (locations)
print ("Part one solution: I am ", manhatan_distance((x,y)), " blocks away!")
# Part one solution: I am  288  blocks away!

print ("Part two solution: Actually, the headquarters is ", solution_2, " blocks away!")
# Part two solution: Actually, the headquarters is  111  blocks away!
