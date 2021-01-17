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


def convert_coordinate_to_digit(coordinate, keypad):
    """ returns button digit/letter in `keypad` given its `coordinate`"""
    for digit, location in keypad.items():
        if coordinate == location:
            return digit


def translate_code(in_coords, keypad):
    """ translates list of button coordinates `in_coords` into a code based on `keypad` used """
    return "".join(convert_coordinate_to_digit(coordinate, keypad) for coordinate in in_coords)


def next_coordinate(coordinate, move, keypad):
    """ returns the next button coordinate `new_coordinate` given `coordinate`, `move` and `keypad`.
    if the new coordinate is out of bounds of `keypad` we stay where we were. """
    new_coordinate = coordinate + MOVE[move]
    if new_coordinate not in keypad.values():
        return coordinate
    else:
        return new_coordinate


def get_button(instruction, start, keypad):
    """ returns button coordinate after executing the row of movements """
    coordinate = start
    for move in instruction:
        coordinate = next_coordinate(coordinate, move, keypad)
    return coordinate


def bathroom_code(instructions, keypad, start_button = '5'):
    """ generates bathroom code following `instructions`, using `keypad` and starting from button `start_button` """
    code_coordinates = []
    button = keypad[start_button]
    for instruction in instructions:
        button = get_button(instruction, button, keypad)
        code_coordinates.append(button)
    return translate_code(code_coordinates, keypad)


instructions = helpers.get_input('inputs/02', '\n')

part_1 = bathroom_code(instructions, KEYPAD)
part_2 = bathroom_code(instructions, WACKY_KEYPAD)

print(part_1) # 99332
print(part_2) # DD483
