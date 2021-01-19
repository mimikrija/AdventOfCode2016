# Day 8: Two-Factor Authentication

import santas_little_helpers as helpers
import re
from collections import namedtuple

Instruction = namedtuple('Instruction', ['command', 'num_1', 'num_2'])


MAX_HORIZONTAL = 49
MAX_VERTICAL = 5

def rect(in_lights, row, column):
    return in_lights | {(x, y) for x in range(column) for y in range(row)}


def rotate_row(in_lights, row, by):
    in_row = {(x, y) for x, y in in_lights if x == row}
    return in_lights - in_row | {(x, helpers.add_wrap(y, by, MAX_HORIZONTAL)) for x, y in in_row}


def rotate_column(in_lights, column, by):
    in_column = {(x, y) for x, y in in_lights if y == column}
    return in_lights - in_column | {(helpers.add_wrap(x, by, MAX_VERTICAL), y) for x, y in in_column}


screen_commands = {'rect': rect,
                   'row': rotate_row,
                   'column': rotate_column,
                   }


def screen_lights_on(instructions):
    lights_on = set()
    for command, num_1, num_2 in instructions:
        lights_on = screen_commands[command](lights_on, num_1, num_2)
    return len(lights_on)


instructions = []
for line in helpers.get_input('inputs/08', '\n'):
    if 'rect' in line:
        instructions.append(Instruction(line.split(' ')[0], *map(int, re.findall(r'\d+', line))))
    else:
        instructions.append(Instruction(line.split(' ')[1], *map(int, re.findall(r'\d+', line))))

part_1 = screen_lights_on(instructions)

helpers.print_solutions(part_1)
# Part 1 solution is: 128

