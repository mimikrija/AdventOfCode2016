# Day 18: Like a Rogue

from santas_little_helpers import *

# the 'is safe' conditions from the puzzle text translate to
# symmetric configurations of the above row, such as:
# .^., ^^^, ..., ^.^ - ie, we only need to check if first
# letter is equal to the last
def generate_next_row(in_row):
    above_row = [True] + in_row + [True]
    return [one == three for one, three in zip(above_row, above_row[2:])]


def count_safe(in_row, total_rows):
    next_row = list(in_row)
    count = 0
    for _ in range(total_rows):
        count += sum(next_row)
        next_row = generate_next_row(next_row)
    return count


first_row = [c=='.' for c in get_input('inputs/18')[0]]
part_1, part_2 = (count_safe(first_row, rows) for rows in {40, 400000})

print_solutions(part_1, part_2)
# Part 1 solution is: 1989
# Part 2 solution is: 19999894
