# Day 23: Safe Cracking

from santas_little_helpers import *
from math import factorial

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
    a_changes = []

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
        a_changes.append(str(registers['a']) + ' in position ' + str(pos))
    return a_changes, registers['a']

results, part_1 = assembunny(instructions, 7)

# part 2: look at values of 'a' over time to figure out a faster way to solve ti
# MyFile=open('inputs/23.out','w')
# for element in results:
#      MyFile.write(element)
#      MyFile.write('\n')
# MyFile.close()

part_2 = factorial(12) + 79 * 74
print_solutions(part_1, part_2)
# Part 1 solution is: 10886
# Part 2 solution is: 479007446
