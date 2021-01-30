# Day 16: Dragon Checksum

from santas_little_helpers import *


def dragon(in_list):
    out_string = in_list + [False] + [not c for c in reversed(in_list)]
    return out_string

def dragon_rounds(in_string, limit):
    dragon_list = list(map(bool, map(int, in_string)))
    while len(dragon_list) < limit:
        dragon_list = dragon(dragon_list)
    return dragon_list[:limit]

def checksum(in_list):
    checksum = list(in_list)
    while len(checksum)%2 == 0:
        checksum = [one == two for one, two in zip(checksum[::2], checksum[1::2])]
    return "".join(str(int(c)) for c in checksum)


my_input = '11110010111001001'

part_1, part_2 = (checksum(dragon_rounds(my_input, disk_size)) for disk_size in {272, 35651584})
print_solutions(part_1, part_2)
# Part 1 solution is: 01110011101111011
# Part 2 solution is: 11001111011000111
