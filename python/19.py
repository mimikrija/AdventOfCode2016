# Day 19: An Elephant Named Joseph
from santas_little_helpers import *

total_elves = 3014387

# create a circle
elves_circle = {elf_num: (elf_num * (elf_num < total_elves) + 1, 1) for elf_num in range(1, total_elves+1)}

while len(elves_circle) > 1:
    for current_elf in range(1, total_elves+1):
        if current_elf in elves_circle.keys():
            points_to, presents = elves_circle[current_elf]
            points_to_next, presents_to_steal = elves_circle[points_to]
            if presents_to_steal > 0:
                elves_circle[current_elf] = (points_to_next, presents + presents_to_steal)
                del elves_circle[points_to]

part_1 = list(elves_circle.keys())[0]
print_solutions(part_1)
# Part 1 solution is: 1834471
