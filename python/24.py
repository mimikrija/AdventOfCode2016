# Day 24: Air Duct Spelunking

from santas_little_helpers import *
from itertools import permutations, product, combinations
from collections import deque


def four_neighbors(in_coordinate):
    "generates up, down, left, right neighbors of `in_coordinate`"
    x, y = in_coordinate
    return {(x, y + delta) for delta in {1,-1}} | {(x + delta, y) for delta in {1,-1}}


def open_neighbors(in_coordinate):
    "returns open (ie. not walls) neighbors of `in_coordinate`, taking into account that the fixed map open coordinates (`open_coordinates`)"
    return {coordinate for coordinate in four_neighbors(in_coordinate) if coordinate in open_coordinates}


def BFS_visit_all(start, goals):
    "BFS visit everything from `start`, stop when `all_goals` are reached"
    frontier = deque()
    frontier.append(start)
    came_from = dict()
    came_from[start] = None

    while frontier:
        current_position = frontier.pop()
        for next_position in open_neighbors(current_position):
            if next_position not in came_from:
                frontier.appendleft(next_position)
                came_from[next_position] = current_position
            # early exit if we found all goals
            if all(goal in came_from for goal in goals):
                return came_from


def path_length(start, end, all_visited):
    " backtracks from `end` to `start` and returns path length"
    came_from = all_visited
    current = end
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    return len(path)


def travelling_salesman_in_a_maze(is_part_2=False):
    shortest = float('inf')
    for variable_sequence in permutations(points_to_visit):
        # we always start from 0, and visit the rest in whatever order
        visit_sequence = ['0'] + list(variable_sequence)
        # in case of part 2 we need to go back to the start 0
        if is_part_2:
            visit_sequence.append('0')
        total_length = sum(all_lengths[visit_pair] for visit_pair in zip(visit_sequence, visit_sequence[1:]))
        shortest = min(shortest, total_length)
    return shortest


grid_input = get_input('inputs/24')

# generate set of open coordinates + dict of goals to visit
open_coordinates = set()
goals = {}
for row, line in enumerate(grid_input):
    for column, c in enumerate(line):
        if c != '#':
            open_coordinates.add((row,column))
            if c != '.':
                goals[c] = (row, column)

points_to_visit = set(goals.keys()) - {'0'}

all_paths = {label: BFS_visit_all(location, goals.values()) for label, location in goals.items()}
all_lengths = {combo: path_length(goals[combo[0]], goals[combo[1]], all_paths[combo[0]])
                                     for combo in combinations(goals.keys(), 2)}
# this makes sure that tuples are interchangeable ie. we get the same
# distance for ('0','1') as for ('1', '0')
all_lengths |= {tuple(reversed(key)): value for key, value in all_lengths.items()}



part_1, part_2 = (travelling_salesman_in_a_maze(is_part_2) for is_part_2 in {False, True})
print_solutions(part_1, part_2)
# Part 1 solution is: 462
# Part 2 solution is: 676
