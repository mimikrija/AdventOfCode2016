# Day 22: Grid Computing

from santas_little_helpers import *
from re import findall
from collections import namedtuple

Node = namedtuple('Node', ['x', 'y', 'size', 'used', 'avail', 'use_percent'])

nodes_data = [Node(*list(map(int, findall(r'\d+', line)))) for line in get_input('inputs/22')[2:]]

