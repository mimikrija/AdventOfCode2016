# Day 18: Like a Rogue

from santas_little_helpers import *


def is_safe(left, right):
    if left == right:
        return '.'
    return '^'


def generate_next_row(in_row):
    above_row = ['.'] + in_row + ['.']
    return [is_safe(one, three) for one, three in zip(above_row, above_row[2:])]


def count_safe(in_row, total_rows):
    next_row = list(in_row)
    count = next_row.count('.')
    for _ in range(total_rows-1):
        next_row = generate_next_row(next_row)
        count += next_row.count('.')
    return count


first_row = [c for c in get_input('inputs/18')[0]]

part_1, part_2 = (count_safe(generate_map(first_row, rows)) for rows in {40, 400000})
print_solutions(part_1, part_2)
# Part 1 solution is: 1989
# Part 2 solution is: 19999894
