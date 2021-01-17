# Day 4: Security Through Obscurity

import santas_little_helpers as helpers
import re
from collections import Counter

def top_five(encrypted_name):
    # first sort by alphabet, then by number of occurrences
    sorted_counter = sorted(sorted(Counter(encrypted_name).items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
    return ''.join(c[0] for c in sorted_counter[:5])


def is_real_room(room):
    encrypted_name = "".join(c for word in room[:-2] for c in word)
    sector_ID = int(room[-2])
    checksum = room[-1]
    #print(top_five(encrypted_name))
    if top_five(encrypted_name) == checksum:
        return sector_ID
    else:
        return False


rooms = [re.findall(r'\w+', line) for line in helpers.get_input('inputs/04', '\n')]

part_1 = sum(is_real_room(room) for room in rooms)



def rotate_letter(c, number):
    offset = number % 26
    total = ord(c) + offset
    if total <= ord('z'):
        return chr(total)
    else:
        return chr(ord('a')+total-ord('z')-1)

def decypher_name(room_data):
    result = []
    words, number = room_data[:-1], int(room_data[-1])
    for word in words:
        new = ''.join( rotate_letter(c, number) for c in word)
        result.append(new)
    return result


for room in rooms:
    if is_real_room(room):
        new = decypher_name(room[:-1])
        if 'object' in new:
            part_2 = int(room[-2])

helpers.print_solutions(part_1, part_2)
# Part 1 solution is: 409147
# Part 2 solution is: 991
