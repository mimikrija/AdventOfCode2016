# Day 22: Grid Computing

from santas_little_helpers import *
from re import findall
from collections import namedtuple, deque
from itertools import product

Node = namedtuple('Node', ['x', 'y', 'size', 'used', 'avail', 'use_percent'])

def are_same_node(node_A, node_B):
    return node_A.x == node_B.x and node_A.y == node_B.y


def is_viable_pair(node_A, node_B):
    if node_A.used == 0:
        return False
    if are_same_node(node_A, node_B):
        return False
    return node_A.used <= node_B.avail


def count_viable_pairs(in_data):
    return sum(is_viable_pair(in_data[one], in_data[two]) for one, two in product(range(len(in_data)), repeat=2))


def four_neighbors(in_coordinate, in_grid):
    "generates up, down, left, right neighbors of `in_coordinate`"
    x, y = in_coordinate
    return ({(x, y + delta) for delta in {1,-1}} | {(x + delta, y) for delta in {1,-1}}) & grid


def generate_grid(in_data, walls):
    return {(node.x, node.y) for node in in_data if (node.x, node.y) not in walls}


def BFS_shortest_distance(start, end, grid):
    "Red blob games BFS with shortest distance from `start` to `end` implementation"
    frontier = deque()
    frontier.append(start)
    came_from = dict()
    came_from[start] = None

    while frontier:
        current_position = frontier.pop()

        for next_position in four_neighbors(current_position, grid):
            if next_position not in came_from:
                frontier.appendleft(next_position)
                came_from[next_position] = current_position
            # early exit if we found the goal (end) point
            if next_position == end:
                return came_from


def path_length(start, end, grid):
    " backtracks from `end` to `start` and returns path length"
    came_from = BFS_shortest_distance(start, end, grid)
    current = end
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    return len(path)


nodes_data = [Node(*list(map(int, findall(r'\d+', line)))) for line in get_input('inputs/22')[2:]]

# part 1
part_1 = count_viable_pairs(nodes_data)



# part 2:

# define access node and goal node
access, goal = min(nodes_data, key= lambda n: n.x), max(nodes_data, key= lambda n: n.x)
goal_coordinate = (goal.x, goal.y)
access_coordinate = (access.x, access.y)

# find walls and the empty node
walls = set()
for node in nodes_data:
    if not any(is_viable_pair(node, other_node) for other_node in nodes_data):
        if node.used == 0:
            empty_coordinate = (node.x, node.y)
        else:
            walls.add((node.x, node.y))

# generate grid (set of coordinates excluding walls)
grid = generate_grid(nodes_data, walls)

count_steps_empty_to_goal = path_length(empty_coordinate, goal_coordinate, grid)
count_steps_goal_to_access = path_length(goal_coordinate, access_coordinate, grid)

# it takes five moves to shift the thing around and move node one place to the side
# we need to subtract one because the first shift around is already accounted for by the first part of the count
part_2 = count_steps_empty_to_goal + (count_steps_goal_to_access-1)*5

print_solutions(part_1, part_2)
# Part 1 solution is: 952
# Part 2 solution is: 181
