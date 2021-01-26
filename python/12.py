# Day 12: Leonardo's Monorail

from santas_little_helpers import *

instructions = [line.split(' ') for line in get_input('inputs/12')]


def assembunny(in_instructions, is_part_2=False):
    pos = 0
    registers = {name: 0 for name in {'a', 'b', 'c', 'd'}}
    # part 2: initialize 'c' to 1 instead of 0
    if is_part_2:
        registers['c'] = 1

    while pos < len(in_instructions):
        operation, *args = in_instructions[pos]

        if operation == 'cpy':
            try:
                registers[args[1]] = int(args[0])
            except:
                registers[args[1]] = registers[args[0]]
        if operation == 'inc':
            registers[args[0]] += 1
        if operation == 'dec':
            registers[args[0]] -= 1
        if operation == 'jnz':
            try:
                compare = int(args[0])
            except:
                compare = registers[args[0]]
            if compare != 0:
                try:
                    pos += int(args[1]) - 1
                except:
                    pos += registers[args[1]] - 1
        pos += 1
    return registers


part_1, part_2 = (assembunny(instructions, is_part_2)['a'] for is_part_2 in {False, True})
print_solutions(part_1, part_2)
# Part 1 solution is: 318007
# Part 2 solution is: 9227661
