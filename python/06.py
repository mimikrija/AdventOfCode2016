# Day 6: Signals and Noise

import santas_little_helpers as helpers
from collections import Counter

messages = helpers.get_input('inputs/06', '\n')

message_length = len(messages[0])

columns = [[line[column] for line in messages] for column in range(0, message_length)]


correct_message = [Counter(column).most_common(1)[0][0] for column in columns]

part_1 = "".join(c for c in correct_message)

helpers.print_solutions(part_1)
