# Day 3: Squares With Three Sides
import santas_little_helpers as helpers
import re

is_triangle = lambda x: x[0] + x[1] > x[2]

potential_triangles = [sorted(map(int, re.findall(r'\d+', line))) for line in helpers.get_input('inputs/03', '\n')]

part_1 = sum(is_triangle(candidate) for candidate in potential_triangles)

helpers.print_solutions(part_1)
