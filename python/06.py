# Day 6: Signals and Noise

import santas_little_helpers as helpers
from collections import Counter


def get_message(in_columns, is_part_2 = False):
    most_or_least_common = lambda x: Counter(x).most_common(1)[0][0] if not is_part_2 else Counter(x).most_common()[len(set(x))-1][0]
    return "".join(c for c in (most_or_least_common(column) for column in in_columns))


messages = helpers.get_input('inputs/06', '\n')

message_length = len(messages[0])
message_columns = [[line[column] for line in messages] for column in range(0, message_length)]


part_1, part_2 = (get_message(message_columns, is_part_2) for is_part_2 in {False, True})
helpers.print_solutions(part_1, part_2)
# Part 1 solution is: tsreykjj
# Part 2 solution is: hnfbujie
