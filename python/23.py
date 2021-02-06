# Day 23: Safe Cracking

from santas_little_helpers import *

instructions = [line.split(' ') for line in get_input('inputs/23')]

def toggle(in_instruction):
    in_operation, *args = in_instruction
    if len(args) == 1:
        if in_operation == 'inc':
            out_operation = 'dec'
        else:
            out_operation ='inc'
    else:
        if in_operation == 'jnz':
            out_operation = 'cpy'
        else:
            out_operation = 'jnz'
    return [out_operation, *args]


def assembunny(in_instructions, reg_a_value):
    pos = 0
    registers = {name: 0 for name in {'a', 'b', 'c', 'd'}}
    registers['a'] = reg_a_value

    while pos < len(in_instructions):
        operation, *args = in_instructions[pos]

        if operation == 'cpy':
            try:
                registers[args[1]] = int(args[0])
            except:
                try:
                    registers[args[1]] = registers[args[0]]
                except:
                    pass
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
        if operation == 'tgl':
            try:
                offset = int(args[0])
            except:
                offset = registers[args[0]]
            try:
                in_instructions[pos+offset] = toggle(in_instructions[pos+offset])
            except:
                pass

        pos += 1
    return registers['a']

part_1 = assembunny(instructions, 7)
print_solutions(part_1)
# Part 1 solution is: 10886
