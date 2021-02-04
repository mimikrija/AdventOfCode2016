# Day 19: An Elephant Named Joseph
from santas_little_helpers import *
from collections import deque

total_elves = 3014387

# create a circle
elves_circle = deque(range(1, total_elves+1))

while len(elves_circle) > 1:
    current_elf = elves_circle.popleft()
    next_elf = elves_circle.popleft()
    elves_circle.append(current_elf)

part_1 = elves_circle.pop()
print_solutions(part_1)
# Part 1 solution is: 1834471
