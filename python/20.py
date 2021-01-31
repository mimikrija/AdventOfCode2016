# Day 20: Firewall Rules

from santas_little_helpers import *
from collections import deque


ranges = (tuple(map(int, line.split('-'))) for line in get_input('inputs/20'))


def find_lowest_allowed(in_forbidden):
    lowest_allowed = 0
    forbidden = sorted(in_forbidden, key = lambda x: x[0])
    for low, high in forbidden:
        if low <= lowest_allowed <= high:
            lowest_allowed = high + 1
    return lowest_allowed



part_1 = find_lowest_allowed(ranges)


print_solutions(part_1)
# Part 1 solution is: 31053880
