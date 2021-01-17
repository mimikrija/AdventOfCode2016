# Day 3: Squares With Three Sides
import santas_little_helpers as helpers
import re

potential_triangles = [sorted(map(int, re.findall(r'\d+', line))) for line in helpers.get_input('inputs/03', '\n')]
