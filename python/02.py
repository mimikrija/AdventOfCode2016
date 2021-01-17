import santas_little_helpers as helpers

KEYPAD = {'1':-1+1j, '2': 0+1j, '3': 1+1j,
          '4':-1+0j, '5': 0+0j, '6': 1+0j,
          '7':-1-1j, '8': 0-1j, '9': 1-1j,
}

WACKY_KEYPAD= {           '1': 0+2j,
               '2':-1+1j, '3': 0+1j, '4': 1+1j,
    '5':-2+0j, '6':-1+0j, '7': 0+0j, '8': 1+0j, '9': 2+0j,
               'A':-1-1j, 'B': 0-1j, 'C': 1-1j,
                          'D': 0-2j,
}

MOVE = { 'U': 0+1j, 'D': 0-1j,
         'R': 1+0j, 'L':-1+0j,
}

def convert_location_to_digit(in_location, keypad):
    for digit, location in keypad.items():
        if in_location == location:
            return digit

def next_location(current_location, move, keypad):
    new_location = current_location + MOVE[move]
    if new_location not in keypad.values():
        return current_location
    else:
        return new_location

def get_digit(instruction, starting_number, keypad):
    current_location = keypad[starting_number]
    for move in instruction:
        current_location = next_location(current_location, move, keypad)
    return convert_location_to_digit(current_location, keypad)

def get_code(instructions, keypad, start_from = '5'):
    code = ''
    current_digit = start_from
    for instruction in instructions:
        next_digit = get_digit(instruction, current_digit, keypad)
        code += next_digit
        current_digit = next_digit
    return code


instructions = helpers.get_input('inputs/02', '\n')

part_1 = get_code(instructions, KEYPAD)
part_2 = get_code(instructions, WACKY_KEYPAD)

print(part_1) # 99332
print(part_2) # DD483
