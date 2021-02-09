# Day 25: Clock Signal
from santas_little_helpers import *
from math import factorial

instructions = [line.split(' ') for line in get_input('inputs/25')]


def assembunny(in_instructions, reg_a_value):
    pos = 0
    registers = {name: 0 for name in {'a', 'b', 'c', 'd'}}
    clock_signal = []
    registers['a'] = reg_a_value
    a_changes = []


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
        if operation == 'out':
            try:
                clock_signal.append(int(args[0]))
            except:
                clock_signal.append(registers[args[0]])
            print(args[0], clock_signal)
            a_changes.append(f"{registers['a']}, {registers['b']}, {registers['c']}, {registers['d']}  in position {pos}, clock: {clock_signal}")
        pos += 1

        a_changes.append(f"{registers['a']}, {registers['b']}, {registers['c']}, {registers['d']}  in position {pos}")
        if len(clock_signal) > 20:
            print(clock_signal)
            return a_changes, registers['a']
    return registers['a']

# look at values of 'a' over time to figure out a pattern
# results, a = assembunny(instructions, part_1)
# MyFile=open('inputs/23.out','w')
# for element in results:
#      MyFile.write(element)
#      MyFile.write('\n')
# MyFile.close()

# ok it seems that the output is a repeating (reversed) sequence of a binary representation of
# 2534 + inital register a value
# where 2534 = 7 * 362 (see 2nd and 3rd row of assembly input)

my_const = 7 * 362
goal_bin = '10' * ((len(bin(my_const))-2)//2)


input_dig = '100111100110'
goal_dig  = '101010101010'

part_1 = int(goal_dig,2) - my_const

print_solutions(part_1)
