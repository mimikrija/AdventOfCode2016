with open('./inputs/01', 'r') as infile:
    directions = infile.readline().split(', ')

def get_direction(absolute_index):
    sides = ['n','e','s','w']
    absolute_index = absolute_index % 4
    return sides[absolute_index]

orientation_vector = {
    'n': (0, 1),
    'e': (1, 0),
    's': (0, -1),
    'w': (-1, 0)
}

def manhattan_distance(coordinate):
    return sum(abs(p) for p in coordinate)


absolute_index = 0
locations = []
solution_1 = (0,0)
solution_2 = None


for direction in directions:
    rotation, distance = direction[0], int(direction[1:])
    coordinate = solution_1

    if rotation == 'R':
        absolute_index += 1
    else:
        absolute_index -= 1
    global_direction = get_direction(absolute_index)

    solution_1 = tuple(solution_1[i] + orientation_vector[global_direction][i] * distance for i in range(2))

    # part 2:
    if solution_2 == None:
        for _ in range(distance):
            coordinate = tuple(coordinate[i] + orientation_vector[global_direction][i] for i in range(2))
            if coordinate in locations:
                solution_2 = coordinate
            locations.append(coordinate)

print ("Part one solution: I am ", manhattan_distance(solution_1), " blocks away!")
# Part one solution: I am  288  blocks away!

print ("Part two solution: Actually, the headquarters is ", manhattan_distance(solution_2), " blocks away!")
# Part two solution: Actually, the headquarters is  111  blocks away!
