# Day 8: Two-Factor Authentication

import santas_little_helpers as helpers
import re
from collections import namedtuple

Instruction = namedtuple('Instruction', ['command', 'num_1', 'num_2'])


instructions = []
for line in helpers.get_input('inputs/08', '\n'):
    if 'rect' in line:
        instructions.append(Instruction(line.split(' ')[0], *map(int, re.findall(r'\d+', line))))
    else:
        instructions.append(Instruction(line.split(' ')[1], *map(int, re.findall(r'\d+', line))))

