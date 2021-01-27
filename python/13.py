# Day 13: A Maze of Twisty Little Cubicles

from santas_little_helpers import *
from collections import deque
import itertools

my_input = 1358
#my_input = 10 # example


def is_open(in_coordinate):
    x, y = in_coordinate
    ones = bin(x*x + 3*x + 2*x*y + y + y*y + my_input).count('1')
    return ones % 2 == 0


def four_neighbors(in_coordinate):
    x, y = in_coordinate
    return {(x, y + delta) for delta in {1,-1}} | {(x + delta, y) for delta in {1,-1}}


def neighbors(in_coordinate):
    return {coordinate for coordinate in four_neighbors(in_coordinate) if all(coord >= 0 for coord in coordinate) and is_open(coordinate)}


def BFS_shortest_distance(start, end):
    """ Red blob games BFS with shortest distance implementation """
    frontier = deque()
    frontier.append(start)
    came_from = dict()
    came_from[start] = None

    while frontier:
        current_position = frontier.pop()
        for next_position in neighbors(current_position):
            if next_position not in came_from:
                frontier.appendleft(next_position)
                came_from[next_position] = current_position
            # early exit if we found the goal (end) point
            if next_position == end:
                return came_from


def path_length(start, end):
    came_from = BFS_shortest_distance(start, end)
    current = end
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    return len(path)


# What is the fewest number of steps required for you to reach 31,39? (starting from 1,1)
start = (1,1)

goal = (31, 39)
#goal = (7, 4) # example

part_1 = path_length(start, goal)
print_solutions(part_1)
# Part 1 solution is: 96
