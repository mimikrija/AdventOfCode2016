# Day 19: An Elephant Named Joseph
from santas_little_helpers import *
from collections import deque

total_elves = 3014387


elves_circle = list(range(1,total_elves+1))

while len(elves_circle) > 1:
    if len(elves_circle)%2 == 1:
        elves_circle = elves_circle[::2][1:]
    else:
        elves_circle = elves_circle[::2]


part_1 = elves_circle.pop()
print_solutions(part_1)
# Part 1 solution is: 1834471
