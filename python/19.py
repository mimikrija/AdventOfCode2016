# Day 19: An Elephant Named Joseph
from santas_little_helpers import *
from math import log


total_elves = 3014387


def joseph(in_circle):
    if len(in_circle) == 1:
        return in_circle[0]
    else:
        if len(in_circle) % 2 == 1:
            return joseph(in_circle[::2][1:])
        else:
            return joseph(in_circle[::2])


def joseph_accross(in_circle):
    size = len(in_circle)
    if size == 1:
        return in_circle[0]
    else:
        midway = size // 2
        return joseph_accross(in_circle[1:midway]+in_circle[midway+1:] + in_circle[:1])


def joseph_accross_formula(size):
    # solutions for size = 1..28 are:
    # 1: 1, 2: 1, 3: 3, 4: 1, 5: 2, 6: 3, 7: 5, 8: 7, 9: 9,
    # 10: 1, 11: 2, 12: 3, 13: 4, 14: 5, 15: 6, 16: 7, 17: 8, 18: 9,
    # 19: 11, 20: 13, 21: 15, 22: 17, 23: 19, 24: 21, 25: 23, 26: 25, 27: 27, 28: 1,
    # if n = 3^a, then the solution is n
    # if n = 3^a + l, where l <= 3^a, solution is l
    # otherwise the solution is an (l-3^a)th odd number greater than 3^a
    # where m = l
    highest_power = int(log(size, 3)) # a
    last_3_to_the_nth = 3**highest_power # 3^a
    rest = size - last_3_to_the_nth # l
    if rest == 0: # solution is n
        return size
    if rest <= last_3_to_the_nth:  # solution is l
        return rest
    else: # solution is (l-3^a)th odd number greater than 3^a
        return last_3_to_the_nth + 2*(rest-last_3_to_the_nth) + 1




elves_circle = list(range(1,total_elves+1))
part_1 = joseph(elves_circle)
part_2 = joseph_accross_formula(total_elves)

print_solutions(part_1, part_2)
# Part 1 solution is: 1834471
# Part 2 solution is: 1420064
