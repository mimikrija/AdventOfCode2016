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


def BFS_visit_everything(start, steps):
    frontier = deque()
    # we add a set of rings that make up a frontier. each frontier is one ring/step
    frontier.append({start})
    reached = set()
    reached.add(start)
    count = 0

    while frontier:
        current_frontier = frontier.pop()
        count += 1
        next_frontier = {next_position for current_position in current_frontier for next_position in neighbors(current_position) if next_position not in reached}
        frontier.append(next_frontier)
        reached |= next_frontier
        if count == steps:
            return len(reached)



# What is the fewest number of steps required for you to reach 31,39? (starting from 1,1)
start = (1,1)

goal = (31, 39)
#goal = (7, 4) # example

part_1 = path_length(start, goal)
part_2 = BFS_visit_everything(start, 50)

print_solutions(part_1, part_2)
# Part 1 solution is: 96
# Part 2 solution is: 141
