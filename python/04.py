# Day 4: Security Through Obscurity

import santas_little_helpers as helpers
import re
from collections import Counter, namedtuple

RoomData = namedtuple('RoomData', ['words', 'ID', 'checksum'])


def top_five(encrypted_name):
    # first sort by alphabet, then by number of occurrences
    sorted_counter = sorted(sorted(Counter(encrypted_name).items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
    return ''.join(c[0] for c in sorted_counter[:5])


def is_real_room(room):
    all_letters = "".join(c for word in room.words for c in word)
    if top_five(all_letters) == room.checksum:
        return room.ID
    else:
        return False


def rotate_letter(c, amount):
    wrap_around = lambda x: x if x <= ord('z') else x - 26
    offset = amount % 26
    return chr(wrap_around(ord(c) + offset))


def decipher_name(room):
    return (''.join(rotate_letter(c, room.ID) for c in word) for word in room.words)


def find_room(rooms, match):
    for room in filter(is_real_room, rooms):
        if match in decipher_name(room):
            return room.ID



raw_room_data = [re.findall(r'\w+', line) for line in helpers.get_input('inputs/04', '\n')]
rooms = [RoomData(raw_data[:-2], int(raw_data[-2]), raw_data[-1]) for raw_data in raw_room_data]

part_1 = sum(is_real_room(room) for room in rooms)
part_2 = find_room(rooms, 'object')

helpers.print_solutions(part_1, part_2)
# Part 1 solution is: 409147
# Part 2 solution is: 991
