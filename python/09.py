# Day 9: Explosives in Cyberspace
import santas_little_helpers as helpers
import re

compressed_string = helpers.get_input('inputs/09','\n')[0]


def decompress(in_string, is_part_2=False):
    first_marker = re.search(r'(\d+)x(\d+)', in_string)
    if first_marker:
        count, multiply = map(int, first_marker.groups())
        before_marker_pos, after_marker_pos = first_marker.start()-1, first_marker.end()+1
        if not is_part_2:
            return before_marker_pos + multiply*count + decompress(in_string[after_marker_pos+count:])
        else:
            # if part we need to evaluate count recursively, but only within the marker + count!
            return before_marker_pos + multiply*decompress(in_string[after_marker_pos:after_marker_pos+count], True) + decompress(in_string[after_marker_pos+count:], True)
    else:
        return len(in_string)


part_1, part_2 = (decompress(compressed_string, is_part_2) for is_part_2 in {False, True})

helpers.print_solutions(part_1, part_2)
# Part 1 solution is: 99145
# Part 2 solution is: 10943094568
