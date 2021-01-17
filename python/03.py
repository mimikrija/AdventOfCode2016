# Day 3: Squares With Three Sides
import santas_little_helpers as helpers
import re

is_triangle = lambda x: x[0] + x[1] > x[2]


potential_triangles = [list(map(int, re.findall(r'\d+', line))) for line in helpers.get_input('inputs/03', '\n')]

part_1 = sum(is_triangle(sorted(candidate)) for candidate in potential_triangles)



potential_vertical = []
for line_num in range(0, len(potential_triangles), 3):
    for n in range (0,3):
        potential_vertical.append([potential_triangles[line_num + offset][n] for offset in range(0,3)])


part_2 = sum(is_triangle(sorted(candidate)) for candidate in potential_vertical)

helpers.print_solutions(part_1, part_2)
# Part 1 solution is: 917
# Part 2 solution is: 1649
