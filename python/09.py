# Day 9: Explosives in Cyberspace
import santas_little_helpers as helpers
import re

compressed_string = helpers.get_input('inputs/09','\n')[0]


def decompress(in_string):
    first_marker = re.search(r'(\d+)x(\d+)', in_string)
    if first_marker:
        count, multiply = map(int, first_marker.groups())
        before_marker_pos, after_marker_pos = first_marker.start()-1, first_marker.end()+1
        return before_marker_pos + multiply*count + decompress(in_string[after_marker_pos+count:])
    else:
        return len(in_string)



# part_1 = len(decompressed_string)
part_1 = decompress(compressed_string)

helpers.print_solutions(part_1)
# Part 1 solution is: 99145
