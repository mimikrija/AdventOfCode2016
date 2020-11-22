with open('./inputs/01', 'r') as infile:
    directions = infile.readline().split(', ')

def get_direction(absolute_index):
    if absolute_index > 3:
        absolute_index = absolute_index % 4
    if absolute_index < -4:
        absolute_index = - (-absolute_index %4)
    return sides[absolute_index]


sides = ['n','e','s','w']


horizontal_distance = 0
vertical_distance = 0
absolute_index = 0
locations = [(0,0)]


for direction in directions:
    x = 0
    y = 0
    #print(direction)
    if direction[0] == 'R':
        absolute_index += 1
    else:
        absolute_index -= 1
    if get_direction(absolute_index) == 'n':
        x = int(direction[1:])
    if get_direction(absolute_index) == 's':
        x = - int(direction[1:])
    if get_direction(absolute_index) == 'e':
        y = int(direction[1:])
    if get_direction(absolute_index) == 'w':
        y = -int(direction[1:])
    vertical_distance += y
    horizontal_distance += x
    last = locations[-1]
    current = (last[0]+x,last[1]+y)
    locations.append(current)


print ("Part one solution: I am ", abs(vertical_distance) +abs(horizontal_distance), " blocks away!")
