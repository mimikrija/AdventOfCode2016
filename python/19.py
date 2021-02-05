# Day 19: An Elephant Named Joseph
from santas_little_helpers import *


total_elves = 3014387

def joseph(in_circle):
    if len(in_circle) == 1:
        return in_circle[0]
    else:
        if len(in_circle) % 2 == 1:
            return joseph(in_circle[::2][1:])
        else:
            return joseph(in_circle[::2])


elves_circle = list(range(1,total_elves+1))


part_1 = joseph(elves_circle)
print_solutions(part_1)
# Part 1 solution is: 1834471
