# Day 21: Scrambled Letters and Hash

from santas_little_helpers import *
from re import findall
from collections import namedtuple

Instruction = namedtuple('Instruction',['command', 'args'])

instructions = []
for line in get_input('inputs/21'):
    command = ' '.join(word for word in line.split(' ')[:2])
    args = (word for word in line.split(' ') if len(word) == 1)
    if command in ('move position', 'reverse positions', 'swap position', 'rotate left', 'rotate right'):
        instructions.append(Instruction(command, map(int, args)))
    if command in ('swap letter', 'rotate based'):
        instructions.append(Instruction(command, args))

