# Day 9: Explosives in Cyberspace
import santas_little_helpers as helpers
import re

compressed_string = helpers.get_input('inputs/09','\n')[0]


# decompressed_string = ''
rest = str(compressed_string)
decompressed_length = 0

while len(rest) > 0:
    try:
        first_marker = re.search(r'(\d+)x(\d+)', rest)
        count, multiply = map(int, first_marker.groups())
        before_marker_pos, after_marker_pos = first_marker.start()-1, first_marker.end()+1
        # decompressed_string += rest[:before_marker_pos] + multiply * rest[after_marker_pos:after_marker_pos+count]
        decompressed_length += before_marker_pos + multiply*count
        rest = rest[after_marker_pos+count:]
    except:
        decompressed_length += len(rest)
        # decompressed_string += rest
        rest = ''

# part_1 = len(decompressed_string)
part_1 = decompressed_length

helpers.print_solutions(part_1)
# Part 1 solution is: 99145
