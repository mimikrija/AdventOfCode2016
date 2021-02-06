# Day 24: Air Duct Spelunking

from santas_little_helpers import *
from itertools import permutations
from collections import deque


def four_neighbors(in_coordinate):
    "generates up, down, left, right neighbors of `in_coordinate`"
    x, y = in_coordinate
    return {(x, y + delta) for delta in {1,-1}} | {(x + delta, y) for delta in {1,-1}}


def open_neighbors(in_coordinate):
    "returns open (ie. not walls) neighbors of `in_coordinate`, taking into account that the map expands in the positive quadrant only (no negative coords allowed)."
    return {coordinate for coordinate in four_neighbors(in_coordinate) if coordinate in available_positions}


def BFS_shortest_distance(start, end):
    "Red blob games BFS with shortest distance from `start` to `end` implementation"
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
            # early exit if we found the goal (end) point
            if next_position == end:
                return came_from


def path_length(start, end):
    " backtracks from `end` to `start` and returns path length"
    came_from = BFS_shortest_distance(start, end)
    current = end
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    return len(path)



def add_distances(start, sequence, shortest_so_far):
    total_length = path_length(start, goals[sequence[0]])
    for stop_1, stop_2 in zip(sequence, sequence[1:]):
        if total_length >= shortest_so_far:
            return shortest_so_far
        total_length += path_length(goals[stop_1], goals[stop_2])

    return total_length

grid_input = get_input('inputs/24')

available_positions = set()
goals = {}
for row, line in enumerate(grid_input):
    for column, c in enumerate(line):
        if c != '#':
            available_positions.add((row,column))
            if c != '.':
                goals[c] = (row, column)

shortest = float('inf')
count = 0


for visit_sequence in permutations(sorted(goals.keys(), reverse=True)[:-1]):
    start_position = goals['0']
    # part 2: visit_sequence = list(visit_sequence) + ['0']
    shortest = min(shortest, add_distances(start_position, visit_sequence, shortest))
    count += 1
    if count % 200 == 0:
        print(count, shortest, visit_sequence)



print(count, shortest)
# part 1: 462
# part 2: 676