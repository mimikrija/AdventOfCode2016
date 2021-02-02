# Day 21: Scrambled Letters and Hash

from santas_little_helpers import *
from re import findall
from collections import namedtuple
from itertools import permutations

Instruction = namedtuple('Instruction',['command', 'args'])

def swap_position(in_string, pos_1, pos_2):
    return in_string[:pos_1] + in_string[pos_2] + in_string[pos_1+1:pos_2] + in_string[pos_1] + in_string[pos_2+1:]

def swap_letter(in_string, letter_1, letter_2):
    return in_string.translate(str.maketrans(letter_1+letter_2, letter_2+letter_1))

def rotate(in_string, rotate_by):
    """ rotates `in_string` by `rotate_by`. If `rotate_by` is positive it is
    the same as "rotate right", otherwise it is the same as "rotate left" """
    return in_string[-rotate_by:] + in_string[:-rotate_by]

def rotate_based(in_string, letter):
    letter_index = in_string.index(letter)
    rotate_by = (1 + letter_index + 1*(letter_index >= 4))%len(in_string)
    return rotate(in_string, rotate_by)

def reverse_positions(in_string, pos_1, pos_2):
    return in_string[:pos_1] + in_string[pos_1:pos_2+1][::-1] + in_string[pos_2+1:]

def move_position(in_string, pos_1, pos_2):
    letter = in_string[pos_1]
    remainder = in_string[:pos_1] + in_string[pos_1+1:]
    return remainder[:pos_2] + letter + remainder[pos_2:]

def single_scramble(command, args, in_string):
    if command == 'swap position':
        return swap_position(in_string, *sorted(args))
    if command == 'swap letter':
        return swap_letter(in_string, *args)
    if command == 'rotate left':
        return rotate(in_string, -args[0])
    if command == 'rotate right':
        return rotate(in_string, args[0])
    if command == 'rotate based':
        return rotate_based(in_string, args[0])
    if command == 'reverse positions':
        return reverse_positions(in_string, *sorted(args))
    if command == 'move position':
        return move_position(in_string, *args)

def scramble(in_string, instructions):
    scrambled = in_string
    for instruction in instructions:
        scrambled = single_scramble(*instruction, scrambled)
    return scrambled

def find_unscrambled(in_scrambled, instructions):
    for unscrambled in permutations(in_scrambled):
        candidate = ''.join(c for c in unscrambled)
        candidate = scramble(candidate, instructions)
        if candidate == in_scrambled:
            return candidate


instructions = []
for line in get_input('inputs/21'):
    command = ' '.join(word for word in line.split(' ')[:2])
    args = [word for word in line.split(' ') if len(word) == 1]
    if command in ('move position', 'reverse positions', 'swap position', 'rotate left', 'rotate right'):
        instructions.append(Instruction(command, list(map(int, args))))
    if command in ('swap letter', 'rotate based'):
        instructions.append(Instruction(command, args))


part_1 = scramble('abcdefgh', instructions)
part_2 = find_unscrambled('fbgdceah', instructions)

print_solutions(part_1, part_2)
# Part 1 solution is: dgfaehcb
# Part 2 solution is: fbgdceah
