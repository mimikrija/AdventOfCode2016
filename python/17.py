# Day 17: Two Steps Forward

from santas_little_helpers import *
from hashlib import md5
from itertools import product
from collections import deque

GRID = {complex(x, y) for x, y in product(range(4), repeat=2)}
start = 0+0j
vault = 3+3j

MOVE = {'U':  0-1j,
        'D':  0+1j,
        'L': -1+0j,
        'R':  1+0j,
        }


def paths_from_here(passcode, path_so_far):
    "returns possible directions based on md5 hash of `passcode`+`path`"
    seed = passcode + ''.join(c for c in path_so_far)
    return [direction for code, direction in zip(md5(seed.encode()).hexdigest()[:4], 'UDLR') if int(code, 16) > 10]


def open_neighbors(position, paths_from_coord):
    return {(position + MOVE[direction], direction) for direction in paths_from_coord if position + MOVE[direction] in GRID}


def BFS_shortest_distance(passcode, start, end, is_part_two=False):
    "Red blob games BFS with shortest distance from `start` to `end` implementation"
    frontier = deque()
    frontier.append((start, []))
    came_from = dict()
    came_from[start] = None
    longest_path_length = 0
    while frontier:
        current_position, path_so_far = frontier.pop()
        possible_paths = paths_from_here(passcode, path_so_far)
        if possible_paths:
            for next_position, direction in open_neighbors(current_position, possible_paths):
                # early exit if we found the goal (end) point
                if next_position == end:
                    if not is_part_two:
                        return ''.join(c for c in path_so_far + [direction])
                    else:
                        longest_path_length = max(longest_path_length, len(path_so_far)+1)
                else:
                    frontier.appendleft((next_position, path_so_far + [direction]))
                    came_from[next_position] = current_position
    return longest_path_length


passcode = 'bwnlcvfs'



part_1, part_2 = (BFS_shortest_distance(passcode, start, vault, is_part_two) for is_part_two in {False, True})
print_solutions(part_1, part_2)
# Part 1 solution is: DDURRLRRDD
# Part 2 solution is: 436
