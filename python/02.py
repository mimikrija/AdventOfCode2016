import santas_little_helpers as helpers

DIGIT_LOCATION = {
    '1':-1+1j,
    '2': 0+1j,
    '3': 1+1j,
    '4':-1+0j,
    '5': 0+0j,
    '6': 1+0j,
    '7':-1-1j,
    '8': 0-1j,
    '9': 1-1j,
}

MOVE = {
    'U': 0+1j,
    'D': 0-1j,
    'R': 1+0j,
    'L':-1+0j,
}

def convert_location_to_digit(in_location):
    print(in_location)
    for digit, location in DIGIT_LOCATION.items():
        if in_location == location:
            return digit

def next_location(current_location, move):
    new_location = current_location + MOVE[move]
    if any(abs(num)>1 for num in {new_location.real, new_location.imag}):
        return current_location
    else:
        return new_location

def get_digit(instruction, starting_number):
    current_location = DIGIT_LOCATION[starting_number]
    for move in instruction:
        current_location = next_location(current_location, move)
    return convert_location_to_digit(current_location)

def get_code(instructions, start_from = '5'):
    code = ''
    current_digit = start_from
    for instruction in instructions:
        next_digit = get_digit(instruction, current_digit)
        code += next_digit
        current_digit = next_digit
    return code


instructions = helpers.get_input('inputs/02', '\n')

part_1 = get_code(instructions)

print(part_1) # 99332
