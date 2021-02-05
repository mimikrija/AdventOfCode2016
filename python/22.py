# Day 22: Grid Computing

from santas_little_helpers import *
from re import findall
from collections import namedtuple
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


nodes_data = [Node(*list(map(int, findall(r'\d+', line)))) for line in get_input('inputs/22')[2:]]

part_1 = count_viable_pairs(nodes_data)
print_solutions(part_1)
# Part 1 solution is: 952
