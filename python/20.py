# Day 20: Firewall Rules

from santas_little_helpers import *


ranges = sorted([tuple(map(int, line.split('-'))) for line in get_input('inputs/20')])


def find_lowest_allowed(in_forbidden, start=0):
    lowest_allowed = start
    for low, high in in_forbidden:
        if low <= lowest_allowed <= high:
            lowest_allowed = high + 1
    return lowest_allowed


def count_allowed(in_forbidden, limit=4294967295):
    lowest_allowed = 0
    counter = 0
    while True:
        lowest_allowed = find_lowest_allowed(in_forbidden, lowest_allowed+1)
        if lowest_allowed > limit:
            return counter
        counter += 1


part_1 = find_lowest_allowed(ranges)
part_2 = count_allowed(ranges)

print_solutions(part_1, part_2)
# Part 1 solution is: 31053880
# Part 2 solution is: 117
