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


def BFS_path(passcode, start, end, is_part_two=False):
    "Attempts to visit all possible locations from `start` to `end` given a `passcode`. Early exit for first found location (shortest distance) if `is_part_two` is not provided"
    frontier = deque()
    frontier.append((start, []))
    longest_path_length = 0

    while frontier:
        current_position, path_so_far = frontier.pop()
        possible_paths = paths_from_here(passcode, path_so_far)
        if possible_paths: # only proceed if this position is not a dead end, ie. possible_paths has at least one element
            for next_position, direction in open_neighbors(current_position, possible_paths):

                if next_position == end:
                    if not is_part_two:
                        return ''.join(c for c in path_so_far + [direction])
                    else:
                        longest_path_length = max(longest_path_length, len(path_so_far)+1)
                else:
                    frontier.appendleft((next_position, path_so_far+[direction]))
    return longest_path_length


passcode = 'bwnlcvfs'



part_1, part_2 = (BFS_path(passcode, start, vault, is_part_two) for is_part_two in {False, True})
print_solutions(part_1, part_2)
# Part 1 solution is: DDURRLRRDD
# Part 2 solution is: 436
