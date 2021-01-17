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
        return 0


rooms = [re.findall(r'\w+', line) for line in helpers.get_input('inputs/04', '\n')]

part_1 = sum(is_real_room(room) for room in rooms)

helpers.print_solutions(part_1)
