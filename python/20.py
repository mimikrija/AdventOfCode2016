# Day 20: Firewall Rules

from santas_little_helpers import *
from collections import deque



ranges = (list(map(int, line.split('-'))) for line in get_input('inputs/20'))


def find_smallest_allowed(in_forbidden):
    allowed = deque()
    allowed.append((0, 4294967295))
    forbidden = sorted(in_forbidden, key = lambda x: x[0])
    for e, f in forbidden:
        a, b = allowed.pop()
        if a == e:
            allowed.append((f+1, b))
        elif e > b or f < a:
            allowed.append((a,b))
        elif a < e < f < b:
            allowed.append((a, e-1))
            allowed.append((f+1, b))
        elif a < e < b < f:
            allowed.append((a, e-1))
        elif e < a < f < b:
            allowed.append((f+1, b))
        else:
            continue
        if len(allowed) == 2:
            return allowed[0][0]



part_1 = find_smallest_allowed(ranges)
print_solutions(part_1)
# Part 1 solution is: 31053880
